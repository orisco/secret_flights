import requests
import os

sheety_endpoint = "https://api.sheety.co/f8d036e704942b782c89cb2cb308a7ac/flightDeals/prices"
sheety_users_endpoint = "https://api.sheety.co/f8d036e704942b782c89cb2cb308a7ac/flightDeals/users"
TOKEN = os.environ.get('SHEETY_TOKEN')

class DataManager:
    def __init__(self):
        self.cities_data = {}
        self.header = {
            'Authorization': TOKEN
        }
        self.user_data = {}

    def get_cities(self):
        response = requests.get(url=sheety_endpoint, headers=self.header)
        self.cities_data = response.json()['prices']
        return self.cities_data

    def update_iata_code(self, iata_code, city_info):
        body = {
            'price': {
                'city': city_info['city'],
                'iataCode': iata_code,
                'lowestPrice': city_info['lowestPrice']
            }
        }
        response = requests.put(url=f"{sheety_endpoint}/{city_info['id']}", json=body, headers=self.header)

    def get_users(self):
        response = requests.get(url=sheety_users_endpoint, headers=self.header)
        self.user_data = (response.json()['users'])
        return self.user_data





