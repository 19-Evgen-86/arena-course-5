from flask_restx import Resource

from flask import Flask, render_template, request, redirect, url_for

from classes.arena import Arena
from classes.base_classes import BaseUnit
from classes.equipments import Equipment
from classes.player_classes import unit_classes
from classes.players import PlayerUnit, EnemyUnit

app = Flask(__name__)

heroes = {
}
# TODO инициализируем класс арены
arena = Arena()


@app.route("/")
def menu_page():
    # TODO рендерим главное меню (шаблон index.html)
    return render_template("index.html ")


@app.route("/fight/")
def start_fight():
    # TODO выполняем функцию start_game экземпляра класса арена и передаем ему необходимые аргументы
    # TODO рендерим экран боя (шаблон fight.html)
    arena.start_game(player=heroes['player'], enemy=heroes['enemy'])
    return render_template('fight.html', heroes=heroes)


@app.route("/fight/hit")
def hit():
    # TODO кнопка нанесения удара
    # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)
    # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
    # TODO если игра не идет - пропускаем срабатывание метода (простот рендерим шаблон с текущими данными)
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result


    return render_template('fight.html', heroes=heroes,result=result)


@app.route("/fight/use-skill")
def use_skill():
    # TODO кнопка использования скилла
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
    # TODO кнопка пропус хода
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
    # TODO кнопка завершить игру - переход в главное меню
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
class ChooseHero(Resource):
    # TODO кнопка выбор героя. 2 метода GET и POST
    # TODO на GET отрисовываем форму.
    # TODO на POST отправляем форму и делаем редирект на эндпоинт choose enemy
    def get(self):
        result = {
            "header": "Выбирете героя",
            "classes": unit_classes,
            "weapon": Equipment().get_weapons_names(),
            "armor": Equipment().get_armors_names()
        }
        return render_template('hero_choosing.html', result=result)

    def post(self):
        name = request.form['name']
        armor = request.form['armor']
        weapon = request.form['weapon']
        unit_class = request.form['unit_class']
        player = PlayerUnit(name=name,
                            unit_class=unit_classes.get(unit_class))
        player.equip_armor(Equipment().get_armor(armor))
        player.equip_weapon(Equipment().get_weapon(weapon))
        heroes['player'] = player
        return redirect(url_for('choose-enemy'))


@app.route("/choose-enemy/", methods=['post', 'get'])
class choose_enemy(Resource):
    # TODO кнопка выбор соперников. 2 метода GET и POST
    # TODO также на GET отрисовываем форму.
    # TODO а на POST отправляем форму и делаем редирект на начало битвы
    def get(self):
        result = {
            "header": "Выбирете соперника",
            "classes": unit_classes,
            "weapon": Equipment().get_weapons_names(),
            "armor": Equipment().get_armors_names()
        }
        return render_template('hero_choosing.html', result=result)

    def post(self):
        name = request.form['name']
        armor = request.form['armor']
        weapon = request.form['weapon']
        unit_class = request.form['unit_class']
        ememy = EnemyUnit(name=name,
                          unit_class=unit_classes.get(unit_class))
        ememy.equip_armor(Equipment().get_armor(armor))
        ememy.equip_weapon(Equipment().get_weapon(weapon))
        heroes['ememy'] = ememy
        return redirect(url_for('start_fight'))


if __name__ == "__main__":
    app.run()
