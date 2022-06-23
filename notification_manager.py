import os
from twilio.rest import Client
import smtplib

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH')
my_email = "orisco@yahoo.com"
my_password = "dqidzojqghrrpgwv"


class NotificationManager:
    def __init__(self, flight, email):
        self.client = Client(account_sid, auth_token)
        self.message = f"Low Price Alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport} from {flight.out_date} to {flight.return_date}. Link: {flight.link}"
        self.email = email

    def send_email(self):
        with smtplib.SMTP("smtp.mail.yahoo.com", port=465) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=self.email,
                                msg=f"Low Price Alert\n\n{self.message}")


    # def send_notification(self):
    #     message = self.client.messages.create(
    #         body=self.message,
    #         from_='+17473022311',
    #         to='+13109337464'
    #     )
    #     print(message.sid)
