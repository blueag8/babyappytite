

# BabyAppytite | Recipe's for 6 months +


view Heroku app [here]

https://babyappytite.herokuapp.com

GitHub repository [here]

https://github.com/blueag8/babyappytite

## About The Project

This is a data-centric project which utilizes MongoDB, a NoSQL (non-relational) database used to store data, and a Flask driven app to provide a user-driven application which allows users to 'Create', 'Read','Update' and 'Delete' information provided on the site.

The main technologies used for this project include:
HTML, CSS, JavaScript, Python+Flask.

Along with the framework provided by https://materializecss.com/,

Git and GitHub are used for version control,

AWS Cloud9 used for development.

View [here]

https://us-east-1.console.aws.amazon.com/cloud9/ide/1a05c8f8cda04b528eac19bc618c2909

Deployment via "Heroku"* 

*See further below for more on deployment.

## The Idea

The initial idea was to create an application for 'parents and caregivers' of children aged from six to twelve months plus. This application would allow users to share and access recipes for children to help them through the weaning* process. 

*Weaning is the process of gradually introducing an infant to an adult diet while gradually withdrawing the supply of 'Infant' milk.

Because a child must be weaned in stages, usually by months at a time, the recipes are grouped by stages.


# UX
**External User Story**

As a user, I want to explore different ideas for recipes to feed my baby. I want to know if they are tried or liked by others, as I prefer to try first, recipes that seem to be enjoyed. 

I wish to be able to share/exchange recipes with others. 
As my child needs to be introduced to foods in stages I want to refer to recipes that are relative to the developmental stage my child is at. 

As a user I want:

 -  a site that is visually appealing and easy to use.
 - a main page that is easy to navigate.
 - the ability to preview recipes before I view the entire one.
 - I want to know how many servings the recipe makes.
 - I want to know the time it will take to make each recipe.
 - I want to know the ingredients and if there are any allergens.
 - I want a clear step by step instructions on how to prepare the recipe.
 - I want to easily Share, Edit or Delete recipes.
 - If a recipe is successful I would like the ability to like it so that I can provide feedback to others. 
 

**Site Owners Potential**

The possibility to provide users with the ability to get an ingredients list to build a shopping list and to add items to a shopping cart. 

Reports could be made to provide feedback on the age-specific recipes being favourited, advertising can also be customized to target 'age' specific audiences.

Login/registration features will provide the site owner with a customer database which in future can be used to build and maintain customer relationships. 

## Development Process
**Wireframes**

