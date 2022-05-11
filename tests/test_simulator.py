from ..pokemons_fight_simulator.classes.player import Player
from ..pokemons_fight_simulator.classes.move import Move
from ..pokemons_fight_simulator.classes.simulator import Simulator
from ..pokemons_fight_simulator.classes.pokemon import Pokemon
from ..pokemons_fight_simulator.config import mode


def test_create():
    simulator = Simulator(mode['against_player'])
    assert len(simulator.get_players()) == 2
    assert simulator.get_rounds() == 1


def test_set_mode():
    simulator = Simulator(mode['against_player'])
    assert simulator.get_mode() == mode['against_player']
    simulator.set_mode(mode['against_computer'])
    assert simulator.get_mode() == mode['against_computer']


def test_set_max_team_size():
    simulator = Simulator(mode['against_computer'])
    simulator.set_max_team_size(8)
    assert simulator.get_max_team_size() == 8
    computer_pokemons = simulator.generate_computer_pokemons()
    assert len(computer_pokemons) == 8


def test_reset():
    simulator = Simulator(mode['against_player'])
    player1, player2 = simulator.get_players()
    simulator.reset(mode['against_player'])
    new_player1, new_player2 = simulator.get_players()
    assert player1 is not new_player1
    assert player2 is not new_player2


def test_set_players():
    simulator = Simulator()
    player1 = Player('First')
    player2 = Player('Second')
    simulator.set_first_player(player1)
    simulator.set_second_player(player2)
    assert player1, player2 == simulator.get_players()


def test_set_current_player():
    simulator = Simulator(mode['against_player'])
    player1 = simulator.get_players()[0]
    simulator.set_current_player(player1)
    assert simulator.get_current_player() == player1


def test_set_computer_random_move():
    simulator = Simulator(mode['against_computer'])
    computer = simulator.get_players()[1]
    pok = Pokemon({'name': 'Pok', 'hp': 100, 'type1': 'cat', 'type2': 'dog'})
    computer.add_pokemon(pok)
    computer.set_current_pokemon(pok)
    assert computer.get_move() is None
    simulator._set_computer_random_move()
    assert computer.get_move() is not None


def test_generate_computer_pokemons():
    simulator = Simulator(mode['against_computer'])
    computer = simulator.get_players()[1]
    assert computer.get_pokemons() == []
    simulator.generate_computer_pokemons(2)
    assert len(computer.get_pokemons()) == 2


def test_is_ready_to_round_player_and_player():
    simulator = Simulator(mode['against_player'])
    player1, player2 = simulator.get_players()
    assert simulator._is_ready_to_round() is False
    player1.set_move(Move('skip'))
    assert simulator._is_ready_to_round() is False
    player2.set_move(Move('skip'))
    assert simulator._is_ready_to_round() is True


def test_hit_by_speed():
    simulator = Simulator(mode['against_player'])
    player1, player2 = simulator.get_players()
    pok1 = simulator.get_available_pokemons()[0]
    pok1.set_stat('speed', 10)
    hp1 = pok1.get_stat('hp')
    pok2 = simulator.get_available_pokemons()[1]
    pok2.set_stat('speed', 1)
    pok2.set_stat('hp', 1)
    player1.add_pokemon(pok1)
    player1.set_current_pokemon(pok1)
    player2.add_pokemon(pok2)
    player2.set_current_pokemon(pok2)
    simulator._hit_by_speed(player1, 2, 'normal attack',
                            player2, 3, 'special attack')
    assert pok1.get_stat('hp') == hp1
    assert pok2.is_alive() is False


def test_add_pokemon():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[111]
    pok2 = Pokemon.get_all_pokemons()[112]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    assert pok1 not in simulator.get_available_pokemons()
    assert pok2 not in simulator.get_available_pokemons()
    assert pok1 in player1.get_pokemons()
    assert pok2 in player2.get_pokemons()


def test_remove_pokemon():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[222]
    player1 = simulator.get_players()[0]
    simulator.add_pokemon(pok1, player1)
    assert pok1 not in simulator.get_available_pokemons()
    assert pok1 in player1.get_pokemons()
    simulator.remove_pokemon(pok1, player1)
    assert pok1 in simulator.get_available_pokemons()
    assert pok1 not in player1.get_pokemons()


def test_round_defense_both():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[0]
    pok2 = Pokemon.get_all_pokemons()[1]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    def1 = pok1.get_stat('defense')
    def2 = pok2.get_stat('defense')
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    player1.set_move(Move('defense'))
    player2.set_move(Move('defense'))
    simulator.round()
    assert pok1.get_stat('defense') > def1
    assert pok2.get_stat('defense') > def2


def test_round_defense_attack():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[2]
    pok2 = Pokemon.get_all_pokemons()[3]
    pok1.set_stat('speed', 45)
    pok2.set_stat('speed', 25)
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    def1 = pok1.get_stat('defense')
    hp1 = pok1.get_stat('hp')
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    player1.set_move(Move('defense'))
    player2.set_move(Move('normal attack'))
    simulator.round()
    assert pok1.get_stat('defense') > def1
    assert pok1.get_stat('hp') < hp1


def test_round_switch_attack():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[4]
    pok2 = Pokemon.get_all_pokemons()[5]
    pok3 = Pokemon.get_all_pokemons()[6]
    pok1.set_stat('speed', 45)
    pok2.set_stat('speed', 25)
    pok3.set_stat('speed', 25)
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    simulator.add_pokemon(pok3, player2)
    hp2 = pok2.get_stat('hp')
    hp3 = pok3.get_stat('hp')
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    player1.set_move(Move('normal attack'))
    player2.set_move(Move('switch', pokemon_to_set=pok3))
    simulator.round()
    assert pok2.get_stat('hp') == hp2
    assert pok3.get_stat('hp') < hp3


