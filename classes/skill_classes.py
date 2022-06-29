from classes.base_classes import BaseSkillClass


class FuryPunch(BaseSkillClass):
    name = "Кулак ярости"
    stamina = 20
    damage = 35

    def skill_effect(self):
        # TODO логика использования скилла -> return str
        # TODO в классе нам доступны экземпляры user и target - можно использовать любые их методы
        # TODO именно здесь происходит уменшение стамины у игрока применяющего умение и
        # TODO уменьшение здоровья цели.
        # TODO результат применения возвращаем строкой

        pass