from enum import Enum, auto, unique
# defining an enumeration class 

class Color(Enum):
    RED = 1
    INDIGO = 2
    GREEN = 3
    VIOLET = 4
    WHITE = 5
    BLUE  = 6
# accessing enum members   
print(Color.RED)
print(Color.RED.value)

# iterating over members
for color in Color:
    print(color)
    
# check if value is part of enum

print(Color.RED in Color)
# print(Color.YELLOW in Color)

# ordered enum
class Size(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    
print(Size.SMALL.value)
print(Size.MEDIUM.value)
print(Size.LARGE.value)

@unique #for unique values
class Day(Enum):
    
    MONDAY = 1
    TUESDAY = 2 
    WEDNESDAY= 3
    THURSDAY = 4
    FRIDAY = 5
    