from flask import Flask, render_template, request, redirect, Response, jsonify,send_file
import base64
import random, json
import mysql.connector
from mySQLaddons import *
from pymongo import MongoClient
import gridfs
import io


app = Flask(__name__)
with open('dbCredentials.json') as f:
	dbCredential = json.load(f)['dbCredential']
	client=MongoClient('mongodb://uwrqa27evvnqagpaogv6:tz5OZNrmlZaSNY2dFYNr@bdeceu5bibkxahl-mongodb.services.clever-cloud.com:27017/bdeceu5bibkxahl')
	griddb = client.gridfs_example
	fs = gridfs.GridFS(griddb)
	rm=client.bdeceu5bibkxahl.roleModels
	r=client.bdeceu5bibkxahl.replicators
	rmAreas=client.bdeceu5bibkxahl.rmAreas
	rmPath=client.bdeceu5bibkxahl.rmPath
	rmBuildings=client.bdeceu5bibkxahl.rmBuildings
	rmTowns=client.bdeceu5bibkxahl.rmTowns
	photos=client.bdeceu5bibkxahl.images
	sites=client.bdeceu5bibkxahl.sites
	modelAction=client.bdeceu5bibkxahl.bestPractices

bui_types=[]
for x in rmBuildings.find({}):
	if 'BUI_TYP' in x['properties'].keys():
		bui_types.append(x['properties']['BUI_TYP'])
bui_types=list( dict.fromkeys(bui_types) )		


@app.route('/')
def index():
	return render_template('testindex.html')

@app.route('/test')
def test():
	return render_template('test.html', buiTypes=bui_types)

@app.route('/bestpractices')
def bestpractices():
	return render_template('bestpractices.html')

# @app.route('/initialMap',methods=['GET','POST'])
# def initialMap():
# 	# read json + reply
# 	request_arg=request.args.get('Role').replace('"','')

# 	cnx = connectToDB(dbCredential)

# 	cursor = cnx.cursor()

# 	query="SELECT * FROM ruritage_schema.%s;"%request_arg

# 	cursor.execute(query)

# 	row_headers=[x[0] for x in cursor.description]
# 	rv=cursor.fetchall()
# 	geojson=queryToGeoJSON(row_headers,rv)
# 	#print geojson
# 	return json.dumps(geojson)

@app.route('/querySIA',methods=['GET','POST'])
def querySIA():
	Roles=request.args.get('Roles').replace('"','')[1:-1].split(',')
	SIAs=request.args.get('SIAs').replace('"',"'")[1:-1].split(',')
	Roles=[x.encode('UTF8') for x in Roles]
	SIAs=[x.encode('UTF8') for x in SIAs]


	# SIAsList=', '
	# SIAsList=SIAsList.join(SIAs)


	# cnx = connectToDB(dbCredential)
	# cursor = cnx.cursor()

	# #Different type of query if we want both RM and R
	# if len(Roles)==1 and Roles[0]=='RoleModel':
	# 	#query="SELECT * FROM ruritage_schema.%s WHERE SIA IN (%s);"%(Roles[0],SIAsList)
	# 	query_template="SELECT %(x)s.Name, %(x)s.Role, %(x)s.Description, %(x)s.X, %(x)s.Y, %(x)s.MainEconomicSector, %(x)s.Ageing,\
	# 	%(x)s.Immigrant, %(x)s.Depopulation, %(x)s.Unemployment, %(x)s.Poverty , SIA.SIA FROM %(x)s INNER JOIN SIA ON %(x)s.SIA = SIA.idSIA WHERE SIA.SIA IN (%(y)s)"
	# 	query=query_template%{"x":Roles[0],"y":SIAsList}

	# elif len(Roles)==1 and Roles[0]=='Replicator':
	# 	query_template="SELECT %(x)s.Name, %(x)s.Role, %(x)s.Description, %(x)s.X, %(x)s.Y, null,null,\
	# 	null,null, null, null ,SIA.SIA FROM %(x)s INNER JOIN SIA ON %(x)s.SIA = SIA.idSIA\
	# 	WHERE SIA.SIA IN (%(y)s)"
	# 	query=query_template%{"x":Roles[0],"y":SIAsList}

	# if len(Roles)==2:
	# 	query_template1="SELECT %(x)s.Name, %(x)s.Role, %(x)s.Description, %(x)s.X, %(x)s.Y,%(x)s.MainEconomicSector,%(x)s.Ageing,\
	# 	%(x)s.Immigrant, %(x)s.Depopulation, %(x)s.Unemployment, %(x)s.Poverty ,SIA.SIA FROM %(x)s INNER JOIN SIA ON %(x)s.SIA = SIA.idSIA\
	# 	WHERE SIA.SIA IN (%(y)s)"

	# 	query_template2="SELECT %(x)s.Name, %(x)s.Role, %(x)s.Description, %(x)s.X, %(x)s.Y, null,null,\
	# 	null,null, null, null ,SIA.SIA FROM %(x)s INNER JOIN SIA ON %(x)s.SIA = SIA.idSIA\
	# 	WHERE SIA.SIA IN (%(y)s)"

	# 	query=query_template1%{"x":Roles[0],"y":SIAsList}+' UNION '+query_template2%{"x":Roles[1],"y":SIAsList}
	# 	print query
	
	# #code to avoid error in case no RM/R or SIA are selected
	# if Roles[0]!='' and SIAsList:
	# 	cursor.execute(query)
	# 	row_headers=[x[0] for x in cursor.description]
	# 	rv=cursor.fetchall()
	# 	geojson=queryToGeoJSON(row_headers,rv)
	# 	#print json.dumps(geojson,indent=4)
	# else:
	# 	geojson={}
	# 	geojson['type']='FeatureCollection'
	# 	geojson['features']=[]

	geojson={}
	geojson['type']='FeatureCollection'
	geojson['features']=[]
	invalid={'_id'}
	SIAs=[x[1:-1] for x in SIAs]

	if 'RoleModel' in Roles:
		for place in rm.find({'properties.SIA':{'$in':SIAs}}):
			item={x: place[x] for x in place if x not in invalid}
			geojson['features'].append(item)
	if 'Replicator' in Roles:
		for place in r.find({'properties.SIA':{'$in':SIAs}}):
			item={x: place[x] for x in place if x not in invalid}
			geojson['features'].append(item)


	return json.dumps(geojson)

