import pyshorteners

type_tiny = pyshorteners.Shortener()


class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, link, stopover=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stopover = stopover
        self.via_city = via_city
        self.link = type_tiny.tinyurl.short(link)

