class EmptyMoveError(Exception):
    def __init__(self):
        super().__init__('Move can\'t be empty')


class SwitchToNoneMoveError(Exception):
    def __init__(self):
        super().__init__('Can\'t switch to None')


class InvalidMoveValueError(Exception):
    def __init__(self):
        super().__init__('Invalid move value')


class SpecialAttackTypeNotSpecifiedError(Exception):
    def __init__(self):
        super().__init__('Special attack must have a pokemon type')


class Move:
    """
    Class representation of player's move

    :param move_type: type of move, must be from Move.move_types
    :type move_type: str

    :param pokemon_to_set: pokemon instance, specified in case when
    player wants to switch current his pokemon
    :type pokemon_to_set: Pokemon, optional(essential with move_type='switch')
    """
    move_types = ['normal attack', 'special attack',
                  'defense', 'switch', 'skip']

    def __init__(self, move_type,
                 pokemon_to_set=None,
                 special_attack_type=None):
        """Constructor method"""
        if move_type == '':
            raise EmptyMoveError()
        if move_type not in Move.move_types:
            raise InvalidMoveValueError()
        if move_type == 'switch' and pokemon_to_set is None:
            raise SwitchToNoneMoveError()
        if move_type == 'special attack' and special_attack_type is None:
            raise SpecialAttackTypeNotSpecifiedError()
        self.move_type = move_type
        self.pokemon_to_set = pokemon_to_set
        self.special_attack_type = special_attack_type
