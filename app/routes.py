from app import myapp_obj
from flask import render_template
from flask import redirect
from app import db
from app.models.character_base import CharacterBase
from app.models.buff_base import BuffBase

@myapp_obj.route("/")
def main():
    return render_template("home.html")

@myapp_obj.route("/<int:character_id>")
def redirect_to_display(character_id):
    character_name = CharacterBase.query.get(character_id).name
    return redirect("/"+character_name)

@myapp_obj.route("/<string:character_name>")
def display(character_name):
    # select a character base without using primary key
    # legacy: character_base = CharacterBase.query.filter(CharacterBase.name == character_name).all()[0]
    # look at https://flask-sqlalchemy.readthedocs.io/en/stable/queries/
    filter_by_name = db.select(CharacterBase).filter_by(name = character_name)
    character_base = db.session.execute(filter_by_name).scalar_one()
    return render_template('display_stats.html', character = character_base)