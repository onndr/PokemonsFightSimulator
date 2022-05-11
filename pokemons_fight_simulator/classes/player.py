class PokemonAlreadyInTeamError(Exception):
    def __init__(self, pokemon, player):
        super().__init__(f'Pokemon {pokemon} is already in {player}\'s team')


class NoSuchPokemonInTeamError(Exception):
    def __init__(self, pokemon, player):
        super().__init__(f'There is no {pokemon} in {player}\'s team')


class PokemonOutOfFightError(Exception):
    def __init__(self, pokemon, player):
        super().__init__(f'{pokemon} of {player} can\'t fight anymore')


class Player:
    """
    Class representing player

    :param name: name of player, defaults to Player
    :type name: str, optional
    """
    def __init__(self, name='Player'):
        """Constructor method"""
        self._name = name
        self._pokemons = []
        self._current_pokemon = None
        self._move = None
        self._comment = ''

    def are_all_pokemons_dead(self):
        """
        Returns if all player's pokemons are dead
        :rtype: bool
        """
        return not any(pokemon.is_alive() for pokemon in self._pokemons)

    def is_current_pokemon_alive(self):
        """
        Returns if the current player's pokemon alive
        :rtype: bool
        """
        return self._current_pokemon.is_alive()

    def get_name(self):
        """
        Returns the name of player
        :rtype: str
        """
        return self._name

    def set_name(self, new_name):
        """
        Setter of player's name
        :param new_name: name to set
        :type new_name: str
        """
        self._name = new_name

    def get_pokemons(self):
        """
        Returns player's pokemons
        :return: list of :class:`Pokemon` objects
        :rtype: list
        """
        return self._pokemons

    def add_pokemon(self, pokemon):
        """
        Adds pokemon to player's team
        :param pokemon: pokemon to be added
        :type pokemon: Pokemon
        """
        if pokemon in self._pokemons:
            raise PokemonAlreadyInTeamError(pokemon, self)
        self._pokemons.append(pokemon)

    def remove_pokemon(self, pokemon):
        """
        Removes pokemon from player's team
        :param pokemon: pokemon to be removed
        :type pokemon: Pokemon
        """
        if pokemon not in self._pokemons:
            raise NoSuchPokemonInTeamError(pokemon, self)
        self._pokemons.remove(pokemon)

    def get_move(self):
        """
        Returns current move of the player
        :rtype: Move
        """
        return self._move

    def set_move(self, move):
        """
        Sets player's current move
        :param move: move to be set
        :type move: Move
        """
        self._move = move

    def get_current_pokemon(self):
        """
        Returns current active pokemon of player
        :rtype: Pokemon
        """
        if self._pokemons == []:
            return None
        return self._current_pokemon

    def set_current_pokemon(self, pokemon):
        """
        Sets current active pokemon of player
        :param pokemon: pokemon from player's team to be active
        :type pokemon: Pokemon
        """
        if pokemon not in self._pokemons:
            raise NoSuchPokemonInTeamError(pokemon, self)
        if not pokemon.is_alive():
            raise PokemonOutOfFightError(pokemon, self)
        self._current_pokemon = pokemon

    def set_comment(self, comment):
        """
        Sets comment of last player's move
        :param comment: comment to be set
        :type comment: str
        """
        self._comment = comment

    def get_comment(self):
        """
        Returns comment of last player's move
        :rtype: str
        """
        return self._comment

    def __str__(self) -> str:
        return self._name
