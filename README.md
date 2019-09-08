#BabyAppytite | Recipe's for 6 months +

view herokuapp [here]

https://babyappytite.herokuapp.com

github repository [here]

https://github.com/blueag8/babyappytite

 
##About The Project 

This is a data centric project which utiizes MongoDB, a noSql database used to 
store data, and a Flask driven app to provide a user driven application which allows
users to 'Create', 'Read','Update' and 'Delete' information provided on the site.

The main technologies used for this project include:
HTML, CSS, JavaScript, Python+Flask.

Along with the framework provided by https://materializecss.com/,

External images are stored on external API "Cloudinary.com"

Deployment is via Heroku 

Git and GitHub used for version control.

AWS Cloud9 used for development.

View [here]

https://us-east-1.console.aws.amazon.com/cloud9/ide/1a05c8f8cda04b528eac19bc618c2909


##The Idea

The initial idea was to create an application for 'parents and caregivers' of 
children aged from six to twelve months plus. This application would allow users 
to share and access recipes for children to help the through the weaning* process. 

*Weaning is the process of gradually introducing an infant to an adult diet while gradually withdrawing the supply of 'Infant' milk.

Because it is very important that a child is weaned in stages, usally by months at 
a time, the recipes are grouped by stages.


##UX

##External User

As a user I want to explore different ideas for recipes to feed my baby. I want to 
know if they are tried or liked by others, as I prefer to try first, recipes that 
seem to be enjoyed. 

I wish to be able to share/exchange recipes with others. 
As my child needs to be introduced to foods in stages I want to refer to recipes 
that are relative to the developmental stage my child is at. 

I want a site that is visually appealing and easy to use.

##Site Owners Future Prospects

The possibilty to provide users with the ability to get an ingredients list
to build a shopping list and to add items to a shopping cart. 

Reports could be made to provide feedback on the age specific recipes being favourited,
advertising can also be customized to target 'age' specific audiences.

Login/registration features will provide the site owner with a customer database 
which in future can be used to build and maintain customer relationships. 


##The Schema used for storing this data in MongoDB is as follows:

The database "Baby_Recipes", contains two collections: "Categories" and "Recipes".
Both of these collections contain a Key "category_age" with corresponding values
ie. "category_age": "6 months +"

![alt wireframe](wireframeforbabyappytite.jpg "mockup")

![alt wireframe](recipes_ list_ by_ age.jpg)

![alt wireframe](schema_categories.png "recipes")

![alt wireframe](schema_recipe.png "categories")


to insert recipes in bulk I used notepad see "recipes.txt"[here]
this was copied and pasted into the AWS CLI 

Commenced development of the application using both frameworks "Materialize" and "Bootsrap", tutor suggested the frameworks may try 
to compete with each other. Removed Bootstrap which affected any CSS editing I had previously done.



Issues

Testing 



UX design improvements required

Yellow used for "7 months +" is quite harsh on the users eye. An alternative colour will be 
more visually pleasing.

Future implementations-Registered login/user identity
-ability to only edit or delete 'user' owned entries
-Image upload
-Social media links
-Search bar
-Allergen filter 
-Shopping list

-Commenting ability
-Sorting new recipes at the top


Usability and Visual Impact:
Project Purpose
UX design
Suitability for purpose
Navigation
Ease of use
Information Architecture
Defensive Design
Layout and Visual Impact:
Responsive Design
Image Presentation
Colour scheme and typography


Bugs


Testing


to test app in development set configuration as follows:

requirements.txt [here]

Heroku vars

Port 0.0.0.0
IP 8080
MONGO URI "mongodb+srv://blueag8:******@cluster0-iodau.mongodb.net/Baby_Recipes?retryWrites=true&w=majority"

Dyno formation = web : Python 

 
For deployment:

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)

for testing set debug to True. 





Deployment
Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:


Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.







##Credits

###Aknowledgements:

Mentor Antonio Rodriguez

Code Institute Tutors:
Michael Park
Niel McEwan
Slack Channel #Data-Centric-Dev:
Fellow student's questions on Slack and referred to projects including
Dave O'dea's "FlaskBook" Recipe App 
https://github.com/davedodea/FlaskBook
Deirdre Welden's "DumpDinners" Recipe App
https://github.com/Deirdre18/dumpdinners-recipe-app

###jQuery-borrowed and adjusted code to add a functioning button to add and delete recipe ingredients and steps so that
the could be submited as array items, and returned as list items. 

Please see:

https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
https://stackoverflow.com/questions/14853779/adding-input-elements-dynamically-to-form

###Images used from 
https://www.seekclipart.com/clipart/
Category-age and image links edited and or produced by myself using paint.

Recipes borrowed for the purpose of development from 

https://www.annabelkarmel.com/
see Ebook in "documents and wireframe" [here] 


Utilized following documentation, turorials and code checking sites:
https://flask-pymongo.readthedocs.io/en/latest/
https://docs.mongodb.com/manual/crud/
https://jshint.com/
https://www.w3schools.com
https://www.10bestdesign.com/dirtymarkup/