def test_round_attack_both_one_dies():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[7]
    pok2 = Pokemon.get_all_pokemons()[8]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    pok1.set_stat('hp', 1)
    hp2 = pok2.get_stat('hp')
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    player1.set_move(Move('normal attack'))
    player2.set_move(Move('special attack', special_attack_type='water'))
    simulator.round()
    assert pok2.get_stat('hp') == hp2
    assert pok1.is_alive() is False


def test_round_attack_both():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[9]
    pok2 = Pokemon.get_all_pokemons()[10]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    hp1 = pok1.get_stat('hp')
    hp2 = pok2.get_stat('hp')
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    player1.set_move(Move('normal attack'))
    player2.set_move(Move('special attack', special_attack_type='water'))
    simulator.round()
    assert pok2.get_stat('hp') < hp2
    assert pok1.get_stat('hp') < hp1


def test_round_move_is_none():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[9]
    pok2 = Pokemon.get_all_pokemons()[10]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    hp1 = pok1.get_stat('hp')
    hp2 = pok2.get_stat('hp')
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    player1.set_move(Move('normal attack'))
    simulator.round()
    assert pok2.get_stat('hp') == hp2
    assert pok1.get_stat('hp') == hp1


def test_round_computer_mode():
    simulator = Simulator(mode['against_computer'])
    pok1 = Pokemon.get_all_pokemons()[100]
    pok2 = Pokemon.get_all_pokemons()[101]
    player, computer = simulator.get_players()
    simulator.add_pokemon(pok1, player)
    simulator.add_pokemon(pok2, computer)
    hp2 = pok2.get_stat('hp')
    player.set_current_pokemon(pok1)
    computer.set_current_pokemon(pok2)
    player.set_move(Move('normal attack'))
    simulator.round()
    assert computer.get_comment()
    assert pok2.get_stat('hp') < hp2


def test_move_handler_defense():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[11]
    pok2 = Pokemon.get_all_pokemons()[12]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    player1.set_move(Move('defense'))
    def1 = pok1.get_stat('defense')
    hp1 = pok1.get_stat('hp')
    assert simulator._perform_move(player1, player2) == (None, None)
    assert pok1.get_stat('defense') > def1
    assert pok1.get_stat('hp') == hp1


def test_move_handler_switch():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[13]
    pok2 = Pokemon.get_all_pokemons()[14]
    pok3 = Pokemon.get_all_pokemons()[15]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player1)
    simulator.add_pokemon(pok3, player2)
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok3)
    player1.set_move(Move('switch', pok2))
    assert simulator._perform_move(player1, player2) == (None, None)
    assert player1.get_current_pokemon() == pok2


def test_move_handler_attack():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[16]
    pok2 = Pokemon.get_all_pokemons()[17]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    player1.set_move(Move('normal attack'))
    res = simulator._perform_move(player1, player2)
    assert res is not None
    assert res[0] > 0 and res[1] == 'normal attack'


def test_hit_and_comment():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[18]
    pok2 = Pokemon.get_all_pokemons()[19]
    player1, player2 = simulator.get_players()
    simulator.add_pokemon(pok1, player1)
    simulator.add_pokemon(pok2, player2)
    player1.set_current_pokemon(pok1)
    player2.set_current_pokemon(pok2)
    hp2 = pok2.get_stat('hp')
    simulator._hit_and_comment(player1, player2, 3, 'normal attack')
    assert hp2 == pok2.get_stat('hp') + 3
    assert player1.get_comment() == (
        f'{pok1} hits {pok2} with normal attack \nand causes 3 damage')


def test_comment_defense():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[20]
    player1 = simulator.get_players()[0]
    simulator.add_pokemon(pok1, player1)
    player1.set_current_pokemon(pok1)
    simulator._comment(player1, 'defense', value=5)
    assert player1.get_comment() == f'{pok1} increases his defense by 5'


def test_comment_skip():
    simulator = Simulator(mode['against_player'])
    player1 = simulator.get_players()[0]
    simulator._comment(player1, 'skip')
    assert player1.get_comment() == f'{player1} skips this round!'


def test_comment_switch():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[21]
    pok2 = Pokemon.get_all_pokemons()[22]
    player1 = simulator.get_players()[0]
    simulator.add_pokemon(pok1, player1)
    player1.set_current_pokemon(pok1)
    simulator._comment(player1, 'switch', new_pokemon=pok2)
    assert player1.get_comment() == f'{player1} switches {pok1} to {pok2}'


def test_comment_attack():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[23]
    pok2 = Pokemon.get_all_pokemons()[24]
    player1 = simulator.get_players()[0]
    simulator.add_pokemon(pok1, player1)
    player1.set_current_pokemon(pok1)
    simulator._comment(player1, 'attack',
                       enemy_pokemon=pok2,
                       attack_type='normal attack',
                       damage=4)
    assert player1.get_comment() == (
        f'{pok1} hits {pok2} with normal attack \nand causes 4 damage')


def test_comment_attack_outfights_pokemon():
    simulator = Simulator(mode['against_player'])
    pok1 = Pokemon.get_all_pokemons()[25]
    pok2 = Pokemon.get_all_pokemons()[26]
    player1 = simulator.get_players()[0]
    simulator.add_pokemon(pok1, player1)
    player1.set_current_pokemon(pok1)
    pok2.set_stat('hp', 0)
    simulator._comment(player1, 'attack',
                       enemy_pokemon=pok2,
                       attack_type='normal attack',
                       damage=4)
    assert player1.get_comment() == f'{pok1} outfights {pok2} causing 4'
