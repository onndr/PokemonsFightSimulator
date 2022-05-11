from ..pokemons_fight_simulator.classes.computer import Computer
from ..pokemons_fight_simulator.classes.simulator import Simulator


def test_create():
    comp = Computer()
    assert comp.get_pokemons() == []


def test_generate_random_team(monkeypatch):
    pokemons = Simulator().get_available_pokemons()

    def mock(a, k):
        return pokemons[:k]
    path = 'pokemon.pokemons_fight_simulator.classes.computer.random.choices'
    monkeypatch.setattr(path, mock)
    comp = Computer()
    comp.generate_random_team(pokemons, 20)
    assert comp.get_pokemons() == pokemons[:20]


def test_get_alive_pokemons():
    comp = Computer()
    simulator = Simulator()
    pokemons = simulator.get_available_pokemons()
    pok1, pok2 = pokemons[0], pokemons[1]
    comp.add_pokemon(pok1)
    comp.add_pokemon(pok2)
    assert pok1, pok2 in comp.get_alive_pokemons()
    pok1.set_stat('hp', 0)
    assert pok1 not in comp.get_alive_pokemons()
    assert pok2 in comp.get_alive_pokemons()


def test_set_random_move(monkeypatch):
    comp = Computer()

    def mock(a):
        return 'defense'
    path = 'pokemon.pokemons_fight_simulator.classes.computer.random.choice'
    monkeypatch.setattr(path, mock)
    comp.set_random_move(['switch', 'normal attack', 'defense'])
    assert comp.get_move().move_type == 'defense'
