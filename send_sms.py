import os
from twilio.rest import Client
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

#.env file contains sensitive info
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(find_dotenv())

# Your Account SID from twilio.com/console
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
# Your Auth Token from twilio.com/console
auth_token  = os.environ.get("TWILIO_ACCOUNT_AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18622513908", 
    from_="+18563145301",
    body="Hello from Python!")

print(message.sid)
