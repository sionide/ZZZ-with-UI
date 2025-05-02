from enum import Enum, auto

class Specialty(Enum):
    ANOMALY: int = auto()
    ATTACKER: int = auto()
    DEFENCE: int = auto()
    STUNNER: int = auto()
    SUPPORT: int = auto()