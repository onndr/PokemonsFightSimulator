from ..pokemons_fight_simulator.classes.pokemon import Pokemon
from ..pokemons_fight_simulator.classes.player import (
    Player,
    PokemonAlreadyInTeamError,
    NoSuchPokemonInTeamError,
    PokemonOutOfFightError
)
from ..pokemons_fight_simulator.classes.move import Move
import pytest


def test_create():
    player = Player('Name')
    assert player.get_name() == 'Name'
    assert player.get_pokemons() == []
    assert player.get_move() is None
    assert player.get_current_pokemon() is None


def test_set_name():
    player = Player('Name')
    assert player.get_name() == 'Name'
    player.set_name('New name')
    assert player.get_name() == 'New name'


def test_add_pokemon():
    player = Player('Name')
    pokemon = Pokemon({'name': 'Pok1'})
    player.add_pokemon(pokemon)
    assert player.get_pokemons()[0] == pokemon
    assert len(player.get_pokemons()) == 1
    pokemon = Pokemon({'name': 'Pok2'})
    player.add_pokemon(pokemon)
    assert player.get_pokemons()[1] == pokemon
    assert len(player.get_pokemons()) == 2


def test_add_pokemon_already_in_team():
    player = Player('Name')
    pokemon = Pokemon({'name': 'Pok'})
    player.add_pokemon(pokemon)
    with pytest.raises(PokemonAlreadyInTeamError):
        player.add_pokemon(pokemon)


def test_remove_pokemon():
    player = Player('Name')
    pokemon1 = Pokemon({'name': 'Pok1'})
    pokemon2 = Pokemon({'name': 'Pok2'})
    player.add_pokemon(pokemon1)
    player.add_pokemon(pokemon2)
    player.remove_pokemon(pokemon1)
    assert pokemon1 not in player.get_pokemons()
    assert pokemon2 in player.get_pokemons()
    assert len(player.get_pokemons()) == 1


def test_remove_pokemon_is_not_in_team():
    player = Player('Name')
    pokemon1 = Pokemon({'name': 'Pok1'})
    pokemon2 = Pokemon({'name': 'Pok2'})
    player.add_pokemon(pokemon1)
    with pytest.raises(NoSuchPokemonInTeamError):
        player.remove_pokemon(pokemon2)


def test_set_current_pokemon():
    player = Player('Name')
    pokemon1 = Pokemon({'name': 'Pok1', 'hp': 1})
    pokemon2 = Pokemon({'name': 'Pok2', 'hp': 1})
    player.add_pokemon(pokemon1)
    player.add_pokemon(pokemon2)
    assert player.get_current_pokemon() is None
    player.set_current_pokemon(pokemon2)
    assert player.get_current_pokemon() == pokemon2


def test_set_current_pokemon_is_not_alive():
    player = Player('Name')
    pokemon1 = Pokemon({'name': 'Pok1', 'hp': 1})
    pokemon2 = Pokemon({'name': 'Pok2', 'hp': 1})
    player.add_pokemon(pokemon1)
    player.add_pokemon(pokemon2)
    pokemon2.set_stat('hp', 0)
    with pytest.raises(PokemonOutOfFightError):
        player.set_current_pokemon(pokemon2)


def test_set_move():
    player = Player('Name')
    move = Move('normal attack')
    assert player.get_move() is None
    player.set_move(move)
    assert player.get_move() == move


def test_set_comment():
    player = Player('Name')
    comment = 'Player has won the battle'
    player.set_comment(comment)
    assert player.get_comment() == comment


def test_current_pokemon_alive():
    player = Player('Name')
    pokemon1 = Pokemon({'name': 'Pok1', 'hp': 1})
    player.add_pokemon(pokemon1)
    player.set_current_pokemon(pokemon1)
    assert player.is_current_pokemon_alive() is True
    pokemon1.set_stat('hp', 0)
    assert player.is_current_pokemon_alive() is False


def test_are_all_pokemons_dead():
    player = Player('Name')
    pokemon1 = Pokemon({'name': 'Pok1', 'hp': 1})
    pokemon2 = Pokemon({'name': 'Pok2', 'hp': 0})
    player.add_pokemon(pokemon1)
    player.add_pokemon(pokemon2)
    assert player.are_all_pokemons_dead() is False
    pokemon1.set_stat('hp', 0)
    assert player.are_all_pokemons_dead() is True
