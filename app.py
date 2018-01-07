
"""

## Step 4 - Climate App

Now that you have completed your initial analysis, design a Flask api based on the queries that you have just developed.

* Use FLASK to create your routes.

### Routes
/** 

* `/api/v1.0/precipitation`

  * Query for the dates and temperature observations from the last year.

  * Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.

  * Return the json representation of your dictionary.

* `/api/v1.0/stations`

  * Return a json list of stations from the dataset.

* `/api/v1.0/tobs`

  * Return a json list of Temperature Observations (tobs) for the previous year

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

## Hints

* You will need to join the station and measurement tables for some of the analysis queries.

* Use Flask `jsonify` to convert your api data into a valid json response object.

"""

# Create an engine for the `hawaii.sqlite` database
from sqlalchemy import create_engine
engine = create_engine("sqlite:///hawaii.sqlite") # a DataBase file in this case should be in the same dir


# Reflect Database into ORM class
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(engine, reflect=True)
Stations = Base.classes.stations
Measurements = Base.classes.measurements

# Start a session to query the database
from sqlalchemy.orm import Session
session = Session(engine)

# 
tobs=session.query(Measurements.date, Measurements.tobs).filter(Measurements.date > '2016-08-23' ).order_by(Measurements.date).all()
tobs_date = set([i[0] for i in tobs])

tobs_all={}
for i in tobs_date:
    vals=[]
    for j in range(len(tobs)):
        if tobs[j][0] == i:
            temp=tobs[j][1]
            vals.append(temp)
    tobs_all[i]=vals


#list of stations 

stations=session.query(Stations.station, Stations.name).all()
station_list={}
for i in stations:
    key=i[0]
    val=i[1]
    station_list[key]=val


# 
prcp=session.query(Measurements.date, Measurements.prcp).filter(Measurements.date > '2016-08-23' ).order_by(Measurements.date).all()
prcp_date = set([i[0] for i in prcp])

prcp_all={}
for i in prcp_date:
    vals=[]
    for j in range(len(prcp)):
        if prcp[j][0] == i:
            temp=prcp[j][1]
            vals.append(temp)
    prcp_all[i]=vals


####
from flask import Flask, jsonify



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        "Welcome to the Honolulu, Hawaii Climate API!<br/>"
        "<br/>"
        "Available Routes:<br/>"
        "<br/>"
        "Returns jason object (date: temperature) observations from the last year<br/>"
        "/api/v1.0/precipitation<br/>"
        "<br/>"
        "Returns jason object (station list)<br/>"
        "/api/v1.0/stations<br/>"
        "<br/>"
        "Returns jason object (date:precipitation list)<br/>"
        "/api/v1.0/precipitation<br/>"
        
        )




@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tobs data as json"""
    
     
    return jsonify(tobs_all)
    #return jsonify(test)
    

@app.route("/api/v1.0/stations")
def stations():
    """Return the test data as json"""
    
    return jsonify(station_list)


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the test data as json"""
    return jsonify(prcp_all)




if __name__ == "__main__":
    app.run(debug=True)