from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class Skill(ABC):
    """
    Базовый класс умения
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
