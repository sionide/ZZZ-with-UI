from enum import auto, Flag


class Attribute(Flag):
    ELECTRIC: int = auto()
    ETHER: int = auto()
    FIRE: int = auto()
    ICE: int = auto()
    PHYSICAL: int = auto()