@app.route('/queryBP',methods=['GET','POST'])
def queryBP():

	RM=request.args.get('RmID')

	output={}
	output['data']=[]

	invalid={'_id'}
	for bp in modelAction.find({'RM': 'rm'+RM},no_cursor_timeout=True):
		action={x: bp[x] for x in bp if x not in invalid}
		output['data'].append(action)	
	
	return json.dumps(output)

@app.route('/RMAreas',methods=['GET','POST'])
def RMAreas():
	#OLD FOR MYSQL
	# cnx = connectToDB(dbCredential)
	# cursor = cnx.cursor()
	# query="SELECT jsonpath from RMAreas"
	# cursor.execute(query)
	# row_headers=[x[0] for x in cursor.description]
	# rv=cursor.fetchall()


	# json_data=[]
	# for result in rv:
	# 	json_data.append(dict(zip(row_headers,result)))


	# output={}
	# output['data']=[]
	# for file in json_data:
	# 	with open(file['jsonpath'].encode('UTF8').replace("'",'')) as f:
	# 		geojson=json.load(f)
	# 		output['data'].append(geojson)



	#OLD FOR MONGO
	# json_data=None
	# for x in rmAreas.find({},no_cursor_timeout=True):
	# 	json_data=x['areasList']

	# print json_data
	# output={}
	# output['data']=[]
	# for j in json_data:
	# 	document=j['filename']
	# 	print document
	# 	for grid_out in fs.find({'filename':document},no_cursor_timeout=True):
	# 		output['data'].append(json.loads(grid_out.read()))

	output={}
	output['data']=[]
	document='LocalArea.json'
	invalid={'_id'}
	for pol in rmAreas.find({},no_cursor_timeout=True):
		area={x: pol[x] for x in pol if x not in invalid}	
		output['data'].append(area)	
	#output={}
	#output['data']=[]
	#document='LocalArea.json'
	#for grid_out in fs.find({},no_cursor_timeout=True):
	#	output['data'].append(json.loads(grid_out.read()))	

	return json.dumps(output)

@app.route('/RMPath',methods=['GET','POST'])
def RMPath():
	# cnx = connectToDB(dbCredential)
	# cursor = cnx.cursor()
	# query="SELECT jsonpath from RMPath"
	# cursor.execute(query)
	# row_headers=[x[0] for x in cursor.description]
	# rv=cursor.fetchall()
	# json_data=[]
	# for result in rv:
	# 	json_data.append(dict(zip(row_headers,result)))

	# output={}
	# output['data']=[]
	# for j in json_data:
	# 	document=j['jsonpath'].encode('UTF8').replace("'",'')
	# 	for grid_out in fs.find({'filename':document},no_cursor_timeout=True):
	# 		output['data'].append(json.loads(grid_out.read()))

	# output={}
	# output['data']=[]
	# for file in json_data:
	# 	with open(file['jsonpath'].encode('UTF8').replace("'",'')) as f:
	# 		geojson=json.load(f)
	# 		output['data'].append(geojson)

	json_data=None
	for x in rmPath.find({},no_cursor_timeout=True):
		json_data=x['pathsList']


	output={}
	output['data']=[]
	for j in json_data:
		document=j['filename']
		print document
		for grid_out in fs.find({'filename':document},no_cursor_timeout=True):
			output['data'].append(json.loads(grid_out.read()))

	return json.dumps(output)


