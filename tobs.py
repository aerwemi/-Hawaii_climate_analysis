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

print(tobs_all)