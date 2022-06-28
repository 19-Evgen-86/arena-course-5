from dataclasses import dataclass


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill:


# Инициализируем экземпляр класса и присваиваем ему необходимые значения аттрибутов
WarriorClass = UnitClass(name="Воин", max_health=100, max_stamina=80, attack=15, stamina=50, armor=10)

RogueClass = UnitClass(name="Разбойник", max_health=80, max_stamina=100, attack=10, stamina=70, armor=7)

unit_classes = {
    RogueClass.name: RogueClass,
    WarriorClass.name: WarriorClass
}
