from flask import Flask, render_template, request, redirect, url_for

from flask_pymongo import PyMongo
import os
if os.path.exists('env.py'):
    import env
from bson.json_util import dumps, loads

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)


# your code here
@app.route("/")
def home():
    return render_template('home.template.html')

@app.route("/get_tasks")
def get_tasks():
    return render_template("get_tasks.template.html", task=mongo.db.task.find())   



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)