from app import db

class CharacterBase(db.Model):
    name = db.Column(db.String, primary_key=True)
    attribute = db.Column(db.String)
    specialty = db.Column(db.String)
    faction = db.Column(db.String)

    base_hp = db.Column(db.Integer)
    base_def = db.Column(db.Integer)
    base_crit_rate = db.Column(db.Integer)
    base_crit_dmg = db.Column(db.Integer)
    base_pen_ratio = db.Column(db.Integer)
    base_impact = db.Column(db.Integer)
    base_anomaly_mastery = db.Column(db.Integer)
    base_anomaly_proficiency = db.Column(db.Integer)
    base_energy = db.Column(db.Integer)
