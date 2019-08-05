import os
import pymongo

from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

#connect to database
app = Flask(__name__)

app.config['MONGO_DBNAME'] ="Baby_Recipes"
app.config['MONGODB_URI'] = os.getenv("MONGO_URI")

@app.route('/Hello')
def Hello():
    print('Hello')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)