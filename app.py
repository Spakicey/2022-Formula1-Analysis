from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import pandas as pd
import csv
import numpy as np
# import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/2022_Formula_1_Data"
mongo = PyMongo(app)

@app.route("/")
def index():
   Results = mongo.db.Results.find_one()
   print(Results)
   return render_template("index.html", Results=Results)

if __name__ == "__main__":
   app.run()