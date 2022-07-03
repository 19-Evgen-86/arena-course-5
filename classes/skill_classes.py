from classes.base_classes import BaseSkill


class FistOfFury(BaseSkill):
    name = "Кулак ярости"
    stamina = 8
    damage = 12

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} применил {self.name} и нанес {self.damage} урона {self.target.name}"


class PreciseKick(BaseSkill):
    name = "Точный пинок"
    stamina = 10
    damage = 18

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f"{self.user.name} применил {self.name} и нанес {self.damage} урона {self.target.name}"
