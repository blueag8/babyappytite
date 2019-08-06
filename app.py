import os

from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

#connect to database
app = Flask(__name__)

app.config['MONGO_DBNAME'] ="Baby_Recipes"
app.config["MONGO_URI"] = "mongodb://localhost:27017/Baby_Recipes"


mongo = PyMongo(app)
#home page
@app.route('/')
def index():
    return render_template("index.html")
    
#get recipes

@app.route('/sixmonth_recipes')
def sixmonth_recipes():
    recipes=mongo.db.recipes.find_one_or_404({"category_age":"6 months +"})
    return render_template("sixmonth_recipes.html", recipes=recipes)

@app.route('/sevenmonth_recipes')
def sevenmonth_recipes():
    return render_template("sevenmonth_recipes.html", recipes=mongo.db.recipes.find({"category_age":"7 months +"}))

@app.route('/tenmonth_recipes')
def tenmonth_recipes():
    return render_template("tenmonth_recipes.html", recipes=mongo.db.recipes.find({"category_age":"10 months +"}))
    
@app.route('/twelvemonth_recipes')
def twelvemonth_recipes():
    return render_template("twelvemonth_recipes.html",recipes=mongo.db.recipes.find({"category_age":"12 months +"}))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)