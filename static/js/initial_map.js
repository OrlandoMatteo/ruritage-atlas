function add_Palestina() {
    // Clear all the except the basemap
   main_map.eachLayer(function (layer){
        if (layer!=openstreetmap_layer) {
           main_map.removeLayer(layer);
        }
    });

    var feature_group_a32ec62d2f314c55932bc7860f17d4a2 = L.featureGroup(
    ).addTo(map_b6fc3204b5d34ff8989110f473c0a67b);


    var marker_ec7364ff785948508a8693bc674b06eb = L.marker(
    [5.01902, -75.621562],
    {
        icon: new L.Icon.Default()
        }
    ).addTo(feature_group_a32ec62d2f314c55932bc7860f17d4a2);



    var icon_d606d9d2a28a460a82e116ca563e5288 = L.AwesomeMarkers.icon({
            icon: 'trophy',
            iconColor: 'white',
            markerColor: 'lightgreen',
            prefix: 'fa',
            extraClasses: 'fa-rotate-0'
            });
        marker_ec7364ff785948508a8693bc674b06eb.setIcon(icon_d606d9d2a28a460a82e116ca563e5288);


    var popup_15c0374a577b471f94c31eb4f3924d12 = L.popup({maxWidth: '300'

    });


    var html_9c9e615a29d6467c8b079e6eda219570 = $(`<div id="html_9c9e615a29d6467c8b079e6eda219570" style="width: 100.0%; height: 100.0%;">Palestina</div>`)[0];
        popup_15c0374a577b471f94c31eb4f3924d12.setContent(html_9c9e615a29d6467c8b079e6eda219570);


    marker_ec7364ff785948508a8693bc674b06eb.bindPopup(popup_15c0374a577b471f94c31eb4f3924d12)
;
}
function add_Replica(){
    // Clear all the except the basemap
   main_map.eachLayer(function (layer){
        if (layer!=openstreetmap_layer) {
           main_map.removeLayer(layer);
        }
    });



    var feature_group_22c215746edc41d4add4940b921b6053 = L.featureGroup(
                ).addTo(map_b6fc3204b5d34ff8989110f473c0a67b);
        
    
    var marker_1e94c4c873864b729344f20aabb052da = L.marker(
            [45, -75.621562],
            {
                icon: new L.Icon.Default()
                }
            ).addTo(feature_group_22c215746edc41d4add4940b921b6053);
        
    

     var icon_fd6df06ccdfb4bb89fd3b07b01e1a6a0 = L.AwesomeMarkers.icon({
                    icon: 'leaf',
                    iconColor: 'white',
                    markerColor: 'lightgreen',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
    marker_1e94c4c873864b729344f20aabb052da.setIcon(icon_fd6df06ccdfb4bb89fd3b07b01e1a6a0);
            
    
    var popup_a931dc205b904e72baa4c8dc9eb3dbe9 = L.popup({maxWidth: '300'
            
            });

            
    var html_1ea603008dd844c0aba8bd3898da3efe = $(`<div id="html_1ea603008dd844c0aba8bd3898da3efe" style="width: 100.0%; height: 100.0%;">Replica</div>`)[0];
                popup_a931dc205b904e72baa4c8dc9eb3dbe9.setContent(html_1ea603008dd844c0aba8bd3898da3efe);
            

     marker_1e94c4c873864b729344f20aabb052da.bindPopup(popup_a931dc205b904e72baa4c8dc9eb3dbe9)
            ;
}

function add_video() {
    // body...
    var marker_video = L.marker(
            [45, -75.621562],
            {
                icon: new L.Icon.Default()
                }
            ).addTo(main_map);
        
    

     var icon_fd6df06ccdfb4bb89fd3b07b01e1a6a0 = L.AwesomeMarkers.icon({
                    icon: 'video',
                    iconColor: 'white',
                    markerColor: 'red',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
    marker_video.setIcon(icon_fd6df06ccdfb4bb89fd3b07b01e1a6a0);
            
    
    var popup_a931dc205b904e72baa4c8dc9eb3dbe9 = L.popup({maxWidth: '300'
            
            });
    popup_a931dc205b904e72baa4c8dc9eb3dbe9.setContent('<video width="300" src="https://magmageopark.no/wp-content/uploads/2018/05/Magma-Webside-test2.mp4" type="video/mp4" controls></video>')    
    //popup_a931dc205b904e72baa4c8dc9eb3dbe9.setContent('<p>Hello world!<br />This is a nice popup.</p>');
    marker_video.bindPopup(popup_a931dc205b904e72baa4c8dc9eb3dbe9);
}

function add3d() {
    // body...
    var marker_3d = L.marker(
            [45, -75.621562],
            {
                icon: new L.Icon.Default()
                }
            ).addTo(main_map);
        
    

     var icon_3d = L.AwesomeMarkers.icon({
                    icon: 'video',
                    iconColor: 'white',
                    markerColor: 'red',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
    marker_3d.setIcon(icon_3d);
            
    
    var popup_3d = L.popup({maxWidth: '300'
            
            });
    popup_3d.setContent('<iframe src="http://localhost:8080/test3D"></iframe>')    
    //popup_a931dc205b904e72baa4c8dc9eb3dbe9.setContent('<p>Hello world!<br />This is a nice popup.</p>');
    marker_3d.bindPopup(popup_3d);
}

function onEachEntity(feature, layer) {

        layer.bindTooltip(feature.properties.Name);

}

function addRM(data) {
    // body...
    /*   main_map.eachLayer(function (layer){
        if (layer!=openstreetmap_layer) {
           main_map.removeLayer(layer);
        }
    });*/
    main_map.eachLayer(function (layer){
        if (layer.feature) {
            if(layer.feature.properties.Role=='RM'){
                main_map.removeLayer(layer);
            }
        }
    });
    var geolayer=data;
        var geo_json_RoleModels = L.geoJson(geolayer,{pointToLayer: RMStyle, onEachFeature:onEachEntity}).addTo(main_map);
        geo_json_RoleModels.setStyle(function(feature) {return feature.properties.style;});
        
    
            /*var layer_control_463e2c303f5641a796469364c8a0a5cf = {
                base_layers : { "openstreetmap" : openstreetmap_layer, },
                overlays : { "macro_element_19c7b17f4e1841ca929eb8534cf3813c" : geo_json_19c7b17f4e1841ca929eb8534cf3813c, }
                };
            L.control.layers(
                layer_control_463e2c303f5641a796469364c8a0a5cf.base_layers,
                layer_control_463e2c303f5641a796469364c8a0a5cf.overlays,
                {position: 'topright',
                 collapsed: true,
                 autoZIndex: true
                }).addTo(main_map);*/
}
function addReplicator(data) {
    // body...
    main_map.eachLayer(function (layer){
        if (layer.feature) {
            if(layer.feature.properties.Role=='R'){
                main_map.removeLayer(layer);
            }
        }
    });

        var geolayer=data;
        var geo_json_Replicators = L.geoJson(geolayer,{pointToLayer: ReplicatorStyle, onEachFeature:onEachEntity}).addTo(main_map);
        geo_json_Replicators.setStyle(function(feature) {return feature.properties.style;});
        
    
            /*var layer_control_463e2c303f5641a796469364c8a0a5cf = {
                base_layers : { "openstreetmap" : openstreetmap_layer, },
                overlays : { "macro_element_19c7b17f4e1841ca929eb8534cf3813c" : geo_json_19c7b17f4e1841ca929eb8534cf3813c, }
                };
            L.control.layers(
                layer_control_463e2c303f5641a796469364c8a0a5cf.base_layers,
                layer_control_463e2c303f5641a796469364c8a0a5cf.overlays,
                {position: 'topright',
                 collapsed: true,
                 autoZIndex: true
                }).addTo(main_map);*/
}


function RMStyle(feature,latlng){
    switch (feature.properties["SIA"]){
        case "SustainableFoodProduction":
            var SIA2Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: 'lightgreen',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA2Icon});
        case "Pilgrimage":
            var SIA1Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: '#633d03',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA1Icon});
        case "Migration":
            var SIA3Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: '#a8a8a8',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA3Icon});
        case "ArtAndFestival":
            var SIA4Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: 'yellow',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA4Icon});
        case "Resilience":
            var SIA5Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: 'orange',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA5Icon});
        case "IntegratedLandscapeManagement":
            var SIA6Icon = L.AwesomeMarkers.icon({
                    icon: 'trophy',
                    iconColor: 'green',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA6Icon});               
    }
}
function ReplicatorStyle(feature,latlng){
    switch (feature.properties["SIA"]){
        case "SustainableFoodProduction":
            var SIA2Icon = L.AwesomeMarkers.icon({
                    icon: 'user',
                    iconColor: 'lightgreen',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA2Icon});
        case "Pilgrimage":
            var SIA1Icon = L.AwesomeMarkers.icon({
                    icon: 'user',
                    iconColor: '#633d03',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA1Icon});
        case "Migration":
            var SIA3Icon = L.AwesomeMarkers.icon({
                    icon: 'user',
                    iconColor: '#a8a8a8',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA3Icon});
        case "ArtAndFestival":
            var SIA4Icon = L.AwesomeMarkers.icon({
                    icon: 'user',
                    iconColor: 'yellow',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA4Icon});
        case "Resilience":
            var SIA5Icon = L.AwesomeMarkers.icon({
                    icon: 'user',
                    iconColor: 'orange',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA5Icon});
        case "IntegratedLandscapeManagement":
            var SIA6Icon = L.AwesomeMarkers.icon({
                    icon: 'user',
                    iconColor: 'green',
                    markerColor: 'white',
                    prefix: 'fa',
                    extraClasses: 'fa-rotate-0'
                    });
        return L.marker(latlng, {icon: SIA6Icon});               
    }
}

function mapUpdater(rm_r,sias) {
    // body...
    if (rm_r=='rm') {    
        roleModelsUpdater(sias);
    }
    if (rm_r=='r') {
        replicatorUpdater(sias);
        
    }
    if (rm_r=='all') {
        roleModelsUpdater(sias);
        replicatorUpdater(sias);
    } 
}
function roleModelsUpdater(sias) {
    var data_to_check=roleModelsData;
            var RMToShow={"type": "FeatureCollection", "features":[] }
            for (var i = 0; i <4; i++) {
                for (var c in sias) 
                {
                    sia=sias[c];

                    if (data_to_check.features[i].properties.SIA==sia) {
                        RMToShow.features.push(data_to_check.features[i])
                }
            }
        addRM(RMToShow);
        }
}

function replicatorUpdater(sias) {
    var data_to_check=replicatorData;
    var ReplicatorToShow={"type": "FeatureCollection", "features":[] }
    for (var i  in data_to_check.features) {
        for (var c in sias) 
        {
            sia=sias[c];
            if (data_to_check.features[i].properties.SIA==sia) {
            ReplicatorToShow.features.push(data_to_check.features[i])
            }
        }
    }
    addReplicator(ReplicatorToShow);
}