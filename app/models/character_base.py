from app import db

class CharacterBase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    attribute = db.Column(db.String)
    specialty = db.Column(db.String)
    faction = db.Column(db.String)

    base_hp = db.Column(db.Integer)
    base_def = db.Column(db.Integer)
    base_atk = db.Column(db.Integer)
    base_crit_rate = db.Column(db.Integer, default = 5)
    base_crit_dmg = db.Column(db.Integer, default = 50)
    base_pen_ratio = db.Column(db.Integer, default = 0)
    base_impact = db.Column(db.Integer)
    base_anomaly_mastery = db.Column(db.Integer)
    base_anomaly_proficiency = db.Column(db.Integer)
    base_energy_regen = db.Column(db.Integer, default = 1.2)

    def __repr__(self):
        return """{0}
        {1}, {2}, {3},
        hp {4} def {5} atk {6}
        """.format(self.name, self.attribute, self.specialty, self.faction, self.base_hp, self.base_def, self.base_atk)
