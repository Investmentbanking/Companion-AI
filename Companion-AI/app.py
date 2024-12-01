# imports the main Flask class to create web application
# request object gives access to data sent by the user like form inputs/JSON data
# jsonify send data back to user in JSON format
from flask import Flask, request, jsonify

# CORS ensures frontend can communicate with backend without browser restrictions
from flask_cors import CORS

# Takes name of current module as argument
# Creates an instance of flask app
# __name__ argument tells flask to use current file/module as app
# allowing it to find resources like templates & static files
app = Flask(__name__)

# ensures flaks app allows requests from different origins
CORS(app)

# defines route for web application
# route maps URL (/) to specific function
# when user visits https://localhost:5000/ function below decorator will execute
@app.route('/')
def hello_world():
    return "Hello World"

# ensures app runs only when file executed directly
if __name__ == '__main__':
    # starts flask development server
    app.run()



