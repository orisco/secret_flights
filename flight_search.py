import requests
import os
import datetime
from dateutil.relativedelta import relativedelta
from flight_data import FlightData

API_KEY = os.environ.get("KIWI_API_KEY")
kiwi_endpoint = "https://tequila-api.kiwi.com"
flying_from = "TLV"

date = datetime.datetime.today() + relativedelta(days=+1)
current_date_formatted = date.strftime('%d/%m/%Y')
six_months = date + relativedelta(months=+6)
six_month_formatted = six_months.strftime('%d/%m/%Y')


class FlightSearch:
    def __init__(self):
        self.iata_code = ""

    def get_iata_code(self, city_name):
        header = {
            'content-type': 'application/json',
            'apikey': API_KEY,
        }
        params = {
            'term': city_name
        }
        response = requests.get(url=f"{kiwi_endpoint}/locations/query", params=params, headers=header)
        self.iata_code = response.json()['locations'][0]['code']
        return self.iata_code


    def search_for_flights(self, city):
        header = {
            'content-type': 'application/json',
            "apikey": API_KEY
        }
        params = {
            'fly_from': flying_from,
            'fly_to': city['iataCode'],
            'date_from': current_date_formatted,
            'date_to': six_month_formatted,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'curr': 'USD',
            'price_to': city['lowestPrice'],
            'max_stopovers': 0,

        }
        response = requests.get(url=f"{kiwi_endpoint}/v2/search", headers=header, params=params)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {city['iataCode']}.")
            return None

        flight_data = FlightData(price=data['price'], origin_city=data['cityFrom'], origin_airport=data['flyFrom'],
                                 destination_city=data['cityTo'], destination_airport=data['cityCodeTo'],
                                 out_date=data['route'][0]['local_departure'].split("T")[0],
                                 return_date=data['route'][1]['local_departure'].split("T")[0], link=data['deep_link'])
        return flight_data
