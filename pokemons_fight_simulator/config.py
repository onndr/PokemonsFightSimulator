pokemon_config = {
    'pokemons_api': 'https://pokeapi.co/api/v2/pokemon/{name}',
    'data_path': 'pokemons_fight_simulator/pokemon_data.json'
}

mode = {
    'against_player': 'plvspl',
    'against_computer': 'plvscomp'
}

gui_config = {
    'sounds': {
        'path': './pokemons_fight_simulator/sounds/{}',
        'main_theme': 'main_theme.mp3',
        'combat': 'battle_music.mp3'
    },
    'pages': {
        'start_page': 0,
        'configuration_page': 1,
        'configure_player_page': 2,
        'fight_page': 3
    }
}
