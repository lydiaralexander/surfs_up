
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database into our classes
Base = automap_base()

#reflect the database
Base.prepare(engine, reflect=True)

#save references to each table. create a variable for each of the classes
#so that we can reference them later.
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database
session = Session(engine)

#define our Flask app. this will create a Flask Application call "app"
app = Flask(__name__)

#define the welcome route
@app.route("/")

#Now our root, or welcome route, is set up. The next step is to add the routing 
# information for each of the other routes. For this we'll create a function, 
# and our return statement will have f-strings as a reference to all of the 
# other routes. This will ensure our investors know where to go to view the 
# results of our data.

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


@app.route("/api/v1.0/precipitation")


def precipitation():
    #add the line of code that calculates the date one year ago from the recent date in the database
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   #write a query to get the date and precipitation for the previous year
   precipitation = session.query(Measurement.date, Measurement.prcp).\
       filter(Measurement.date >= prev_year).all()
   return jsonify(precip)

#create a dictionary with the date as the key and the precipitation as the value.
#To do this, we will "jsonify" our dictionary. A function that converts the dictionary to a JSON file.