![wireframe for babyappytite](https://res.cloudinary.com/blueag8/image/upload/v1567947477/Babyappytite/wireframe_for_babyappytite_xvntx4.jpg)
[https://www.justinmind.com](https://www.justinmind.com/) used trial to help produce mock up templates
![plans for recipe page](https://res.cloudinary.com/blueag8/image/upload/v1567947507/Babyappytite/HTML_Recipes_list_by_age_akjzhw.jpg)
> Written with [StackEdit](https://stackedit.io/).

## Data Schema
**The Schema used for storing this data in MongoDB is as follows:**

The database "Baby_Recipes", contains two collections: "Categories" and "Recipes".
Both of these collections contain a Key "category_age" with corresponding values
ie. "category_age": "6 months +"

**Recipe**
![Schema for Recipe](https://res.cloudinary.com/blueag8/image/upload/v1567948039/Babyappytite/schema_recipe_v5ju6b.png)

**Category**
![Schema for categories](https://res.cloudinary.com/blueag8/image/upload/v1567948041/Babyappytite/schema_categories_ujf8do.png)

##  Features
*Current*
 - Add recipe
 - Read recipes 
 - Edit recipe
 - Delete recipe
 
*Still requiring implementation*

 - User  authentification: login and registration
 - Upload images, storage to be in Cloudinary. Cloudinary have a pre-existing API widget uploader feature which can be integrated into the application.
 - Search Bar
 - Filters for allergens and ingredients

*Future possible implementations/opportunities*

 - Commenting functionality to provide users the opportunity to give further feedback about a recipe and any suggestions on adjustments
 - Ability for users to generate a shopping list
 - As the site owner, I may wish to collaborate with external companies or my own and build a shopping cart functionality from the shopping list. 
 
## Technologies Used

 - HTML checked with [https://validator.w3.org/nu/#textarea](https://validator.w3.org/nu/#textarea)
 - CSS for styling and checked using https://jigsaw.w3.org/css-validator/validator<p><a href="http://jigsaw.w3.org/css-validator/check/referer"><img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" /> </a></p>

 - Flask 1.1.1- web framework
 - Flask-Pymongo 2.3.0- to bridge Flask and MongoDB 
 - Python 0.15.5
 - Jinga 2.10.1- templating language for Python similar to Django
 -   jQuery- to simplify DOM manipulation. 
 - Materialize 0.100.2 - used to aid styling and functionality
 - Werkzeug 0.15.5-for development and debugging
 - MongoDB Atlas to store data
 - Cloudinary 1.17.0- used to store images as an external source
 - Heroku 0.1.4- used as a platform for deployment
 - Git and GitHub- used for version control. I realised at the end of the project that all commits are under the default Ubuntu name. I attempted to correct this in my final commits but unsure on how to correct the past commits.
 

**Process**
Due to time restraints and a deadline to submit project, there are still yet many implementations and adjustments required before I would call this is a saleable application and one I am proud of to publicize. 

To insert recipes in bulk I used notepad see "recipes.txt" in "documents and wireframes" folder. This was easily copied and pasted into the AWS CLI to allow a quick installation of documents to the database. 

I commenced development of the application using both frameworks "Materialize" and "Bootstrap". A tutor suggested that the frameworks may try to compete with each other. At this stage, I was nearing the deadline and had already written the bulk of my application. I was having issues with my forms no longer submitting data properly. As suggested I removed Bootstrap, which affected any HTML and CSS editing I had previously done. This caused quite a few issues with the styling and also with some of the JavaScript functionality.

The functionality is successful, with users being able to create, edit and delete entries.  However, as there is currently no registration or user login feature available, this means that access is to the 'Public' meaning that anyone can edit or delete recipes which were previously not published by them.

The functionality to share an image has yet to be implemented. 
At current, there is no option for a user to insert or edit recipe images.  A few images have been stored using the URL for the image link on Cloudinary, and stored in the Database as a string under "image".  To ensure that the image will not disappear on the editing/updating of the recipe the mongo operator $set has been used on all other form fields, meaning that these will be targeted and image will remain the same.
Allergens and special diets such as vegetarian, vegan etc are now a huge priority to many when planning meals. Also due to time restraints, I am yet to implement the ability to filter recipes for user preferences and needs.  Allergens at present are still listed in the recipes and are stored in the database but recipes are not separated from each other within the category "ages".

**Responsive Design and styling**

Because of the time restraints and encountering many issues with the functionality of the application, which caused delays, the responsive design has much yet to be desired. 
Layout is 'OK' on portrait mobile but not if viewed in landscape. Desktop layout is 'better' but not ideal.
 
Images need resizing and adjusting still for a sharper and better image quality. 

The Yellow used for "7 months +" is quite harsh on the users eye. An alternative colour will be more visually pleasing.

## Testing

 - The application was tested on mobile (Honor PCT-L29 by Huawei) and desktop
 - Checked add form successfully submits data to the MongoDB Storage
 - Checked edit form returns previously saved data and allows new input to successfully update data in the database
 - Checked button functionality cancel returns user to previous page, "Go back to Recipes" returns users to the list of recipes previously viewed. "Share", "Update" and "Delete" Buttons successfully trigger modals and the confirmation buttons within the modals, successfully alter data in the database
 - Checked delete function removes data from the database
 - Checked recipes are saved and loaded within specialized categories in which they should be assigned
 - Checked app is intuitive for the user (added modals to help the user know that entries/edits have been successful)
 -Ensured that these were clear and obvious. 
 -Checked images maintain ratio on different view sizes
 -Used the print function in app.py to test code functionality using Werkzeug debugger
 
**Process/Challenges **

I encountered multiple issues with the browser caching, this meant that I had to manually restart the application regularly and clear any cookies by processing an "Empty cache and/or hard refresh".
Because I had not realized this was an issue until late in my project this caused me a considerable delay. It is possible, that errors may have been corrected quickly but because the browser was not refreshing, I had assumed the corrections had not been successful so continued to alter the code when it may have been unnecessary, thus adding to the time taken to develop a functioning application.

**Issues encountered** 

*Issue* 1. Form submitted successfully on adding but on editing the category age value was changed from ''string' to 'null' when returned to database. This resulted in the recipe disappearing from the application 'get_recipe' results.
*Solution:* HTML Jinga templates were incorrect and the placement needed to be adjusted.

*Issue* 2. Modals not firing from triggers also resulted in forms not being submitted.
*Solution:* This was because I had used  Bootstrap as the framework to provide the template for the Modal. The functionality was affected when I removed the Bootstrap framework. This was solved by using the Materialize Modal template.

*Issue* 3. Checkbox values not saving.
*Solution:* Also a result of having used two frameworks and removing one without adjusting the HTML.  Correcting the HTML and so that the Javascript would match up to the Materialize template.

*Issue* 4. Routes to category-specific recipes returning all recipes and not filtering the recipes by age/stages as it should have. This was a result of routing issues whilst merging the four previous routes to recipes. I had previously separated the routes for each category-age which did not reflect the "DRY" principle of coding, this was brought to my attention from my tutor Anto.  I found it challenging to achieve the result I had desired of displaying recipes on age-specific pages. I had two collections in the database and wished to ensure that they would relate to each other.  I attempted to try the $lookup functionality which worked in the CLI connection to MongoDB but I could not translate into Python for the application.
The solution was to create a route using the variable "category-age" and to target the "Recipes"  collection with a field filter/search function, rather than trying to access the categories collection and using the category id.

*Issue* 6. "Add Steps" and "Add Ingredient" fields not saving data.
*Solution:* This was a result of a jQuery and targeting the buttons, the names were not identical to what the class was on the Html page. The name field on the inputs in the javascript had an '[]' on them which also caused issue.

## Deployment

Requirements to run code locally:

1. Clone the repository at 
https://github.com/blueag8/babyappytite.git
2. Install Python 3.6 using the command $pip3 install python
3. Install Flask-Pymongo using the command $pip3 
install flask-pymongo
4. Create a requirements.txt file by using the command $pip3 freeze --local > requirements.txt
5.  Create a Procfile with the command $echo web: python app.py 
6. Install Heroku via the CLI with $sudo install Heroku --classic
7. Heroku config vars need to be set 

Port 0.0.0.0
IP 8080
MONGO_URI

For the purpose of assesment the following configs are required:
Database Name= "Baby_Recipes"
MONGO URI ="mongodb+srv://blueag8:mongo8@cluster0-iodau.mongodb.net/Baby_Recipes?retryWrites=true&w=majority"

line 167.  in app.py

(for testing  purposes set debug to =True.) 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)

# Credits

**Acknowledgements:**

Mentor Antonio Rodriguez

Code Institue module and tutorial for Data-Centric Development
[https://github.com/Code-Institute-Solutions/TaskManager](https://github.com/Code-Institute-Solutions/TaskManager)
Code Institute Tutors:
Michael Park
Niel McEwan
Slack Channel #Data-Centric-Dev:
Fellow student's questions on Slack and referred to projects including:
Dave O'dea's "FlaskBook" Recipe App 
https://github.com/davedodea/FlaskBook
Deirdre Welden's "DumpDinners" Recipe App
https://github.com/Deirdre18/dumpdinners-recipe-app

jQuery- function to add or delete fields
Utilized some Materialise selection functions and modal trigger.

(Borrowed and adjusted code to add a functioning button to add and delete recipe ingredients and steps so that
the could be submitted as array items, and returned as list items).
Please see:

https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
https://stackoverflow.com/questions/14853779/adding-input-elements-dynamically-to-form

**Images** used from 
https://www.seekclipart.com/clipart/
Category-age and image links edited and or produced by myself using paint.
Recipe images from the Ebook from https://www.annabelkarmel.com/

**Recipes** borrowed for development **from** 

https://www.annabelkarmel.com/

**Referenced** following documentation, tutorials and code checking sites:
https://flask-pymongo.readthedocs.io/en/latest/
https://docs.mongodb.com/manual/crud/
https://jshint.com/
https://www.w3schools.com
https://www.10bestdesign.com/dirtymarkup/



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MDk4MDk5NjddfQ==
-->