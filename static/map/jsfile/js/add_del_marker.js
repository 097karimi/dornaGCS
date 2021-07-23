var map = L.map('map').setView([35.6892, 51.3890], 14);
        mapLink = 
            '<a href="http://www.esri.com/">Esri</a>';
        wholink = 
            'i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community';
        L.tileLayer(
            'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
            attribution: '&copy; '+mapLink+', '+wholink,
            maxZoom: 18,
            }).addTo(map);
        
        //add a marker
        //L.marker([35.6892, 51.3890]).addTo(map);

        //add a marker on the map by click
        {% comment %} map.on('click', function(e) {
            L.marker(e.latlng).addTo(map)
        } ); {% endcomment %}
        {% comment %} map.on('click', function(e) {
            L.removeLayer()
        } ); {% endcomment %}
        
        //add a marker on the map by click
        {% comment %} var marker;
        map.on('click', function(e) {
             marker = new L.Marker(e.latlng, {draggable:true});
        map.addLayer(marker);
        marker.bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();
        } );

        var marker;
        map.on('contextmenu', function(e) {
            map.removeLayer(marker)
        } ); {% endcomment %}

        // attaching function on map click
        map.on('click', onMapClick);

        // Script for adding marker on map click
        function onMapClick(e) {

            var geojsonFeature = {
                "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "Point",
                        "coordinates": [e.latlng.lat, e.latlng.lng]
                }
            }

            var marker;

            L.geoJson(geojsonFeature, {
                
                pointToLayer: function(feature, latlng){
                    
                    marker = L.marker(e.latlng, {
                        
                        title: "Resource Location",
                        alt: "Resource Location",
                        riseOnHover: true,
                        draggable: true,

                    }).bindPopup("<p> lat : " + (e.latlng.lat) + "<br>lng : " + (e.latlng.lng) + "</p><input type='button' value='Delete this marker' class='marker-delete-button'/>");

                    marker.on("popupopen", onPopupOpen);
            
                    return marker;
                }
            }).addTo(map);
        }


        // Function to handle delete as well as other events on marker popup open
        function onPopupOpen() {

            var tempMarker = this;

            //var tempMarkerGeoJSON = this.toGeoJSON();

            //var lID = tempMarker._leaflet_id; // Getting Leaflet ID of this marker

            // To remove marker on click of delete
            $(".marker-delete-button:visible").click(function () {
                map.removeLayer(tempMarker);
            });
        }


        {% comment %} 
        var map = L.map('map').setView([-41.2858, 174.78682], 14);
        mapLink = 
            '<a href="http://openstreetmap.org">OpenStreetMap</a>';
        L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; ' + mapLink + ' Contributors',
            maxZoom: 18,
            }).addTo(map);
            {% endcomment %}