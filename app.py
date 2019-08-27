import pymongo
import os


from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo

#connect to database
app = Flask(__name__)

app.config['MONGO_DBNAME'] ="Baby_Recipes"
app.config["MONGO_URI"] ="mongodb+srv://blueag8:mongo8@cluster0-iodau.mongodb.net/Baby_Recipes?retryWrites=true&w=majority"
app.config['SECRET_KEY'] = 'yum'    

mongo = PyMongo(app)


#home page



@app.route('/')
def home():
    return render_template("index.html", recipes=mongo.db.recipes.find(), all_ages=mongo.db.category_age.find())
    
#get 
#single recipe

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipes=mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    category_age=mongo.db.category_age.find()
    return render_template("recipe.html", recipes=recipes, category_age=category_age)

#TEST1
    
#recipes categorized per page route

#@app.route('/recipes')
#def recipes():
   # recipes=mongo.db.recipes.find()
    #TEST
    #for recipe in recipes:
      #  print(recipe)
        
   # return render_template("recipes.html")
    
@app.route('/recipes')
def all_recipes():
   return render_template("recipes.html", recipes=mongo.db.recipes.find())
   
   
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
    return render_template("recipes.html",recipes=mongo.db.recipes.find())

#add recipe 

@app.route('/addrecipe')
def addrecipe():
    #return render_template("testform.html",recipes=mongo.db.recipes.find(),
          # categories=mongo.db.categories.find())
    return render_template("addrecipe.html", all_ages=mongo.db.category_age.find())

#@app.route('/insert_recipe', methods=['POST'])
#def insert_recipe():
   # recipes=mongo.db.recipes
   # recipes.insert(request.form.to.dict(flat=False))
   # flash ("Thank you, your recipe has been added!")

    #return render_template("addrecipe.html", recipe=recipe)
    #Test1 Failed 
    
    #Testing2 
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    all_ages=mongo.db.category_age

    recipe_name=request.form["recipe_name"]
    category_age=request.form.get("category_age")
    cooking_time=int(request.form["cooking_time"])
    portion_sizes=int(request.form["portion_size"]) 
    allergens=request.form.getlist("allergen")
    ingredients=request.form.getlist("ingredient")
    recipe_description=request.form["recipe_description"]
    steps=request.form.getlist("step")
    
    if 'image' in request.files:
        image = request.files["image"]
        filename = image.save(request.files['image'])
        filepath = 'static/image/uploads/' + filename
    else: 
        filepath = 'static/image/babyappytite.png/'
        
    form={
    
        "recipe_name":recipe_name,
        "category_age":category_age,
        "cooking_time":cooking_time,
        "portion_size":portion_sizes,
        "allergen": allergens,
        "ingredient": ingredients,
        "recipe_description":recipe_description,
        "step": steps,
        
          }
          
     
    recipes.insert_one(form)
    
    return redirect(url_for('home', recipe=recipe, category_age=category_age))


#edit recipe
#@app.route('/editrecipe/<recipe_id>', methods=['GET','POST'])
#def editrecipe(recipe_id):
   
    #return render_template("testform.html",recipes=mongo.db.recipes.find(),
          # categories=mongo.db.categories.find())
    #return render_template("editrecipe.html",recipes=mongo.db.recipes.find({"_id": ObjectId(recipe_id)}),
          # categories=mongo.db.categories.find())

#TESTING 
@app.route('/editrecipe/<recipe_id>')
def editrecipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_ages=mongo.db.category_age.find()
    return render_template('editrecipe.html', recipe=the_recipe, category_age=all_ages)
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes=mongo.db.recipes
    all_ages=mongo.db.category_age
    recipes.update( {'_id': ObjectId(recipe_id)},
   
    {
            'recipe_name':request.form.get("recipe_name"),
            'category_age':request.form.get("category_age"),
            'cooking_time':int(request.form["cooking_time"]),
            'portion_sizes':int(request.form["portion_size"]),
            'allergens':request.form.getlist('check'),
            'ingredients':request.form.getlist("ingredient"),
            'recipe_description':request.form.get("recipe_description"),
            'steps':request.form.getlist("step"),
            'filename':image.save(request.files['image']),
      })
          
    #flash ("Thank you, your recipe has been added!")
    return redirect(url_for('home'))
    
   # filepath = '../static/img/' + filename

    #filename = image.save(request.files['image']
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('home'))

# routing for likes
#referred to another student's code for likes.

@app.route('/stars/<recipe_id>',methods=["GET", "POST"])
def stars(recipe_id):
    
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        { '$inc': { 'stars': 1}}
    )
    
    return redirect(url_for('recipe',recipe_id=recipe_id))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)