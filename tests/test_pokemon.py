from ..pokemons_fight_simulator.classes.pokemon import (
    ImageRequestError,
    Pokemon,
    PokemonsDataFileNotFoundError,
    EmptyPokemonDataError,
    EmptyPokemonNameError,
    PokemonAlreadyLeftFightError
)
import pytest


def test_get_pokemons_data_invalid_path():
    path = 'random/path/pokemons.json'
    with pytest.raises(PokemonsDataFileNotFoundError):
        Pokemon.get_pokemons_data(path)


def test_get_all_pokemons():
    pokemons = Pokemon.get_all_pokemons()
    assert len(pokemons) > 0


def test_get_pokemon_by_name():
    pokemon = Pokemon.get_all_pokemons()[10]
    pokemon_name = pokemon.get_name()
    found_pokemon = Pokemon.get_pokemon_by_name(pokemon_name)
    assert pokemon == found_pokemon
    name = 'abra-kadabra'
    found_pokemon = Pokemon.get_pokemon_by_name(name)
    assert found_pokemon is None


def test_get_image():
    pokemon = Pokemon.get_all_pokemons()[0]
    content = pokemon.get_image_content()
    assert content


def test_get_image_wrong_url():
    pokemon = Pokemon.get_all_pokemons()[0]
    pokemon._url = 'https://pokemons.abrakadabra'
    with pytest.raises(ImageRequestError):
        pokemon.get_image_content()


def test_count_damage_normal(monkeypatch):
    def f(x, y):
        return 90
    mocked = 'pokemon.pokemons_fight_simulator.classes.pokemon.randint'
    monkeypatch.setattr(mocked, f)
    pokemon1 = Pokemon({'name': 'Pok1', 'hp': 30, 'attack': 150, 'speed': 182})
    pokemon2 = Pokemon({'name': 'Pok2', 'hp': 30, 'defense': 10})
    damage = Pokemon.count_normal_damage(pokemon1, pokemon2)
    assert damage == 27


def test_count_damage_special(monkeypatch):
    def f(x, y):
        return 90
    mocked = 'pokemon.pokemons_fight_simulator.classes.pokemon.randint'
    monkeypatch.setattr(mocked, f)
    pokemon1 = Pokemon({'name': 'Pok1', 'hp': 30, 'attack': 150, 'speed': 182,
                        'type1': 'water', 'type2': 'rock'})
    pokemon2 = Pokemon({'name': 'Pok2', 'hp': 30, 'defense': 10,
                        'against_water': 0.85, 'against_rock': 1.5})
    damage = Pokemon.count_special_damage(pokemon1, pokemon2,
                                          pokemon1._data['type2'])
    assert damage == 40


def test_create():
    data = {'name': 'Pikachu', 'hp': '100'}
    pokemon = Pokemon(data)
    assert pokemon.get_name() == data['name']
    assert pokemon.get_stat('hp') == 100


def test_create_empty_data():
    with pytest.raises(EmptyPokemonDataError):
        Pokemon({})


def test_create_empty_name():
    data = {'type1': 'Snow'}
    with pytest.raises(EmptyPokemonNameError):
        Pokemon(data)


def test_set_stat():
    data = {'name': 'Pikachu', 'defense': '100'}
    pokemon = Pokemon(data)
    assert pokemon.get_name() == data['name']
    assert pokemon.get_stat('defense') == 100
    pokemon.set_stat('defense', 20)
    assert pokemon.get_stat('defense') == 20


def test_get_types():
    data = {'name': 'Name', 'type1': 'Water', 'type2': ''}
    pokemon = Pokemon(data)
    assert pokemon.get_types() == ('Water', '')


def test_take_damage():
    pokemon = Pokemon({'name': 'Pok', 'hp': 100})
    pokemon.take_damage(33)
    assert pokemon.get_stat('hp') == 67


def test_take_damage_left_fight():
    pokemon = Pokemon({'name': 'Pok', 'hp': 0})
    with pytest.raises(PokemonAlreadyLeftFightError):
        pokemon.take_damage(33)


def test_take_zero_hitpoints():
    pokemon = Pokemon({'name': 'Pok', 'hp': 12})
    pokemon.take_damage(60)
    assert pokemon.is_alive() is False
    assert pokemon.get_stat('hp') == 0
