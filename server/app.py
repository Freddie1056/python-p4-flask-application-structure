#!/usr/bin/env python3

from flask import Flask  # Import the Flask class

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/')  # Define the route for the homepage
def index():  # Function that runs when accessing the homepage
    return '<h1>Welcome to my page!</h1>'  # Return a simple message

@app.route('/<string:username>')  # Define a route that takes a username
def user(username):  # Function that runs when accessing a user profile
    return f'<h1>Profile for {username}</h1>'  # Return the user's profile

if __name__ == '__main__':  # Check if this file is being run directly
    app.run(port=5555, debug=True)  # Run the application on port 5555
