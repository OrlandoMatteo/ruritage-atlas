import json
import ast
import mysql.connector
def queryToGeoJSON(row_headers,rv):
	json_data=[]
	for result in rv:
		json_data.append(dict(zip(row_headers,result)))
	#print json_data
	geojson={}
	geojson['type']='FeatureCollection'
	geojson['features']=[]
	for x in json_data:
		feature={}
		feature['type']='Feature'
		feature['properties']={}
		feature['properties']['Name']=x['Name']
		feature['properties']['Role']=x['Role']
		feature['properties']['SIA']=x['SIA']
		feature['properties']['Description']=x['Description']
		if x['Role']=='RM':
			pass
			feature['properties']['MainEconomicSector']=x['MainEconomicSector']
			feature['properties']['Ageing']=x['Ageing']
			feature['properties']['Immigrant']=x['Immigrant']
			feature['properties']['Depopulation']=x['Depopulation']
			feature['properties']['Unemployment']=x['Unemployment']
			feature['properties']['Poverty']=x['Poverty']
		feature['geometry']={}
		feature['geometry']['type']='Point'
		feature['geometry']['coordinates']=[x['X'],x['Y']]
		geojson['features'].append(feature)

	return geojson


def queryToBPJSON(row_headers,rv):
	json_data=[]
	jsonBP={'BestPractices':[]}
	for result in rv:
		json_data.append(dict(zip(row_headers,result)))

	for x in json_data:
		if not any(d.get('idBestPractice')==x['idBestPractice'] for d in jsonBP['BestPractices']):
			practice={}
			practice['idBestPractice']=x['idBestPractice']
			practice['BPName']=x['BPName'].encode('UTF8')
			practice['SIA']=x['SIA'].encode('UTF8')
			practice['RM']=x['Name'].encode('UTF8')
			practice['CCs']=[]
			practice['CCs'].append(x['CCName'].encode('UTF8'))
			jsonBP['BestPractices'].append(practice)
		else:
			practice=next(d for d in jsonBP['BestPractices'] if d['idBestPractice']==x['idBestPractice'] )
			practice['CCs'].append(x['CCName'].encode('UTF8'))
	return jsonBP


def connectToDB(dbCredential):
	cnx = mysql.connector.connect(user=dbCredential['user'], password=dbCredential['password'],
                              host=dbCredential['host'],
                              database=dbCredential['database'])
	return cnx