from . import Enums
from .City import City

class CityList:
    def __init__(self, boardCubePool, outbreakCallback):
        #Initialize and store the list of all cities in Pandemic
        self.cities = {
            "San Francisco" : City("San Francisco", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "Chicago" : City("Chicago", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "Montreal" : City("Montreal", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "New York" : City("New York", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "Washington" : City("Washington", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "Atlanta" : City("Atlanta", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "London" : City("London", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "Madrid" : City("Madrid", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "Paris" : City("Paris", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "Essen" : City("Essen", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "Milan" : City("Milan", Enums.Color.Blue, boardCubePool, outbreakCallback),
            "St. Petersburg" : City("St. Petersburg", Enums.Color.Blue, boardCubePool, outbreakCallback),

            "Los Angeles" : City("Los Angeles", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Mexico City" : City("Mexico City", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Miami" : City("Miami", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Bogota" : City("Bogota", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Lima" : City("Lima", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Santiago" : City("Santiago", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Buenos Aires" : City("Buenos Aires", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Sao Paulo" : City("Sao Paulo", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Lagos" : City("Lagos", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Khartoum" : City("Khartoum", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Kinshasa" : City("Kinshasa", Enums.Color.Yellow, boardCubePool, outbreakCallback),
            "Johannesburg" : City("Johannesburg", Enums.Color.Yellow, boardCubePool, outbreakCallback),

            "Algiers" : City("Algiers", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Cairo" : City("Cairo", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Istanbul" : City("Istanbul", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Moscow" : City("Moscow", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Baghdad" : City("Baghdad", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Riyadh" : City("Riyadh", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Tehran" : City("Tehran", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Karachi" : City("Karachi", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Delhi" : City("Delhi", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Mumbai" : City("Mumbai", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Chennai" : City("Chennai", Enums.Color.Black, boardCubePool, outbreakCallback),
            "Kolkata" : City("Kolkata", Enums.Color.Black, boardCubePool, outbreakCallback),

            "Bangkok" : City("Bangkok", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Jakarta" : City("Jakarta", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Ho Chi Minh City" : City("Ho Chi Minh City", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Sydney" : City("Sydney", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Manila" : City("Manila", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Taipei" : City("Taipei", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Hong Kong" : City("Hong Kong", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Shanghai" : City("Shanghai", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Beijing" : City("Beijing", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Seoul" : City("Seoul", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Tokyo" : City("Tokyo", Enums.Color.Red, boardCubePool, outbreakCallback),
            "Osaka" : City("Osaka", Enums.Color.Red, boardCubePool, outbreakCallback)
        }


    def __iter__(self):
        return iter(self.cities)

