from . import Enums
from .City import City

class CityList:
    def __init__(self, boardCubePool):
        #Initialize and store the list of all cities in Pandemic
        self.cities = {
            "San Francisco" : City("San Francisco", Enums.Color.Blue, boardCubePool),
            "Chicago" : City("Chicago", Enums.Color.Blue, boardCubePool),
            "Montreal" : City("Montreal", Enums.Color.Blue, boardCubePool),
            "New York" : City("New York", Enums.Color.Blue, boardCubePool),
            "Washington" : City("Washington", Enums.Color.Blue, boardCubePool),
            "Atlanta" : City("Atlanta", Enums.Color.Blue, boardCubePool),
            "London" : City("London", Enums.Color.Blue, boardCubePool),
            "Madrid" : City("Madrid", Enums.Color.Blue, boardCubePool),
            "Paris" : City("Paris", Enums.Color.Blue, boardCubePool),
            "Essen" : City("Essen", Enums.Color.Blue, boardCubePool),
            "Milan" : City("Milan", Enums.Color.Blue, boardCubePool),
            "St. Petersburg" : City("St. Petersburg", Enums.Color.Blue, boardCubePool),

            "Los Angeles" : City("Los Angeles", Enums.Color.Yellow, boardCubePool),
            "Mexico City" : City("Mexico City", Enums.Color.Yellow, boardCubePool),
            "Miami" : City("Miami", Enums.Color.Yellow, boardCubePool),
            "Bogota" : City("Bogota", Enums.Color.Yellow, boardCubePool),
            "Lima" : City("Lima", Enums.Color.Yellow, boardCubePool),
            "Santiago" : City("Santiago", Enums.Color.Yellow, boardCubePool),
            "Buenos Aires" : City("Buenos Aires", Enums.Color.Yellow, boardCubePool),
            "Sao Paulo" : City("Sao Paulo", Enums.Color.Yellow, boardCubePool),
            "Lagos" : City("Lagos", Enums.Color.Yellow, boardCubePool),
            "Khartoum" : City("Khartoum", Enums.Color.Yellow, boardCubePool),
            "Kinshasa" : City("Kinshasa", Enums.Color.Yellow, boardCubePool),
            "Johannesburg" : City("Johannesburg", Enums.Color.Yellow, boardCubePool),

            "Algiers" : City("Algiers", Enums.Color.Black, boardCubePool),
            "Cairo" : City("Cairo", Enums.Color.Black, boardCubePool),
            "Istanbul" : City("Istanbul", Enums.Color.Black, boardCubePool),
            "Moscow" : City("Moscow", Enums.Color.Black, boardCubePool),
            "Baghdad" : City("Baghdad", Enums.Color.Black, boardCubePool),
            "Riyadh" : City("Riyadh", Enums.Color.Black, boardCubePool),
            "Tehran" : City("Tehran", Enums.Color.Black, boardCubePool),
            "Karachi" : City("Karachi", Enums.Color.Black, boardCubePool),
            "Delhi" : City("Delhi", Enums.Color.Black, boardCubePool),
            "Mumbai" : City("Mumbai", Enums.Color.Black, boardCubePool),
            "Chennai" : City("Chennai", Enums.Color.Black, boardCubePool),
            "Kolkata" : City("Kolkata", Enums.Color.Black, boardCubePool),

            "Bangkok" : City("Bangkok", Enums.Color.Red, boardCubePool),
            "Jakarta" : City("Jakarta", Enums.Color.Red, boardCubePool),
            "Ho Chi Minh City" : City("Ho Chi Minh City", Enums.Color.Red, boardCubePool),
            "Sydney" : City("Sydney", Enums.Color.Red, boardCubePool),
            "Manila" : City("Manila", Enums.Color.Red, boardCubePool),
            "Taipei" : City("Taipei", Enums.Color.Red, boardCubePool),
            "Hong Kong" : City("Hong Kong", Enums.Color.Red, boardCubePool),
            "Shanghai" : City("Shanghai", Enums.Color.Red, boardCubePool),
            "Beijing" : City("Beijing", Enums.Color.Red, boardCubePool),
            "Seoul" : City("Seoul", Enums.Color.Red, boardCubePool),
            "Tokyo" : City("Tokyo", Enums.Color.Red, boardCubePool),
            "Osaka" : City("Osaka", Enums.Color.Red, boardCubePool)
        }


    def __iter__(self):
        return iter(self.cities)

    def __getitem__(self, key):
        return self.cities[key]

