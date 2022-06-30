from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from classes.equipments import Weapon, Armor


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
    skill: BaseSkillClass


class BaseSkillClass(ABC):
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
        self._hp = unit_class.max_health
        self._stamina = unit_class.max_stamina
        self.weapon: Weapon
        self.armor: Armor
        self._is_skill_used: bool = False

    @property
    def health_points(self):
        return f"У {self.name} осталось {self._hp} очков здоровья"

    @property
    def stamina_points(self):
        return f"У {self.name} осталось {self._stamina} очков выносливости"

    def equip_weapon(self, weapon: Weapon):
        # TODO присваиваем нашему герою новое оружие
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        # TODO одеваем новую броню
        return f"{self.name} экипирован броней {self.armor.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        damage: int
        # TODO Эта функция должна содержать:
        #  логику расчета урона игрока
        #  логику расчета брони цели
        #  здесь же происходит уменьшение выносливости атакующего при ударе
        #  и уменьшение выносливости защищающегося при использовании брони
        #  если у защищающегося нехватает выносливости - его броня игнорируется
        #  после всех расчетов цель получает урон - target.get_damage(damage)
        #  и возвращаем предполагаемый урон для последующего вывода пользователю в текстовом виде
        return damage

    def get_damage(self, damage: int) -> Optional[int]:
        # TODO получение урона целью
        #      присваиваем новое значение для аттрибута self.hp
        pass

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
        pass
