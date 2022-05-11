from random import randint
from ..config import pokemon_config
import json
import requests


class ImageRequestError(Exception):
    def __init__(self):
        super().__init__('Can\'t get the image content from api')


class EmptyPokemonNameError(Exception):
    def __init__(self):
        super().__init__('Pokemon\'s name can\'t be empty')


class EmptyPokemonDataError(Exception):
    def __init__(self):
        super().__init__('Init data of Pokemon instance can\'t be empty')


class PokemonAlreadyLeftFightError(Exception):
    def __init__(self, pokemon):
        super().__init__(f'{pokemon} already left fight')


class PokemonsDataFileNotFoundError(Exception):
    def __init__(self, path):
        super().__init__(f'File {path} was not found')


class Pokemon:
    """
        Pokemon Class represents battle unit used by player

        :param data: contains all nesessery pokemon stats
        (name, attack, defense etc.)
        :type data: dictionary
    """

    def __init__(self, data):
        """Constructor method"""
        if not data:
            raise EmptyPokemonDataError()
        if not data.get('name'):
            raise EmptyPokemonNameError()
        self._data = data
        self._url = pokemon_config['pokemons_api'].format(
                name=self.get_name().lower()
            )
        self._image_content = None

    @staticmethod
    def get_all_pokemons(path=None):
        """
        Static method, returns a list of :class:`Pokemon` objects

        :param path: path to pokemons json data file
        :type path: str, optional

        :return: list of :class:`Pokemon` objects
        :rtype: list
        """
        return [Pokemon(data) for data in Pokemon.get_pokemons_data(path)]

    @staticmethod
    def get_pokemon_by_name(name, path=None):
        """
        Static method, returns a Pokemon instance found by its name stat

        :param name: name of the pokemon to be found
        :type name: str

        :param path: path to pokemons json data file
        :type path: str, optional

        :return: :class:`Pokemon` object
        :rtype: Pokemon
        """
        pokemons_found = Pokemon.get_pokemons_by_name(name, path)
        if pokemons_found:
            return pokemons_found[0]

    @staticmethod
    def get_pokemons_by_name(name, path=None):
        """
        Static method, returns a list of :class:`Pokemon`
        objects containing name value in their names

        :param name: name of the pokemons to be found
        :type name: str

        :param path: path to pokemons json data file
        :type path: str, optional

        :return: list of :class:`Pokemon` objects
        :rtype: list
        """
        pokemons_data = Pokemon.get_pokemons_data(path)
        return [
                Pokemon(d) for d in pokemons_data
                if name in d.get('name')
            ]

    @staticmethod
    def get_pokemons_data(path=None):
        """
        Static method, returns a list of dictionaries containing pokemons data

        :param path: path to pokemons json data file
        :type path: str, optional

        :return: list of dictionaries with pokemons data
        :rtype: list
        """
        path = pokemon_config['data_path'] if path is None else path
        try:
            with open(path, 'r', encoding='utf8') as file:
                text = file.read()
                data = json.loads(text)
                return data
        except FileNotFoundError:
            raise PokemonsDataFileNotFoundError(path)

    @staticmethod
    def count_special_damage(attack_pok, def_pok, type):
        """
        Static method, returns damage done by pokemon's special attack

        :param attack_pok: attacking pokemon
        :type attack_pok: Pokemon

        :param def_pok: pokemon taking damage
        :type def_pok: Pokemon

        :return: damage done by pokemon
        :rtype: int
        """
        if type == 'fighting':
            type = 'fight'
        type_modifier = def_pok.get_stat(f'against_{type}')
        base_damage = Pokemon.count_normal_damage(attack_pok, def_pok)
        damage = base_damage*type_modifier
        return int(damage)

    @staticmethod
    def count_normal_damage(attack_pok, def_pok):
        """
        Static method, returns damage done by pokemon's normal attack

        :param attack_pok: attacking pokemon
        :type attack_pok: Pokemon

        :param def_pok: pokemon taking damage
        :type def_pok: Pokemon

        :return: damage done by pokemon
        :rtype: int
        """
        def critical(pokemon):
            threshold = pokemon.get_stat('speed')/2
            rnd = randint(0, 255)
            if rnd < threshold:
                return 1.8
            else:
                return 1

        def random():
            mod = randint(85, 100)/100
            return mod

        modifiers = critical(attack_pok)*random()
        base_damage = (attack_pok.get_stat('attack') /
                       def_pok.get_stat('defense') + 2)
        damage = base_damage*modifiers
        return (int(damage) or 1)

    def get_name(self):
        """
        Return the name of pokemon
        :rtype: str
        """
        return self._data['name']

    def is_alive(self):
        """
        Returns whether pokemon is alive or not
        :rtype: bool
        """
        return self.get_stat('hp') > 0

    def get_stat(self, stat):
        """
        Returns stat of pokemon

        :param stat: name of stat
        :type stat: str

        :rtype: float
        """
        return float(self._data[stat])

    def set_stat(self, stat, value):
        """
        Sets value of pokemon's stat

        :param stat: name of stat
        :type stat: str

        :param value: value of stat to be set
        :type value: int

        :rtype: float
        """
        self._data[stat] = int(value)

    def get_types(self):
        """
        Returns types of pokemon

        :return: returns tuple of pokemon's types
        :rtype: tuple
        """
        return (self._data['type1'], self._data['type2'])

    def take_damage(self, damage):
        """
        Reduces the hp stat by damage done to pokemon

        :param damage: damage done to pokemon
        :type damage: int
        """
        if not self.is_alive():
            raise PokemonAlreadyLeftFightError(self)
        hp = self.get_stat('hp') - damage
        self.set_stat('hp', max(hp, 0))

    def get_image_content(self):
        """
        Returns pokemon's image data
        :return: pokemon's image data gotten from pokemon's api
        :rtype: bytes
        """
        try:
            if self._image_content is not None:
                return self._image_content
            data = requests.get(self._url).json()
            img_url = data['sprites']['other']
            img_url = img_url['official-artwork']['front_default']
            self._image_content = requests.get(img_url).content
            return self._image_content
        except Exception:
            raise ImageRequestError()

    def __str__(self):
        return self.get_name()

    def __eq__(self, obj):
        return obj == self.get_name()
