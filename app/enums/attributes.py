from enum import auto, Flag
import operator
from functools import reduce

# Honestly I just found this online to enable an all attribute flag that was dynamic and updated automatically
# https://stackoverflow.com/questions/42251081/representation-of-all-values-in-flag-enum
class AllFlag(Flag):
    @classmethod
    def all(cls):
        cls_name = cls.__name__
        if not len(cls):
            raise AttributeError(f"Empty {cls_name} does not have an ALL value")
        value = reduce(operator.or_, cls)
        cls._member_map_['ALL'] = value
        return value

class Attribute(AllFlag):
    ELECTRIC: int = auto()
    ETHER: int = auto()
    FIRE: int = auto()
    ICE: int = auto()
    PHYSICAL: int = auto()

def convert_string_to_attribute(string: str):
    attributes_list = string.split('|')
    result = Attribute(0)
    for attribute in attributes_list:
        result |= Attribute[attribute] # Uses a bitwise operator to enable attributes
    return result
