from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/formula_one_analysis"
mongo = PyMongo(app)

@app.route("/")
def index():
   formula1 = mongo.db.formula.find_one()
   return render_template("index.html", formula1=formula1)

@app.route("/")
def scrape():
   formula1 = mongo.db.formula1
   formula1_data = scraping.scrape_all()
   formula1.update_one({}, {"$set":formula1_data}, upsert=True)
   return redirect('/', code=302)

.update_one(query_parameter, {"$set": data}, options)

if __name__ == "__main__":
   app.run()