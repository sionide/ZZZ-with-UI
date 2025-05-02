import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import basedir
from app.models.character_base import CharacterBase
from enums.attributes import Attribute
from enums.specialties import Specialty
from enums.factions import Faction

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

session.add(HarumasaBase)
session.commit()

print(HarumasaBase)