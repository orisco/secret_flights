from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_cities()

for city in sheet_data:
    if city['iataCode'] == "":
        iata_code = flight_search.get_iata_code(city['city'])
        data_manager.update_iata_code(iata_code, city)
    else:
        flight = flight_search.search_for_flights(city)

    if flight:
        users = data_manager.get_users()
        for user in users:
            notification_manager = NotificationManager(flight, user['email'])
            notification_manager.send_email()

