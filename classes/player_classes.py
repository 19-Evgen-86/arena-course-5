from classes.base_classes import BaseUnitClass
from classes.skill_classes import FuryPunch

WarriorClass = BaseUnitClass(name="Воин", max_health=100, max_stamina=80, attack=15, stamina=50, armor=10,
                             skill=FuryPunch())

RogueClass = BaseUnitClass(name="Разбойник", max_health=80, max_stamina=100, attack=10, stamina=70, armor=7)


unit_classes = {
    RogueClass.name: RogueClass,
    WarriorClass.name: WarriorClass
}
