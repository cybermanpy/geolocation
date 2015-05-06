(function () {



	if(navigator.geolocation){

		navigator.geolocation.getCurrentPosition(getCoords, errorFound);

	} else{

		alert("Actualiza tu navegador");

	}



	function errorFound(error){

		alert("Ocurrio un error: " + error.code);

		// 0: Error desconocido

		// 1: Permiso denegado

		// 2: Posicion no esta disponible

		// 3: Timeout

	}

	function getCoords(position){

		var lat = position.coords.latitude;

		var lon = position.coords.longitude;

		console.log("tu posicion es: " + lat + "," + lon);

		var x = document.getElementById("latitude");

		var y = document.getElementById("longitude");

		x.value = lat;

		y.value = lon

	}



})();
