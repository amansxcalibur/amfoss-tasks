document.getElementById("searchButton").addEventListener("click", () => {
    const location = document.getElementById("locationInput").value;
    getWeatherData(location);
});

function getWeatherData(location) {
    const apikey = 'd3ba06387f61ba8744bd8111e5303c1a';
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&APPID=${apikey}`;

    fetch(apiUrl)
        .then((response) => response.json())
        .then((jsonData) => {
            const tempCelsius = (jsonData.main.temp - 273.15).toFixed(2);
            const feelsLike = (jsonData.main.feels_like - 273.15).toFixed(2);

            document.getElementById("text_location").innerHTML = jsonData.name;
            document.getElementById("text_location_country").innerHTML = jsonData.sys.country;
            document.getElementById("text_temp").innerHTML = Math.round(tempCelsius);
            document.getElementById("text_feelslike").innerHTML = feelsLike;
            document.getElementById("text_desc").innerHTML = jsonData.weather[0].description;
        })
        .catch((error) => {
            console.error("Error fetching weather data:", error);
        });
}