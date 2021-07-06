from flask_pymongo import PyMongo
from app.config import MongoUri
import urllib 

# functions for database connectivity

def init_db():
    mongo = PyMongo()
    return mongo


def get_db(app, mongo):
    app.config["MONGO_URI"] = MongoUri
    mongo.init_app(app)
