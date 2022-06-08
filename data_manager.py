import requests
import os

sheety_endpoint = "https://api.sheety.co/2c408ce9f0ac3e6917e66cfd5863a5b8/flightDeals/prices"
TOKEN = os.environ.get('SHEETY_TOKEN')

class DataManager:
    def __init__(self):
        self.cities_data = {}
        self.header = {
            'Authorization': TOKEN
        }

    def get_cities(self):

        response = requests.get(url=sheety_endpoint, headers=self.header)
        self.cities_data = response.json()['prices']
        return self.cities_data

    def update_iata_code(self, iata_code, city_info):\

        body = {
            'price': {
                'city': city_info['city'],
                'iataCode': iata_code,
                'lowestPrice': city_info['lowestPrice']
            }
        }
        response = requests.put(url=f"{sheety_endpoint}/{city_info['id']}", json=body, headers=self.header)



