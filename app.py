from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

from flask_restful import Api, Resource, reqparse
from sqlalchemy.orm import sessionmaker
from tabledef import *
import sys

# engine = create_engine('sqlite:///tutorial.db', echo=True)

variablaae = 5
app = Flask(__name__)
api = Api(app)
# app.secret_key = os.urandom(12)


users = [{"name": "Nicholas", "age": 42, "occupation": "Network Engineer"}]


class User(Resource):

    def get(self, name):
        for user in users:
            if name == user["username"]:
                return user, 200
        return "user not found 404"

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        parser.add_argument("username")
        args = parser.parse_args()

        for user in users:
            if name == user["username"]:
                return "user with name {} already exists".format(name), 400

        user = {
            "username": name,
            "email": args["email"],
            "name": args["name"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("email")
        parser.add_argument("username")
        args = parser.parse_args()

        for user in users:
            if name == user["username"]:
                if name == user["username"]:
                    user["email"] = args["email"]
                    user["name"] = args["name"]
                    return user, 200

        user = {
            "username": name,
            "email": args["email"],
            "name": args["name"]
        }
        users.append(user)
        return user, 200

    def delete(self, name):
        global users
        users = [user for user in users if user["username"] != name]
        return "{} is delete.".format(name), 200


api.add_resource(User, "/user/<string:name>")


@app.route('/')
def home(origin=""):
    print(variablaae)
    if session.get('logged_in') and origin == "logout":
        return "Hello "  + "!  <a href='/logout'>Logout</a>"
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    variablaae = 5
    # POST_USERNAME = str(request.form['username'])
    # POST_PASSWORD = str(request.form['password'])
    #
    # Session = sessionmaker(bind=engine)
    # s = Session()
    # query2 = s.query(User)
    # s.add(User("lala", "lala", "kaska"))
    # s.commit()
    # query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    # result = query.first()
    result = 0
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home("logout")


@app.route("/logout")
def logout():
    # if not session['logged_in']:
    #     return home()
    variablaae = 5
    session['logged_in'] = False
    return home("logout")


if __name__ == "__main__":

    # importing required libraries
    from datetime import time
    import requests
    import numpy
    import json
    import googlemaps
    import datetime
    import time
    from dateutil import tz
    import sys
    from sklearn.neighbors import KNeighborsRegressor

    # enter your api key here
    api_key = 'AIzaSyCNBl9RA3jmY5dc3A7n4tksBXrMl4LjLFc'

    # Take source as input
    source = 'Boston'  # sys.argv[1]

    # Take destination as input
    dest = 'nyc'  # sys.argv[2]

    # url variable store url
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    # Get method of requests module
    # return response object

    r = requests.get(url + 'origins=' + source +
                     '&destinations=' + dest +
                     '&key=' + api_key)

    # json method of response object
    # return json format result
    x = r.json()

    # Requires API key
    gmaps = googlemaps.Client(api_key)

    # Requires cities name
    my_dist = gmaps.distance_matrix(source, dest)['rows'][0]['elements'][0]["duration"]["value"]


    def requestTime(origin, destination, arrival_time, departure_time=-1, mode='driving',
                    api_key='AIzaSyCNBl9RA3jmY5dc3A7n4tksBXrMl4LjLFc'):
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        requestUrl = url + 'origins=' + origin + '&destinations=' + destination + '&mode=' + mode + '&key=' + api_key
        # print(arrival_time)
        # print(departure_time)
        if arrival_time > 0:
            # print('arrival bigger')
            requestUrl += '&arrival_time=' + str(arrival_time)
        elif departure_time > 0:
            # print('depart bigger')
            requestUrl += '&departure_time=' + str(departure_time)
        else:
            pass
        # print(requestUrl)

        r = requests.get(requestUrl)
        x = r.json()
        return x


    def smoothFit(x, y, n_neighbors=2):
        x = numpy.array(x)
        neigh = KNeighborsRegressor(n_neighbors=n_neighbors)
        neigh.fit(x.reshape(-1, 1), y)
        prediction = neigh.predict(x.reshape(-1, 1))
        neigh.fit(x.reshape(-1, 1), prediction)
        predictionPrediction = neigh.predict(x.reshape(-1, 1))
        return x, predictionPrediction


    origin = 'boston'  # sys.argv[1]
    destination = 'nyc'  # sys.argv[2]
    arrival_time = '13:30:00'  # sys.argv[3]
    ftr = [3600, 60, 1]
    arrival_time = sum([a * b for a, b in zip(ftr, map(int, arrival_time.split(':')))])

    current_time = datetime.datetime.now().time()
    current_time = int(current_time.hour) * 3600 + int(current_time.minute) * 60 + int(current_time.second)

    Time_interval = arrival_time - current_time - my_dist

    if Time_interval < 0:
        arrival_time = current_time + my_dist + 60
        Time_interval = arrival_time - current_time - my_dist
        # "You cannot get there that fast"

    results = []
    y = []
    x = []

    for i in range(0, Time_interval, 600):
        results.append(requestTime(origin, destination, arrival_time, current_time + i * 600))

    for i in results:
        y.append(i['rows'][0]['elements'][0]["duration"]["value"])

    for i in range(len(y)):
        x.append(arrival_time - y[i])
    print("lala")
    smoothFit(x, y)
    sys.stdout.flush()

    app.run(debug=True, host='0.0.0.0', port=4000)
