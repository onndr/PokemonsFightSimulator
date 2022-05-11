from ..pokemons_fight_simulator.classes.move import (
    EmptyMoveError,
    InvalidMoveValueError,
    Move,
    SwitchToNoneMoveError,
    SpecialAttackTypeNotSpecifiedError
)
from ..pokemons_fight_simulator.classes.pokemon import (
    Pokemon
)
import pytest


def test_create():
    pokemon = Pokemon({'name': 'Pok'})
    move = Move('switch', pokemon)
    assert move.move_type == 'switch'
    assert move.pokemon_to_set == pokemon


def test_create_switch_no_pokemon():
    with pytest.raises(SwitchToNoneMoveError):
        Move('switch')


def test_create_empty_move():
    with pytest.raises(EmptyMoveError):
        Move('')


def test_create_invalid_move():
    with pytest.raises(InvalidMoveValueError):
        Move('attack_twice')


def test_create_special_attack_move_not_type():
    with pytest.raises(SpecialAttackTypeNotSpecifiedError):
        Move('special attack')
