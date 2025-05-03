from sqlalchemy import ForeignKey

from app import db
from app.models import CharacterBase

# This is kinda like inheritance??
# Needs app to run to add for some reason
# Maybe it's the query???
class CharacterInstance(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    base_id = db.Column(db.Integer, ForeignKey('character_base.id'))
    attribute = db.Column(db.String)
    specialty = db.Column(db.String)
    faction = db.Column(db.String)

    base_hp = db.Column(db.Integer)
    base_def = db.Column(db.Integer)
    base_atk = db.Column(db.Integer)
    base_crit_rate = db.Column(db.Integer)
    base_crit_dmg = db.Column(db.Integer)
    base_pen_ratio = db.Column(db.Integer)
    base_impact = db.Column(db.Integer)
    base_anomaly_mastery = db.Column(db.Integer)
    base_anomaly_proficiency = db.Column(db.Integer)
    base_energy_regen = db.Column(db.Integer)

    def __init__(self, base_id):
        base = CharacterBase.query.get(base_id)

        self.name = base.name
        self.base_id = base_id
        self.attribute = base.attribute
        self.specialty = base.specialty
        self.faction = base.faction
        self.base_hp = base.base_hp
        self.base_def = base.base_def
        self.base_atk = base.base_atk
        self.base_crit_rate = base.base_crit_rate
        self.base_crit_dmg = base.base_crit_dmg
        self.base_pen_ratio = base.base_pen_ratio
        self.base_impact = base.base_impact
        self.base_anomaly_mastery = base.base_anomaly_mastery
        self.base_anomaly_proficiency = base.base_anomaly_proficiency
        self.base_energy_regen = base.base_energy_regen

    def __repr__(self):
        print(self.base_id)
        print(self.name)
        print(self.attribute)
        print(self.specialty)
        print(self.faction)
        print(self.base_hp)
        print(self.base_def)
        print(self.base_atk)
        print(self.base_crit_rate)
        print(self.base_crit_dmg)
        print(self.base_pen_ratio)
        print(self.base_impact)
        print(self.base_anomaly_mastery)
        print(self.base_anomaly_proficiency)
        print(self.base_energy_regen)
        return ""