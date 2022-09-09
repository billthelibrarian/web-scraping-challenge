# Flask app

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():

    some_data = mongo.db.mars.find_one()

    return render_template("index.html", some_data=some_data)

@app.route("/scrape")
def scrape():

    mars = mongo.db.mars

    mars_data = scrape_mars.scrape()

    mars.update_one({}, {"$set": mars_data}, upsert=True)

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
