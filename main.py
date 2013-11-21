import flask
from flask import Flask
app = flask.Flask(__name__)

@app.route("/logs", methods=['PUT'])
def root():
    for log in request.json['logs']:
        pass

if __name__ == "__main__":
    app.run()
