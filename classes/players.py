from random import randint

from classes.base_classes import BaseUnit


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар игрока:
        здесь происходит проверка достаточно ли выносливости для нанесения удара.
        вызывается функция self._count_damage(target)
        а также возвращается результат в виде строки
        """
        if self.stamina > self.weapon.stamina_per_hit:
            damage = self._count_damage(target)
            if damage > 0:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
            else:
                return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        else:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:

        """
                функция удар соперника
                должна содержать логику применения соперником умения
                (он должен делать это автоматически и только 1 раз за бой).
                Например, для этих целей можно использовать функцию randint из библиотеки random.
                Если умение не применено, противник наносит простой удар, где также используется
                функция _count_damage(target
                """

        if not self._is_skill_used and self.stamina > self.unit_class.skill.stamina and randint(0, 100) < 10:
            self.use_skill(target)

        if self.stamina > self.weapon.stamina_per_hit:
            damage = self._count_damage(target)
            if damage > 0:
                return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
            else:
                return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        else:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
