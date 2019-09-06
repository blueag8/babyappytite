#Babyappytite
 
##About Project 

This is a data centric project which utiizes MongoDB, a noSql database to 
store data and a Flask driven app to provide a user driven application which allows
users to 'Create', 'Read','Update' and 'Delete' information provided on the website.

The main technologies used for this project include HTML, CSS, JavaScript, Python+Flask.
Along with the frameworks provided by https://materializecss.com/

The initial idea was to create an application for 'parents and caregivers' of 
children aged from six to twelve months plus. This application would allow users 
to share and access recipes for children to help with the 'weaning' process. 

"Weaning is the process of gradually introducing an infant to what will be its adult diet while withdrawing the supply of its "mother's" milk.""

Because it is very important that a child is weaned in stages, usally by months at 
a time, the recipes are grouped by age.

#The Schema used for storing this data in MongoDB is as follows:

The database "Baby_Recipes", contains two collections: "Categories" and "Recipes".
Both of these collections contain a Key "category_age" with corresponding values
ie. "category_age": "6 months +"



![alt wireframe](Schema_Categories.png "recipes")

![alt wireframe](Schema_Recipe.png "categories")


Issues







Future implementations

-Registered login/user identity
-ability to only edit or delete 'user' owned entries
-Image upload
-Social media links
-Search bar
-Allergen filter 
-Commenting ability








##links

view herokuapp [here]

https://babyappytite.herokuapp.com

view development [here]

https://us-east-1.console.aws.amazon.com/cloud9/ide/1a05c8f8cda04b528eac19bc618c2909

github repository [here]

https://github.com/blueag8/babyappytite

to test app in development set configuration as follows:








![alt wireframe](wireframeforbabyappytite.jpg "mockup")


##UX
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

Existing Features
Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

##Features Left to Implement
Another feature idea
Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

JQuery
The project uses JQuery to simplify DOM manipulation.
Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

##Credits

https://stackoverflow.com/questions/14853779/adding-input-elements-dynamically-to-form
https://www.annabelkarmel.com/
https://www.seekclipart.com/aboutseek/
https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
https://flask-pymongo.readthedocs.io/en/latest/
https://jshint.com/



Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X


