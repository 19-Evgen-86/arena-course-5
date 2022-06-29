from classes.base_classes import BaseUnit


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар игрока:
        здесь происходит проверка достаточно ли выносливости для нанесения удара.
        вызывается функция self._count_damage(target)
        а также возвращается результат в виде строки
        """
        pass
        # TODO результат функции должен возвращать следующие строки:
        f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
        f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."
        f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."

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
        # TODO результат функции должен возвращать результат функции skill.use или же следующие строки:
        f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."
        f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."
        f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."