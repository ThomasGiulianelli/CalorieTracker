# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Get message sent by the user
    body = request.values.get('Body', None)
    
    # Start our response
    resp = MessagingResponse()

    # Ensure correct input (digits only)
    if body.isdigit():
        # Determine amount of calories left in their diet for the day
        consumedCalories = int(body)   
        caloriesRemaining = 2000 - consumedCalories
        resp.message("You have {} Calories remaining for the day (2000 Calorie diet).".format(caloriesRemaining))
    else:
        resp.message("Please send Calorie intake only.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
