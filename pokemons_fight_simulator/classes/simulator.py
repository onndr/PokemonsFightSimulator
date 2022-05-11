from .player import Player
from .computer import Computer
from .pokemon import Pokemon
from .move import Move
from .. import config


class PlayerIsNotSetToSimulatorError(Exception):
    def __init__(self):
        super().__init__('Player is not set to simulator')


class Simulator:
    """
    Simulator Class, contains main game logic
    """
    def __init__(self, mode=None):
        """Constructor method"""
        self.reset(mode)

    def reset(self, mode):
        """
        Resets all simulator fields to default values
        """
        self._first_player = Player()
        self._second_player = Player()
        self._computer = Computer()
        self._available_pokemons = Pokemon.get_all_pokemons()
        self._current_player = None
        self._current_round = 1
        self._mode = mode

    def generate_computer_pokemons(self, pokemons_number=None):
        """
        Calls computer's generate_random_team method
        giving list with available pokemons and
        number of pokemons as a parametre
        Returns generated pokemons list
        :rtype: list
        """
        n = pokemons_number or self._max_team_size
        return self._computer.generate_random_team(self._available_pokemons, n)

    def set_mode(self, mode):
        """
        Sets the mode of game
        Can be vs player or vs computer
        """
        self._mode = mode

    def get_mode(self):
        """
        Returns game mode
        :rtype: string
        """
        return self._mode

    def set_max_team_size(self, n):
        """Sets maximum number of pokemons that can be chosen by players"""
        self._max_team_size = n

    def get_max_team_size(self):
        """
        Returns maximum number of pokemons that can be chosen by players
        :rtype: int
        """
        return self._max_team_size

    def get_players(self):
        """
        Returns fighting players
        :return: tuple of :class:`Player` objects
        :rtype: tuple
        """
        if self._mode == config.mode['against_computer']:
            return self._first_player, self._computer
        elif self._mode == config.mode['against_player']:
            return self._first_player, self._second_player

    def set_current_player(self, player):
        """
        Sets current active player, must be one of players in simulator
        :param player: object of :class:`Player` to be set as current active
        :type player: Player
        """
        if player not in self.get_players():
            raise PlayerIsNotSetToSimulatorError()
        self._current_player = player

    def set_first_player(self, new_player):
        """
        Sets first player
        :param new_player: player to be set as first
        :type new_player: Player
        """
        self._first_player = new_player

    def set_second_player(self, new_player):
        """
        Sets second player
        :param new_player: player to be set as second
        :type new_player: Player
        """
        self._second_player = new_player

    def get_current_player(self):
        """
        Returns current active player
        :rtype: Player
        """
        return self._current_player

    def get_current_player_pokemons(self):
        """
        Returns pokemons of current active player
        :return: list of :class:`Pokemon` objects
        :rtype: list
        """
        return self._current_player.get_pokemons()

    def add_pokemon(self, pokemon, player=None):
        """
        Adds pokemon to player's team, by default to the current player,
        but player to whose team pokemon should be added can also be specified

        :param pokemon: pokemon of :class:`Pokemon` to be added to
        player's team
        :type pokemon: Pokemon

        :param player: player to whose team pokemon should be added,
        defaults to None
        :type player: Player
        """
        if self._current_player is None and player is None:
            return
        if self._current_player is not None:
            player = self._current_player
        if pokemon in self._available_pokemons:
            player.add_pokemon(pokemon)
            self._available_pokemons.remove(pokemon)

    def remove_pokemon(self, pokemon, player=None):
        """
        Removes pokemon from player's team, by default from the current player,
        but player from whose team pokemon should be added
        can also be specified

        :param pokemon: pokemon of :class:`Pokemon` to be removed
        from player's team
        :type pokemon: Pokemon

        :param player: player from whose team pokemon should be removed,
        defaults to None
        :type player: Player
        """
        if self._current_player is None and player is None:
            return
        if self._current_player is not None:
            player = self._current_player
        if pokemon in player.get_pokemons():
            player.remove_pokemon(pokemon)
            self._available_pokemons.append(pokemon)

    def get_available_pokemons(self):
        """
        Returns pokemons that are still available for adding
        to some player's team
        :return: list of :class:`Pokemon` objects
        :rtype: list
        """
        return self._available_pokemons

    def get_rounds(self):
        """
        Returns current round of fight
        :rtype: int
        """
        return self._current_round

    def _comment(self, player, move_type, **kwargs):
        """
        Comments the move of player and sets the comment to player

        :param player: player whose move must be commented
        :type plyer: Player

        :param move_type: type of player's move
        :type move_type: str

        :param **kwargs: additional parametres of player's move
        """
        pokemon = player.get_current_pokemon()
        match move_type:
            case 'defense':
                value = kwargs['value']
                text = f'{pokemon} increases his defense by {value}'
            case 'switch':
                new_pokemon = kwargs['new_pokemon']
                text = f'{player} switches {pokemon} to {new_pokemon}'
            case 'skip':
                text = f'{player} skips this round!'
            case 'attack':
                enemy_pokemon = kwargs['enemy_pokemon']
                attack_type = kwargs['attack_type']
                damage = kwargs['damage']
                is_enemy_alive = enemy_pokemon.is_alive()
                text = (f'{pokemon} hits {enemy_pokemon} with {attack_type}' +
                        f' \nand causes {damage} damage')
                if not is_enemy_alive:
                    text = (f'{pokemon} outfights {enemy_pokemon}' +
                            f' causing {damage}')
            case _:
                text = ''
        player.set_comment(text)

    def round(self):
        """
        Performs round of moves
        Firstly non-attack moves are done,
        then attacks by speed order
        """
        player1, player2 = self.get_players()
        if not self._is_ready_to_round():
            return False
        else:
            result1, result2 = self._do_both_players_moves()
            damage1, attack_type1 = result1
            damage2, attack_type2 = result2

            self._hit_by_speed(player1, damage1, attack_type1,
                               player2, damage2, attack_type2)
            self._current_round += 1
            return True

    def _set_computer_random_move(self):
        """Makes computer choose random move"""
        self._computer.set_random_move(
                [t for t in Move.move_types if not t == 'skip'])

    def _is_ready_to_round(self):
        """Returns whether moves of both players are defined"""
        player1, player2 = self.get_players()
        if self._mode == config.mode['against_computer']:
            self._set_computer_random_move()
        if not player1.get_move() or not player2.get_move():
            return False
        return True

    def _hit_by_speed(self,
                      player1, damage1, attack_type1,
                      player2, damage2, attack_type2):
        """
        Pokemons become hit by their speed stat
        First attacks that pokemon with higher speed stat
        """
        pokemon1 = player1.get_current_pokemon()
        pokemon2 = player2.get_current_pokemon()
        speed1, speed2 = pokemon1.get_stat('speed'), pokemon2.get_stat('speed')

        if speed1 >= speed2:
            if pokemon1.is_alive() and damage1:
                self._hit_and_comment(player1, player2, damage1, attack_type1)
            if pokemon2.is_alive() and damage2:
                self._hit_and_comment(player2, player1, damage2, attack_type2)
        else:
            if pokemon2.is_alive() and damage2:
                self._hit_and_comment(player2, player1, damage2, attack_type2)
            if pokemon1.is_alive() and damage1:
                self._hit_and_comment(player1, player2, damage1, attack_type1)

    def _hit_and_comment(self, attacking_player, enemy_player,
                         damage, attack_type):
        """Makes pokemon of enemy take damage and comments the attack move"""
        enemy_pokemon = enemy_player.get_current_pokemon()
        enemy_pokemon.take_damage(damage)
        self._comment(attacking_player, 'attack',
                      enemy_pokemon=enemy_pokemon,
                      attack_type=attack_type,
                      damage=damage)

    def _do_both_players_moves(self):
        """
        Performs moves of both players
        Then sets players' moves to None
        Returns results of moves
        """
        player1, player2 = self.get_players()
        result1 = self._perform_move(player1, player2)
        result2 = self._perform_move(player2, player1)
        player1.set_move(None), player2.set_move(None)
        return result1, result2

    def _perform_move(self, moving_player, enemy_player):
        """
        Handles moves of players in a defined sequence:
        Moves have their priorities
        Defense and switch have first priority,
        while attack always has second priority.
        So here is only damage calculated and returned if move is an attack
        """
        move = moving_player.get_move()
        moving_pokemon = moving_player.get_current_pokemon()
        enemy_pokemon = enemy_player.get_current_pokemon()
        non_attack_result = None, None
        match move.move_type:
            case 'defense':
                defense = moving_pokemon.get_stat('defense')
                new_defense = int(1.1*defense)
                def_increase = int(new_defense - defense)
                moving_pokemon.set_stat('defense', new_defense)
                self._comment(moving_player, move.move_type,
                              value=def_increase)
                return non_attack_result
            case 'switch':
                self._comment(moving_player, move.move_type,
                              new_pokemon=move.pokemon_to_set)
                moving_player.set_current_pokemon(move.pokemon_to_set)
                return non_attack_result
            case 'normal attack':
                damage = Pokemon.count_normal_damage(moving_pokemon,
                                                     enemy_pokemon)
                return damage, move.move_type
            case 'special attack':
                damage = Pokemon.count_special_damage(moving_pokemon,
                                                      enemy_pokemon,
                                                      move.special_attack_type)
                return damage, move.move_type
            case 'skip':
                self._comment(moving_player, move.move_type)
                return non_attack_result
            case _:
                raise ValueError('Move is not properly defined')
