import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH')


class NotificationManager:
    def __init__(self, flight):
        self.client = Client(account_sid, auth_token)
        self.message = f"Low Price Alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport} from {flight.out_date} to {flight.return_date}. Link: {flight.link}"

    def send_notification(self):
        message = self.client.messages.create(
            body=self.message,
            from_='+17473022311',
            to='+13109337464'
        )
        print(message.sid)
