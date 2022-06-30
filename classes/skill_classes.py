from classes.base_classes import BaseSkill


class FistOfFury(BaseSkill):
    name = "Кулак ярости"
    stamina = 8
    damage = 12

    def skill_effect(self):
        self.user.stamina -= self.stamina
        damage = self.damage - self.target.armor.defence * self.target.unit_class.armor
        self.target.hp -= self.damage - damage
        return f"{self.user.name} применил {self.name} и нанес {damage} урона {self.target.name}"


class PreciseKick(BaseSkill):
    name = "Точный пинок"
    stamina = 10
    damage = 18

    def skill_effect(self):
        self.user.stamina -= self.stamina
        damage = self.damage - self.target.armor.defence * self.target.unit_class.armor
        self.target.hp -= self.damage - damage
        return f"{self.user.name} применил {self.name} и нанес {damage} урона {self.target.name}"
