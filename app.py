import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'CarHire'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)