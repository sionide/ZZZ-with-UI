import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import basedir
from models import CharacterBase, BuffBase, Weapon
from enums import Attribute, Specialty, Faction

# creates/finds file app.db as database to work with
engine = create_engine('sqlite:///' + os.path.join(basedir, 'app.db'), echo=True)

# create an instance of a session
Session = sessionmaker(bind = engine)
session = Session()

HarumasaBase = CharacterBase(name = "Harumasa",
                             attribute = Attribute.ELECTRIC.name, specialty = Specialty.ATTACKER.name, faction = Faction.HSO6.name,
                             base_hp = 7405, base_def = 600, base_atk = 915,
                             base_crit_rate = 19.4, base_crit_dmg = 50,
                             base_pen_ratio = 0, base_impact = 90,
                             base_anomaly_mastery = 90, base_anomaly_proficiency = 95,
                             base_energy_regen = 1.2)

# HarumasaCore = BuffBase(name = "Masa Core", bonus_dmg_attribute = Attribute.all().name, bonus_dmg = 40)

# buff = BuffBase(name = "Temp")

Starlight_Engine1 = Weapon(name = "Starlight Engine1", weapon_base_atk = 100, unconditional_atk_percent = 25, conditional_atk_percent = 19.2)

session.add(Starlight_Engine1)
session.commit()

print(HarumasaBase)