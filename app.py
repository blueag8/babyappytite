import pymongo
import os


from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo

#connect to database
app = Flask(__name__)


#set app variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI","monogodb://localhost")
app.config["SECRET_KEY"]= 'yum'

#app.config["IMAGE_UPLOADS"] ="/home/ubuntu/environment/static/image/uploads"

mongo = PyMongo(app)


#home page



@app.route('/')
def home():
    return render_template("index.html", categories=mongo.db.categories.find())
    
@app.route('/get_recipes')
def get_recipes():
   
    #TEST
    category_age=request.form.get("category_age")
  
    
    print()
    
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"category_age":category_age}))

    

#single recipe

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
      return render_template("recipes.html", recipes=mongo.db.recipes.find({"_id": ObjectId(recipe_id)}))
#TEST1
    
#recipes categorized per page route

#@app.route('/recipes')
#def recipes():
   # recipes=mongo.db.recipes.find()
    #TEST
    #for recipe in recipes:
      #  print(recipe)
        
   # return render_template("recipes.html")
   
   
#sort recipes by age group 

@app.route('/sixmonth_recipes')
def sixmonth_recipes():
   return render_template("recipes.html", recipes=mongo.db.recipes.find({"category_age":"6 months +"}))

@app.route('/sevenmonth_recipes')
def sevenmonth_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"category_age":"7 months +"}))

@app.route('/tenmonth_recipes')
def tenmonth_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"category_age":"10 months +"}))
    
@app.route('/twelvemonth_recipes')
def twelvemonth_recipes():
    return render_template("recipes.html",recipes=mongo.db.recipes.find({"category_age":"12 months +"}))

#add recipe 

@app.route('/addrecipe')
def addrecipe():
    
    return render_template("addrecipe.html", categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
   # if 'image' in request.files:
        #filename = images.save(request.files['image'])
        #filepath = '../static/images/' + filename
    recipes=mongo.db.recipes


    recipe_name=request.form["recipe_name"]
    category_age=request.form.get("category_age")
    cooking_time=int(request.form["cooking_time"])
    portion_size=int(request.form["portion_size"]) 
    allergens=request.form.getlist("allergen")
    ingredients=request.form.getlist("ingredient")
    recipe_description=request.form["recipe_description"]
    steps=request.form.getlist("step")
      
    form={
    
        "recipe_name":recipe_name,
        "category_age":category_age,
        "cooking_time":cooking_time,
        "portion_size":portion_size,
        "allergen": allergens,
        "ingredient": ingredients,
        "recipe_description":recipe_description,
        "step": steps,
           
          }
          
        #"image": filepath
      
    recipes.insert_one(form)
    return redirect(url_for('recipes'))

@app.route('/editrecipe/<recipe_id>')
def editrecipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    categories=mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=recipe, categories=categories)
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):

     
    #if request.method == "POST":
      # if request.files:
                     

    recipes=mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
  
    {
            'recipe_name':request.form.get("recipe_name"),
            'category_age':request.form.get("category_age"),
            'cooking_time':int(request.form["cooking_time"]),
            'portion_size':int(request.form["portion_size"]),
            'allergens':request.form.getlist('check'),
            'ingredients':request.form.getlist("ingredient"),
            'recipe_description':request.form.get("recipe_description"),
            'steps':request.form.getlist("step"),
            #'image':request.files["image"]
      })
     
        
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        { '$inc': { 'stars': 1}}
    )    
          
  
    return redirect(url_for('recipes', recipe_id=recipe_id))
    
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes', recipe_id=recipe_id))

# routing for likes
#referred to another student's code for likes.

@app.route('/stars/<recipe_id>', methods=["GET", "POST"])
def stars(recipe_id):
    
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        { '$inc': { 'stars': 1}}
    )
    
    return redirect(url_for('recipe',recipe_id=recipe_id))
 
#@app.route("/upload-image", methods=["GET", "POST"])
#def upload_image():

  #  if request.method == "POST":

      #  if request.files:

          #  image = request.files["image"]

          # image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))


          # return redirect(request.url)   


    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)