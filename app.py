from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/2022_Formula_1_Analysis"
mongo = PyMongo(app)

@app.route("/")
def index():
   RaceResults = mongo.db.RaceResults.find_one()
   return render_template("index.html", RaceResults=RaceResults)

if __name__ == "__main__":
   app.run()  