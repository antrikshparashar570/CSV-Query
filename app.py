from flask import Flask, render_template
from flask_restful import Resource, Api
from backend import data

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return render_template('frontend.html')

api.add_resource(data,'/data')

if __name__ == '__main__':
    app.run()