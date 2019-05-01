from enum import Enum, auto
from abc import ABC
class ResourceCard(Enum):
    Brick = auto()
    Grain = auto()
    Lumber = auto()
    Ore = auto()
    Wool = auto()

class DevelopmentCard(ABC):
    pass

class VictoryPointCard(DevelopmentCard):
    pass

class ProgressCard(DevelopmentCard):
    pass

class MonopolyCard(ProgressCard):
    pass

class RoadBuildingCard(ProgressCard):
    pass

class YearOfPlentyCard(ProgressCard):
    pass

class KnightCard(DevelopmentCard):
    pass
    
