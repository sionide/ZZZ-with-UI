from app import db

class BuffBase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

    unconditional_atk_percent = db.Column(db.Integer, default = 0)
    unconditional_atk_flat = db.Column(db.Integer, default = 0)
    conditional_atk_percent = db.Column(db.Integer, default = 0)
    conditional_atk_flat = db.Column(db.Integer, default = 0)
    crit_rate = db.Column(db.Integer, default = 0)
    crit_dmg = db.Column(db.Integer, default = 0)
    bonus_dmg_attribute = db.Column(db.String, default = None)
    bonus_dmg = db.Column(db.Integer, default = 0)
    pen_ratio = db.Column(db.Integer, default = 0)
    pen_flat = db.Column(db.Integer, default = 0)
    anomaly_proficiency = db.Column(db.Integer, default = 0)
    anomaly_mastery = db.Column(db.Integer, default = 0)

    def_reduction = db.Column(db.Integer, default = 0)
    res_ignore = db.Column(db.Integer, default = 0)
    dmg_taken = db.Column(db.Integer, default = 0)
    out_of_stun = db.Column(db.Boolean, default = False)
    stun_dmg = db.Column(db.Integer, default = 0)