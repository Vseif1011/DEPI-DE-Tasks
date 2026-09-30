# 🌤️ Weather Data ETL Pipeline

## 🎯 Objective

Build an **ETL pipeline using Python** to collect weather data for cities in Egypt from the OpenWeatherMap API, transform the data, and load it into **SQL Server**.

## 🛠️ Technologies

* Python
* Requests
* OpenWeatherMap API
* SQL Server
* PyODBC

## 📍 Cities

Use these 10 cities:

```python
cities = [
    "Cairo",
    "Giza",
    "Alexandria",
    "Port Said",
    "Suez",
    "Ismailia",
    "Mansoura",
    "Tanta",
    "Luxor",
    "Aswan"
]
```

## 🔄 ETL Requirements

### 1. Extract

* Call the OpenWeatherMap Current Weather API for each city.
* Store the required weather fields.
* You can use this API endpoint: `https://api.openweathermap.org/data/2.5/weather`

* You can use your API key.

😔 Since the Weather App is currently not working, we couldn't find the documentation. You can try using the syntax below. Your task is simply to retrieve the weather data for **all cities**.

```python
url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "appid": "YOUR_API_KEY",
    "q": "Cairo"
}

response = requests.get(url, params=params)

data = response.json()
```

### 2. Transform

Clean and transform the API data:

* Standardize city names.
* Handle missing values if found.
* Convert numeric fields to the correct data types.
* Store all temperatures in **Celsius (°C)**.
* Create a **`Region`** column:

  * Greater Cairo
  * North Coast
  * Lower Egypt
  * Upper Egypt
  * Canal
  * Sinai
  * Red Sea
* Create a **`TemperatureCategory`** column:

  * Cold
  * Moderate
  * Hot
* Create a **`HumidityCategory`** column:

  * Low
  * Medium
  * High
* Create an **`IngestionTime`** column to record when the ETL pipeline ingested the data.
* Validate the final data.

### 3. Load
Connect to Azure SQL Server using PyODBC.
* Server Name: depi213.database.windows.net
* Username: sqladmin
* Password: Depi123#
Create a table with your name:

```text
Mohamed_Hamed_WeatherData
```

Load the transformed data into SQL Server using **PyODBC**.

## 📊 Required Columns

```text
ID (Create an auto-incrementing ID using IDENTITY)
City
Country
Latitude
Longitude
Temperature
Pressure
Humidity
WindSpeed
WeatherMain
WeatherDescription
Region
TemperatureCategory
HumidityCategory
IngestionTime
```

## 🔄 Final Flow

```text
OpenWeatherMap API
        ↓
     Extract
        ↓
    Transform
   ├── Clean Data
   ├── Celsius °C
   ├── Region
   ├── Temperature Category
   ├── Humidity Category
   └── Ingestion Time
        ↓
      Load
        ↓
    SQL Server
```
