from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from classes.equipments import Weapon, Armor

STAMINA_TURN_UP = 1


@dataclass
class BaseUnitClass:
    """
    класс (воин,маг,разбойник) юнита
    """
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: BaseSkill


class BaseSkill(ABC):
    """
    класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        """
        параметр описывающий название умения
        """
        pass

    @property
    @abstractmethod
    def stamina(self):
        """
        параметр описывающий колличество выносливости, необходимое для приминения умения
        """
        pass

    @property
    @abstractmethod
    def damage(self):
        """
        параметр описывающий количество урона, наносимого умением
        """
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        """
        метод описыающий логику приминения умения
        """
        pass

    def _is_stamina_enough(self):
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """

    def __init__(self, name: str, unit_class: BaseUnitClass):
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon: Weapon = None
        self.armor: Armor = None
        self._is_skill_used: bool = False

    @property
    def health_points(self):
        return f"У {self.name} осталось {self.hp} очков здоровья"

    @property
    def stamina_points(self):
        return f"У {self.name} осталось {self.stamina} очков выносливости"

    def equip_weapon(self, weapon: Weapon):
        # присваиваем нашему герою новое оружие
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        #  одеваем новую броню
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        stamina_turn_up = STAMINA_TURN_UP * self.unit_class.stamina
        damage: int
        # расчета урона игрока
        unit_damage = self.weapon.damage * self.unit_class.attack
        #  расчет брони цели
        target_defence = self.armor.defence * self.unit_class.armor
        # выносливость после удара
        if self.stamina >= self.weapon.stamina_per_hit:
            self.stamina = self.stamina - self.weapon.stamina_per_hit + stamina_turn_up
            if target.stamina < target.armor.stamina_per_turn:
                damage = unit_damage - target_defence
                target.get_damage(damage)
                return damage
            else:
                damage = unit_damage - target_defence
                target.get_damage(damage)
                return damage
        else:
            self.stamina += stamina_turn_up
            return 0

    def get_damage(self, damage: int) -> Optional[int]:
        self.hp -= damage
        return damage

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        """
        этот метод будет переопределен ниже
        """
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        метод использования умения.
        если умение уже использовано возвращаем строку
        Навык использован
        Если же умение не использовано тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернем нам строку которая характеризует выполнение умения
        """
        if self._is_skill_used:
            return "Навык использован"
        else:
            self._is_skill_used = True
            self.unit_class.skill.use(user=self, target=target)

