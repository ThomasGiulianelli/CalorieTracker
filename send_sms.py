from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "***REMOVED***"
# Your Auth Token from twilio.com/console
auth_token  = "***REMOVED***"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18622513908", 
    from_="+18563145301",
    body="Hello from Python!")

print(message.sid)