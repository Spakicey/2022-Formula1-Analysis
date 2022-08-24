# Add dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import cleaning

# Init flask app
app = Flask(__name__)

# Use flask pymongo to set up mongo connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/f1_app'
mongo = PyMongo(app)

# App routes
@app.route('/')
def index():
  f1 = mongo.db.f1.find_one()
  return render_template('index.html', f1=f1)

@app.route('/scrape')
def scrapeAndClean():
  f1 = mongo.db.f1
  f1_data = cleaning.cleanAll()
  # f1.update_one({}, {'$set':f1_data_json}, upsert=True)
  # f1.insert_many(f1_data.to_dict('records'))
  f1.update_one({}, {"$set":{'race':f1_data.to_html()}}, upsert=True)

  return redirect('/', code=302)
   
if __name__ == "__main__":
   app.run()

