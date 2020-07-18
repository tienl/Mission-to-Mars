from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrapingchallenge

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scrapingchallenge.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

@app.route("/cerb")
def cerb():
   mars = mongo.db.mars.find_one()
   return render_template("cerb.html", mars=mars)

@app.route("/schi")
def schi():
   mars = mongo.db.mars.find_one()
   return render_template("schi.html", mars=mars)

@app.route("/syrt")
def syrt():
    mars = mongo.db.mars.find_one()
    return render_template("syrt.html", mars=mars)

@app.route("/vall")
def vall():
   mars = mongo.db.mars.find_one()
   return render_template("vall.html", mars=mars)



if __name__ == "__main__":
   app.run()
