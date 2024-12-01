# imports the main Flask class to create web application
# request object gives access to data sent by the user like form inputs/JSON data
# jsonify send data back to user in JSON format
from flask import Flask, request, jsonify

# CORS ensures frontend can communicate with backend without browser restrictions
from flask_cors import CORS

import json


# Takes name of current module as argument
# Creates an instance of flask app
# __name__ argument tells flask to use current file/module as app
# allowing it to find resources like templates & static files
app = Flask(__name__)

# ensures flaks app allows requests from different origins
CORS(app)

# personalities dictionary loaded when server starts
# converts JSON file into python dictionary
with open('personalities.json') as f:
    personalities = json.load(f)

# defines route for web application
# route maps URL (/) to specific function
# when user visits https://localhost:5000/ function below decorator will execute
@app.route('/')
def hello_world():
    return "Hello World"

# defines new endopint and specifies it accepts POST requests
# used by frontend to send user messages to backend
@app.route('/chat', methods=['POST'])
def chat():
    # captures JSON data sent by frontend
    data = request.get_json()

    # retrieves user_input key from JSON data which represents what user typed
    user_input = data.get('user_input', '')

    # personality = data.get('personality', '')

    if user_input.lower() == 'hi':
        response = f"Hi, how are you doing today?"
    else:
        response = f"You said: {user_input}"
    # chatbot echoes back what user said
    # response = f"You said: {user_input}"

    # converts chatbots response into JSON format
    # frontend can easily process & display
    # converts python data into JSON
    return jsonify({"response": response})


# ensures app runs only when file executed directly
if __name__ == '__main__':
    # starts flask development server
    app.run()



