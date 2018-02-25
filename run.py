# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

#dictionary to store unique phone numbers and their calorie consumption
users = {}

@app.route("/sms", methods=['GET', 'POST'])
def calorie_reply():
    """Respond to incoming messages with calorie information SMS."""
    # Get message sent by the user
    body = request.values.get('Body', None)
    # Get user's phone number
    user = request.values.get('From', None)
    
    # Start our response
    resp = MessagingResponse()

    # Ensure correct input (digits only)
    if body.isdigit():
        # Determine amount of calories left in their diet for the day
        consumedCalories = int(body) 
        
        #if user is already known, add onto their calorie total
        if user in users:
            users[user] = users[user] + consumedCalories
        else:
            #add user and their calorie consumption to the dictionary
            users[user] = consumedCalories
          
        caloriesRemaining = 2000 - users[user]
        if caloriesRemaining > 0:
            resp.message("You have {} Calories remaining for the day (2000 Calorie diet).".format(caloriesRemaining))
        else:
            resp.message("You have exceeded the recommended calorie intake for today by {} calories.".format(abs(caloriesRemaining)))
    else:
        resp.message("Please send Calorie intake only.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
