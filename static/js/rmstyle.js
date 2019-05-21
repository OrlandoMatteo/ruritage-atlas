function RMStyle(feature,latlng){
	switch (feature.properties["SIA"]){
		case "Sustainable food production":
			var SIA1Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: 'white',
                    markerColor: 'lightgreen',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
		return L.marker(latlng, {icon: SIA1Icon});
		case "Pilgrimage":
			var SIA2Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: 'white',
                    markerColor: 'beige',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
		return L.marker(latlng, {icon: SIA2Icon});
		case "Migration":
			var SIA3Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: 'white',
                    markerColor: 'gray',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
		return L.marker(latlng, {icon: SIA3Icon});		
	}
}

//	var geolayer=data
//        var geo_json_19c7b17f4e1841ca929eb8534cf3813c = L.geoJson(geolayer,{pointToLayer: RMStyle}).addTo(map_edd0f5c3f36548d5a1e0c288d022407d);
//        geo_json_19c7b17f4e1841ca929eb8534cf3813c.setStyle(function(feature) {return feature.properties.style;});
