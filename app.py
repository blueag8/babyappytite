import pymongo
import os


from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

#connect to database
app = Flask(__name__)

app.config['MONGO_DBNAME'] ="Baby_Recipes"
app.config["MONGO_URI"] ="mongodb+srv://blueag8:mongo8@cluster0-iodau.mongodb.net/Baby_Recipes?retryWrites=true&w=majority"

mongo = PyMongo(app)


#home page



@app.route('/')
def home():
    return render_template("index.html")
    
#get recipes
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    return render_template("recipe.html", recipes=mongo.db.recipes.find({"_id": ObjectId(recipe_id)}))

@app.route('/sixmonth_recipes')
def sixmonth_recipes():
   return render_template("sixmonth_recipes.html", recipes=mongo.db.recipes.find({"category_age":"6 months +"}))

@app.route('/sevenmonth_recipes')
def sevenmonth_recipes():
    return render_template("sevenmonth_recipes.html", recipes=mongo.db.recipes.find({"category_age":"7 months +"}))

@app.route('/tenmonth_recipes')
def tenmonth_recipes():
    return render_template("tenmonth_recipes.html", recipes=mongo.db.recipes.find({"category_age":"10 months +"}))
    
@app.route('/twelvemonth_recipes')
def twelvemonth_recipes():
    return render_template("twelvemonth_recipes.html",recipes=mongo.db.recipes.find({"category_age":"12 months +"}))

#add recipe 

@app.route('/addrecipe')
def addrecipe():
    return render_template("addrecipe.html", categories=mongo.db.categories.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    mongo.db.recipes.insert_one(request.form.to_dict())
    return redirect(url_for('/addrecipe'))

    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)