@app.route('/buildings',methods=['GET','POST'])
def buildings():
	bounds=ast.literal_eval(request.args.get('bounds').encode('UTF8'))
	types=ast.literal_eval(request.args.get('bui_types').encode('UTF8'))
	rectangle={
			"type": "Polygon",
			"coordinates": [
				[
	                [
	                    bounds['_southWest']['lng'],bounds['_northEast']['lat']
	                ],
	                [
	                    bounds['_northEast']['lng'],bounds['_northEast']['lat']
	                ],
	                [
	                    bounds['_northEast']['lng'],bounds['_southWest']['lat']
	                ],
	                [
	                    bounds['_southWest']['lng'],bounds['_southWest']['lat']
	                ],
	                [
	                    bounds['_southWest']['lng'],bounds['_northEast']['lat']
	                ]
	            ]
	        ]
	    }
	#print rmBuildings.find({'coordinates':{ '$geoWithin': { '$geometry': rectangle } } },no_cursor_timeout=True).count()
	


	invalid={'_id'}
	output={ "type": "FeatureCollection", "features": []}

	for point in rmBuildings.find({'coordinates':{ '$geoWithin': { '$geometry': rectangle } }, 'properties.BUI_TYP':{'$in':types} },no_cursor_timeout=True):
		building={x: point[x] for x in point if x not in invalid}
		output['features'].append(building)


        if len(types)==0:
            output={ "type": "FeatureCollection", "features": []}
	return json.dumps(output)

@app.route('/towns',methods=['GET','POST'])
def towns():
	bounds=ast.literal_eval(request.args.get('bounds').encode('UTF8'))
	rectangle={
			"type": "Polygon",
			"coordinates": [
				[
	                [
	                    bounds['_southWest']['lng'],bounds['_northEast']['lat']
	                ],
	                [
	                    bounds['_northEast']['lng'],bounds['_northEast']['lat']
	                ],
	                [
	                    bounds['_northEast']['lng'],bounds['_southWest']['lat']
	                ],
	                [
	                    bounds['_southWest']['lng'],bounds['_southWest']['lat']
	                ],
	                [
	                    bounds['_southWest']['lng'],bounds['_northEast']['lat']
	                ]
	            ]
	        ]
	    }
	#print rmTowns.find({'coordinates':{ '$geoWithin': { '$geometry': rectangle } } },no_cursor_timeout=True).count()
	


	invalid={'_id'}
	output={ "type": "FeatureCollection", "features": []}

	for point in rmTowns.find({'coordinates':{ '$geoWithin': { '$geometry': rectangle } } },no_cursor_timeout=True):
		town={x: point[x] for x in point if x not in invalid}
		output['features'].append(town)


	return json.dumps(output)

@app.route('/sites',methods=['GET','POST'])
def Sites():
	bounds=ast.literal_eval(request.args.get('bounds').encode('UTF8'))
	rectangle={
			"type": "Polygon",
			"coordinates": [
				[
	                [
	                    bounds['_southWest']['lng'],bounds['_northEast']['lat']
	                ],
	                [
	                    bounds['_northEast']['lng'],bounds['_northEast']['lat']
	                ],
	                [
	                    bounds['_northEast']['lng'],bounds['_southWest']['lat']
	                ],
	                [
	                    bounds['_southWest']['lng'],bounds['_southWest']['lat']
	                ],
	                [
	                    bounds['_southWest']['lng'],bounds['_northEast']['lat']
	                ]
	            ]
	        ]
	    }
	#print rmTowns.find({'coordinates':{ '$geoWithin': { '$geometry': rectangle } } },no_cursor_timeout=True).count()
	


	invalid={'_id'}
	output={ "type": "FeatureCollection", "features": []}

	for point in sites.find({'coordinates':{ '$geoWithin': { '$geometry': rectangle } } },no_cursor_timeout=True):
		site={x: point[x] for x in point if x not in invalid}
		output['features'].append(site)


	return json.dumps(output)




@app.route('/images',methods=['GET','POST'])
def images():
	bounds=ast.literal_eval(request.args.get('bounds').encode('UTF8'))
	rectangle={
			"type": "Polygon",
			"coordinates": [
				[
	                [
	                    bounds['_southWest']['lng'],bounds['_northEast']['lat']
	                ],
	                [
	                    bounds['_northEast']['lng'],bounds['_northEast']['lat']
	                ],
	                [
	                    bounds['_northEast']['lng'],bounds['_southWest']['lat']
	                ],
	                [
	                    bounds['_southWest']['lng'],bounds['_southWest']['lat']
	                ],
	                [
	                    bounds['_southWest']['lng'],bounds['_northEast']['lat']
	                ]
	            ]
	        ]
	    }
	#print images.find({'coordinates':{ '$geoWithin': { '$geometry': rectangle } } },no_cursor_timeout=True).count()
	


	invalid={'_id'}
	output={'images':[]}

	#Serve un ciclo che cerchi tutte le immagini per ogni sito edificio citta etc, ogni cosa che puo avere immagini

	for point in sites.find({'coordinates':{ '$geoWithin': { '$geometry': rectangle } } },no_cursor_timeout=True):
		for grid_out in fs.find({'filename':point['properties']['IMAGE']},no_cursor_timeout=True):
			image_binary= grid_out.read()
			output['images'].append(base64.b64encode(image_binary))


	return json.dumps(output)


@app.route('/palestina',methods=['GET','POST'])
def palestina():
	with open('static/db/PalestinaBuilding.json') as f:
		geojson=json.load(f)
	return json.dumps(geojson)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0')
    #app.run(host='127.0.0.2')
