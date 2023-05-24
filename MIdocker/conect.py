from flask import flask
from flask import request
from flask import render_template

var = Flask(__name__)

@var.route("/")
def main():
	return render_template("index.html")

if __name__ == "__main__":
	var.run(host="0.0.0.0", )
