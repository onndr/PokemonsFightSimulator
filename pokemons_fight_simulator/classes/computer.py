from .player import Player
from .move import Move
import random


class Computer(Player):
    """
    Class representing 'computer' player

    :param name: name of player, defaults to Player
    :type name: str, optional
    """
    def __init__(self, name='Super powerful AI'):
        """Constructor method"""
        super().__init__(name=name)

    def generate_random_team(self, list_of_pokemons, pokemons_number):
        """
        Sets given number of randomly chosen pokemons from given pokemons list
        Returns list with those pokemons
        :rtype: list
        """
        self._pokemons = random.choices(list_of_pokemons, k=pokemons_number)
        return self._pokemons

    def get_alive_pokemons(self):
        """
        Returns all computer's pokemons that are alive
        :rtype: list
        """
        return [pok for pok in self._pokemons if pok.is_alive()]

    def set_random_move(self, moves):
        """Sets randomly chosen move from given move types list"""
        random_move = random.choice(moves)
        random_pokemon = random_type = None
        if random_move == 'switch':
            random_pokemon = random.choice(self.get_alive_pokemons())
        if random_move == 'special attack':
            while not random_type:
                random_type = random.choice(self._current_pokemon.get_types())
        move = Move(random_move, random_pokemon, random_type)
        self.set_move(move)
