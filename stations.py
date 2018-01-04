# Create an engine for the `hawaii.sqlite` database
from sqlalchemy import create_engine
engine = create_engine("sqlite:///hawaii.sqlite") # a DataBase file in this case should be in the same dir


# Reflect Database into ORM class
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(engine, reflect=True)
Stations = Base.classes.stations

# Start a session to query the database
from sqlalchemy.orm import Session
session = Session(engine)

# 
#from sqlalchemy import func
stations=session.query(Stations.station, Stations.name).all()

station_list={}
for i in stations:
    key=i[0]
    val=i[1]
    station_list[key]=val

print(station_list)
