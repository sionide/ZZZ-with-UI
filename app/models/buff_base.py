from app import db

class BuffBase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String)

    __mapper_args__ = {
        'polymorphic_on' : type,
        'polymorphic_identity': 'Base' }
