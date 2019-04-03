import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

list_prcp = []

@app.route("/")
def homepage():
    print("We received your for homepage request")
    return (
        f"Welcome/Bienvenido/Bonjour!<br/>"
        f"Routes Available :<br/>"
        f"/api/v1.0/precp<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/temps<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precp():
    print("Server received your request for precipitation results")
    prcp_results = session.query(Measurement.prcp).all()
    prcp_list = []
    for x in results:
        prcp_list.append(x)
    date_list = []
    date_results = session.query(Measurement.date).all()
    date_list = []
    for y in date_results:
        date_list.append(y)

    dictionary = dict(zip(date_list, prcp_list))
    return jsonify(dictionary)

@app.route("/api/v1.0/stations")
def station():
    print("We received your for homepage request for stations homepage")
    station_results = session.query(Measurement.station).all()

    stations_list = []
    for z in station_results:
        station_dict = {}
        station_dict["Stations"] = station_results
        stations_list.append(z)

    return jsonify(station_dict)