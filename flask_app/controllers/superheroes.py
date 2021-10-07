from flask_app import app
from flask import render_template,request
from flask import jsonify
import requests
import os        
import dotenv


@app.route("/")
def form():
    return render_template("index.html")

@app.route('/search', methods=["POST"])
def query_():
    print(request.form)
    pw = os.environ.get("SUPERHERO_KEY")
    url = f"https://superheroapi.com/api/{pw}/search/{request.form['query']}"
    print(url)
    r = requests.get(url)
    print(r,r.json())
    return jsonify(r.json())

