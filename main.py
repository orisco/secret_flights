from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_cities()

for city in sheet_data:
    flight_search = FlightSearch()
    if city['iataCode'] == "":
        iata_code = flight_search.get_iata_code(city['city'])
        data_manager.update_iata_code(iata_code, city)
    flight = flight_search.search_for_flights(city)

    if flight:
        notification_manager = NotificationManager(flight)
        notification_manager.send_notification()

