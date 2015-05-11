(function () {



   if(navigator.geolocation){

        navigator.geolocation.watchPosition(getCoords, errorFound);

        //navigator.geolocation.clearWatch(id);

        //navigator.geolocation.getCurrentPosition(getCoords, errorFound);

    } else{

        alert("Actualiza tu navegador");

    }

    function errorFound(error){

        // alert("Ocurrio un error: " + error.code);

        switch(error.code){

            case 0:

                alert("Error deconocido");

                break;

            case 1:

                alert("Permiso denegado");

                break;

            case 2:

                alert("Posicion no esta disponible");

                break;

            case 3:

                alert("Timeout");

                break;

        }

        // 0: Error desconocido

        // 1: Permiso denegado

        // 2: Posicion no esta disponible

        // 3: Timeout

    }

    function getCoords(position){

        var lat = position.coords.latitude;

        var lon = position.coords.longitude;

        console.log("tu posicion es: " + lat + "," + lon);

        var x = document.getElementById("id_latitude").value=lat;

        var y = document.getElementById("id_longitude").value=lon;

        var xlat = document.getElementById('lat').value = lat;

        var ylon = document.getElementById('lon').value = lon;

    }



})();


