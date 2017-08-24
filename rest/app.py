#Author: Stephen Weldon
#Github Address:

import datetime
from flask import Flask, jsonify, json, flash, redirect, render_template, request, session, abort, escape
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from functools import wraps
from base64 import b64encode

#Engine used for queries for the sqlite database.
engine = create_engine('sqlite:///users.db', echo=True)
app = Flask(__name__)

#Base / route. Returns user data for the user logged into the session or Hello World to non logged in user.
@app.route("/")
def index():

    # If the user has a valid session token, output the username and all additional JSON data for that user.
    if 'username' in session:
        return "Logged in as %s" % escape(session['username'])

    # If the user does not have a valid session, response with JSON form Hello World.
    else:
        list = [
            {'message': 'Hello World'}
        ]
        return jsonify(results=list)

#POST APImethod for creating a user.
@app.route('/user',methods = ['POST'])
def user():

    if request.method == 'POST':
        json_dict = request.get_json()

        username = (json_dict['username'])

        #Encode the password in base64 so it is not stored in plaintext
        password = b64encode((json_dict['password']))
        email = (json_dict['email'])
        address = (json_dict['address'])
        phone = (json_dict['phone'])


        Session = sessionmaker(bind=engine)
        session = Session()

        #Create the User object and add that user to the database.
        user = User(username, password, email, address, phone)
        session.add(user)

        session.commit()

        return jsonify(json_dict)

#Get Put Delete APIs for selected user to get information, update, or delete the user.
@app.route('/user/<username>',methods = ['GET', 'PUT', 'DELETE'])
def users(username):

    if request.method == 'GET':

        result = engine.execute('Select * FROM users where username = ?', username).first()

        results_array = []

        for _r in result:
            value = _r
            results_array.append(value)

        results_json = {"username": results_array[1], "password": results_array[2], "email": results_array[3], "address": results_array[4], "phone": results_array[5]}

        if result:

            return jsonify(results_json)

        else:
            return "Object not found"

    if request.method == 'PUT':

        json_dict = request.get_json()

        username = (json_dict['username'])
        email = (json_dict['email'])
        address = (json_dict['address'])
        phone = (json_dict['phone'])

        result = engine.execute('UPDATE users set email = ?, address = ?, phone = ? WHERE username = ?', email, address, phone, username)

        return "Put method done"

    if request.method == 'DELETE':

        result = engine.execute('DELETE FROM users where username = ?', username)

        return "Delete Method"

#API to get the session code.
@app.route('/auth', methods=['POST', 'DELETE'])
def auth():
    POST_USERNAME = "python"
    POST_PASSWORD = b64encode("python")

    json_dict = request.get_json()
    username = (json_dict['username'])
    password = (json_dict['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([username]), User.password.in_([b64encode(password)]))
    result = query.first()
    if result:
        return "Object found"
    else:
        return "Object node found"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)