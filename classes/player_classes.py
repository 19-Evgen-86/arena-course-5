from classes.base_classes import BaseUnitClass
from classes.skill_classes import FistOfFury, PreciseKick

WarriorClass = BaseUnitClass(name="Воин", max_health=50, max_stamina=20, attack=1.7, stamina=1.3, armor=1.2,
                             skill=FistOfFury())

RogueClass = BaseUnitClass(name="Разбойник", max_health=30, max_stamina=30, attack=1.1, stamina=1.5, armor=0.8,
                           skill=PreciseKick())

unit_classes = {
    RogueClass.name: RogueClass,
    WarriorClass.name: WarriorClass
}
