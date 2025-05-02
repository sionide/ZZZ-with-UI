from app import myapp_obj
from flask import render_template
from flask import redirect
from app import db

@myapp_obj.route("/")
def main():
    return render_template("home.html")