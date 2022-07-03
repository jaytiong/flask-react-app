from flask import Flask, jsonify, redirect, url_for, request, make_response
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ini db
db = SQLAlchemy(app)

# URL DB
class Urls(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    longer = db.Column("longer", db.String())
    shorter = db.Column("shorter", db.String(10))

    def __init__(self, longer, shorter):
        self.longer = longer
        self.shorter = shorter

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        randomLetters = random.choices(letters, k=5)
        randomLetters = "".join(randomLetters)
        short_url = Urls.query.filter_by(shorter=randomLetters).first()
        if not short_url:
            return "http://localhost:5000/" + randomLetters

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/<short_url>")
def redirectURL(short_url):
    short_url = "http://localhost:5000/" + short_url
    long_url = Urls.query.filter_by(shorter=short_url).first()
    urlToReturn = long_url.longer
    if (not (urlToReturn.startswith('http://') or urlToReturn.startswith("https://"))):
        urlToReturn = "http://" + urlToReturn

    if urlToReturn:
        return redirect(urlToReturn)
    else:
        return make_response(
            jsonify(
                Error="Please enter a valid URL.2"
            ), 404
        )

@app.route("/shorten_url",methods=['POST','GET'])
def test():
    if request.method =="POST":
        url_received = request.json['url']
        found_url = Urls.query.filter_by(longer=url_received).first()
        
        if found_url:
            return jsonify({'url':found_url.shorter})
        else:
            short_url = shorten_url()
            new_url = Urls(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            return jsonify({'url':short_url})  
    else:
        return make_response(
            jsonify(
                Error="Please enter a valid URL.3"
            ), 404
        )
        

@app.route("/urls",methods=['GET'])
def urls():
    url = Urls.query.all()
    return "meow"


# Run
if __name__ =="__main__":
    app.run(debug=True)