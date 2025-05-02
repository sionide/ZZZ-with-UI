# ZZZ-with-UI

How I set up my environment

Using bash terminal:
    
set up virutal environment:

    python -m venv venv
    source venv/Scripts/activate

set up libraries:

    pip install Flask
    pip install sqlalchemy
    pip install flask-wtf
    pip install flask-login

    pip3 freeze > requirements.txt


install libraries from requirements.txt:

    pip install -r requirements.txt

use flask shell to set up your database:
    
    flask shell

    from app import db
    db.creata_all()
    exit()