from PySide6.QtWidgets import (
    QApplication, QListWidgetItem, QMainWindow)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from .classes.move import Move
from .classes.simulator import Simulator
from .ui_main import Ui_mainWindow
from .config import gui_config, mode


class LoadImageError(Exception):
    def __init__(self):
        super().__init__('Can\'t load image')


def connect_signals(ui, window):
    buttons = {
        ui.buttonPlayerVsPlayer: lambda:
            window._go_configuration_page(
                mode['against_player']),
        ui.buttonPlayerVsComputer: lambda:
            window._go_configuration_page(
                mode['against_computer']),
        ui.buttonConfigureFirstPlayer: lambda:
            window._go_configure_player_page(window._first_player),
        ui.buttonConfigureSecondPlayer: lambda:
            window._go_configure_player_page(window._second_player),
        ui.buttonDefense1: lambda: window._move(
            window._first_player, 'defense'),
        ui.buttonDefense2: lambda: window._move(
            window._second_player, 'defense'),
        ui.buttonNormalAttack1: lambda: window._move(
            window._first_player, 'normal attack'),
        ui.buttonNormalAttack2: lambda: window._move(
            window._second_player, 'normal attack'),
        ui.buttonSpecialAttack1: lambda:
            window._show_pokemon_special_attack_type_menu(
                window._first_player),
        ui.buttonSpecialAttack2: lambda:
            window._show_pokemon_special_attack_type_menu(
                window._second_player),
        ui.buttonStartGameVsPlayer: window._go_fight_player_page,
        ui.buttonBack1: window._go_start_page,
        ui.buttonBack2: window._go_last_page,
        ui.buttonEndFight: window._go_start_page,
    }
    lists = {
        ui.pokemonsList1: lambda item: window._move(
            window._first_player, 'switch', pokemon_to_set=item.pokemon),
        ui.pokemonsList2: lambda item: window._move(
            window._second_player, 'switch', pokemon_to_set=item.pokemon),
        ui.availablePokemonsList: window._add_pokemon_configure_page,
        ui.chosenPokemonsList: window._remove_pokemon_configure_page,
        ui.typesList1: lambda item: window._move(
            window._first_player, 'special attack',
            special_attack_type=item.text()),
        ui.typesList2: lambda item: window._move(
            window._second_player, 'special attack',
            special_attack_type=item.text())
    }
    edits = {
        ui.playerNameEdit: window._set_name,
        ui.findPokemonEdit: window._setup_searched_pokemons
    }
    ui.maxPokemonsSpinbox.valueChanged.connect(window._set_max_team_size)
    for button, handler in buttons.items():
        button.clicked.connect(handler)
    for list, handler in lists.items():
        list.itemClicked.connect(handler)
    for edit, handler in edits.items():
        edit.textChanged.connect(handler)


class PokemonsFightSimulatorWindow(QMainWindow):
    """The only and main window of ui"""
    def __init__(self, parent=None):
        """Constructor"""
        super().__init__(parent)
        self._init_music()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self._simulator = Simulator()
        self._reset()
        self._pages = gui_config.get('pages')
        self._go_start_page()
        self._max_team_size = 1
        connect_signals(self.ui, self)

    def _get_music_file(self, name):
        """Returns path to music file"""
        filename = gui_config['sounds'][name]
        return gui_config['sounds']['path'].format(filename)

    def _init_music(self):
        """Initializes music player at start page and plays theme of Pokemon"""
        self._media_player = QMediaPlayer()
        self._audio_output = QAudioOutput()
        self._media_player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(0.5)
        music_file = self._get_music_file('main_theme')
        self._play_soundtrack(music_file)

    def _set_max_team_size(self, value):
        """Sets the maximum of pokemons of player"""
        self._max_team_size = value
        self._simulator.set_max_team_size(value)

    def _go_start_page(self):
        """Basically ressets the whole game"""
        self._go_to_page(self._pages['start_page'])
        self._reset()

    def _reset(self):
        """Goes to default start values"""
        self._previous_pages = []
        filename = gui_config['sounds']['main_theme']
        if not self._media_player.source().fileName() == filename:
            theme_music_file = self._get_music_file('main_theme')
            self._play_soundtrack(theme_music_file)

    def _set_widgets_to_players(self):
        """Sets widgets to players so that it could easier to access them"""
        self._first_player.widgets = {
            'buttons': {
                self.ui.buttonDefense1,
                self.ui.buttonNormalAttack1,
                self.ui.buttonSpecialAttack1
                },
            'pokemons_list': self.ui.pokemonsList1,
            'comment_label': self.ui.commentPlayer1,
            'choose_type_label': self.ui.chooseSpecialTypeLabel1,
            'special_attack_types': self.ui.typesList1
        }
        self._second_player.widgets = {
            'buttons': {
                self.ui.buttonDefense2,
                self.ui.buttonNormalAttack2,
                self.ui.buttonSpecialAttack2
                },
            'pokemons_list': self.ui.pokemonsList2,
            'comment_label': self.ui.commentPlayer2,
            'choose_type_label': self.ui.chooseSpecialTypeLabel2,
            'special_attack_types': self.ui.typesList2
        }

    def _go_last_page(self):
        """
        Goes to the last saved page, removes its index from last pages list
        """
        last_page_index = self._previous_pages.pop()
        self.ui.stack.setCurrentIndex(last_page_index)

    def _save_page(self):
        """Saves current page index in list as its last item"""
        current_page_index = self.ui.stack.currentIndex()
        self._previous_pages.append(current_page_index)

    def _go_to_page(self, index):
        """Goes to the page with given index"""
        self._save_page()
        self.ui.stack.setCurrentIndex(index)

    def _set_enabled_widgets(self, player, value):
        """Enables or disables widgets of player by value"""
        for button in player.widgets['buttons']:
            button.setEnabled(value)
        player.widgets['pokemons_list'].setEnabled(value)

    def _move(self, player, move, **kwargs):
        """
        Sets move to the player,
        disables his widgets and tries to perform round
        """
        pokemon_to_set = kwargs.get('pokemon_to_set')
        special_attack_type = kwargs.get('special_attack_type')
        if pokemon_to_set and not pokemon_to_set.is_alive():
            return
        player.set_move(Move(move, pokemon_to_set, special_attack_type))
        self._set_enabled_widgets(player, False)
        self._round()

    def _show_pokemon_special_attack_type_menu(self, player):
        types_list = player.widgets['special_attack_types']
        types_list.clear()
        pokemon = player.get_current_pokemon()
        types = pokemon.get_types()
        [QListWidgetItem(type, types_list) for type in types if type]
        player.widgets['choose_type_label'].show()
        types_list.show()

    def _round(self):
        """
        if game in 'computer' mode, calls function setting his random move
        If moves of players are defined, round in simulator can be performed
        Enables widgets of player, if player is not computer
        Refreshes the page with new data after round
        Checks if players' pokemons are alive
        """
        round_success = self._simulator.round()
        if round_success:
            self._set_enabled_widgets(self._first_player, True)
            if self._mode == mode['against_player']:
                self._set_enabled_widgets(self._second_player, True)
            self._setup_fight_page()
            self._do_for_both_players(self._check_alive)

    def _check_alive(self, player, *args):
        """Checks the state of pokemons of given player"""
        if not player.is_current_pokemon_alive():
            if player.are_all_pokemons_dead():
                self._player_lose_message(player)
            else:
                self._current_pokemon_died(player)

    def _current_pokemon_died(self, player_to_change_pokemon):
        """
        Services the case when an active pokemon of given player is dead
        Shows the text saying that player has to change pokemon
        The other player's widgets are disabled, he skips the round
        Player whose pokemon is dead can choose next pokemon from list
        """
        self._set_enabled_widgets(self._second_player, False)
        self._set_enabled_widgets(self._first_player, False)
        text = ('Your pokemon can\'t fight anymore,' +
                '\nyou have to choose another one')
        player_to_change_pokemon.widgets['pokemons_list'].setEnabled(True)
        player_to_change_pokemon.widgets['comment_label'].setText(text)
        if player_to_change_pokemon == self._first_player:
            self._second_player.set_move(Move('skip'))
        elif player_to_change_pokemon == self._second_player:
            self._first_player.set_move(Move('skip'))
            if self._mode == mode['against_computer']:
                self._round()

    def _player_lose_message(self, player):
        """End of fight message"""
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        if player == self._first_player:
            text = (f'{self._second_player} has won! It was fantastic!\n' +
                    f'{player}, better luck next time')
        else:
            text = (f'{self._first_player} has won! It was fantastic!\n' +
                    f'{player}, better luck next time')
        msgBox.setText(text)
        msgBox.setWindowTitle("Congratulations")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.buttonClicked.connect(self._go_start_page)
        msgBox.exec()

    def _set_name(self, value):
        """Sets the name of current player """
        self._simulator.get_current_player().set_name(value)

    def _setup_searched_pokemons(self, text):
        """Sets the list of pokemons found by name search"""
        self.ui.availablePokemonsList.clear()
        searched_pokemons = []
        for pokemon in self._simulator.get_available_pokemons():
            if text.lower() in pokemon.get_name().lower():
                searched_pokemons.append(pokemon)
        self._setup_pokemons_list(searched_pokemons,
                                  self.ui.availablePokemonsList)

    def _go_configuration_page(self, mode):
        """Goes to configuretion page, setting the mode of game"""
        self._mode = mode
        self._simulator.reset(mode)
        self._first_player, self._second_player = self._simulator.get_players()
        self._set_widgets_to_players()
        self._setup_configuration_page()
        self._go_to_page(self._pages['configuration_page'])

    def _setup_configuration_page(self):
        """Changes the label of button depending on game mode"""
        if self._mode == mode['against_player']:
            self.ui.buttonConfigureSecondPlayer.setText('Configure Player2')
        elif self._mode == mode['against_computer']:
            self.ui.buttonConfigureSecondPlayer.setText('Configure Computer')

    def _go_configure_player_page(self, player):
        """Goes to page, where player can configure his pokemons squad"""
        self._simulator.set_current_player(player)
        self._set_configure_page()
        self._go_to_page(self._pages['configure_player_page'])

    def _set_configure_page(self):
        """Sets the configure page with available and chosen pokemons lists"""
        self._setup_available_pokemons_configure_page()
        self._setup_chosen_pokemons_configure_page()
        player_name = self._simulator.get_current_player().get_name()
        self.ui.playerNameEdit.setText(player_name)

    def _setup_available_pokemons_configure_page(self):
        """Sets the list with available pokemons to pick"""
        self.ui.availablePokemonsList.clear()
        self.ui.findPokemonEdit.clear()
        pokemons = self._simulator.get_available_pokemons()
        self._setup_pokemons_list(pokemons, self.ui.availablePokemonsList)

    def _setup_chosen_pokemons_configure_page(self):
        """Sets the list with already chosen by player pokemons"""
        self.ui.chosenPokemonsList.clear()
        pokemons = self._simulator.get_current_player_pokemons()
        self._setup_pokemons_list(pokemons, self.ui.chosenPokemonsList)

    def _setup_pokemons_list(self, pokemons, list):
        """Fills the list with items named text as pokemons' names"""
        for pokemon in pokemons:
            item = QListWidgetItem(pokemon.get_name())
            item.pokemon = pokemon
            list.addItem(item)

    def _add_pokemon_configure_page(self, item):
        """Adds pokemon to player's team"""
        pokemons = self._simulator.get_current_player_pokemons()
        if self._max_team_size <= len(pokemons):
            return
        pokemon = item.pokemon
        self._simulator.add_pokemon(pokemon)
        self._delete_list_item(item, item.listWidget())
        self.ui.chosenPokemonsList.addItem(item)

    def _delete_list_item(self, item, list):
        row = list.row(item)
        list.takeItem(row)

    def _remove_pokemon_configure_page(self, item):
        """Removes pokemon from player's team"""
        pokemon = item.pokemon
        self._simulator.remove_pokemon(pokemon)
        self._delete_list_item(item, item.listWidget())
        self.ui.availablePokemonsList.addItem(item)

    def _play_soundtrack(self, file, loops=3):
        """Plays the given soundtrack file"""
        self._media_player.setSource(QUrl.fromLocalFile(file))
        self._media_player.setLoops(loops)
        self._media_player.play()

    def _go_fight_player_page(self):
        """
        Fight can be started if both players have pokemons
        If it's 'computer' mode, its pokemons can be chosen
        by player, or randomly
        """
        pokemons1 = self._first_player.get_pokemons()
        pokemons2 = self._second_player.get_pokemons()
        if not pokemons1:
            return
        computer_mode = mode['against_computer']
        if self._mode == computer_mode and not pokemons2:
            n = len(pokemons1)
            pokemons2 = self._simulator.generate_computer_pokemons(n)
        if pokemons1 and pokemons2:
            self._setup_fight_page()
            self._go_to_page(self._pages['fight_page'])
            music_file = self._get_music_file('combat')
            self._play_soundtrack(music_file)

    def _setup_fight_page(self):
        """Sets widgets on fight page"""
        self._do_for_both_players(
            self._set_player_name_fight_page,
            widgets=[
                self.ui.firstPlayerNameLabel,
                self.ui.secondPlayerNameLabel
            ])
        self._do_for_both_players(
            self._set_current_pokemon_name_fight_page,
            widgets=[
                self.ui.currentPokemon1Label,
                self.ui.currentPokemon2Label
            ])
        self._do_for_both_players(
            self._set_current_pokemon_image_fight_page,
            widgets=[
                self.ui.currentPokemon1Label,
                self.ui.currentPokemon2Label
            ])
        self._do_for_both_players(
            self._set_pokemons_list_fight_page,
            widgets=[
                self.ui.pokemonsList1,
                self.ui.pokemonsList2
            ])
        self._do_for_both_players(self._hide_pokemon_special_attack_type_menu)
        self._do_for_both_players(lambda pl, args:
                                  self._set_enabled_widgets(pl, True))
        self._set_round_label_fight_page(self._simulator.get_rounds())
        self._set_comments()
        if self._mode == mode['against_computer']:
            self._set_enabled_widgets(self._second_player, False)

    def _hide_pokemon_special_attack_type_menu(self, player, args):
        player.widgets['choose_type_label'].hide()
        player.widgets['special_attack_types'].hide()

    def _set_player_name_fight_page(self, player, label):
        """Sets given player's name on fight page on given label"""
        label.setText(player.get_name())

    def _set_current_pokemon_name_fight_page(self, player, label):
        """Sets the name of player's current pokemon"""
        if player.get_current_pokemon() is None:
            player.set_current_pokemon(player.get_pokemons()[0])
        pokemon_name = player.get_current_pokemon().get_name()
        label.setText(pokemon_name)

    def _get_pokemon_image(self, pokemon):
        """Returns image of given pokemon"""
        image = QImage()
        image.loadFromData(pokemon.get_image_content())
        return image

    def _set_current_pokemon_image_fight_page(self, player, label):
        """Sets image of player's current pokemon to label as Pixmap"""
        pokemon = player.get_current_pokemon()
        try:
            label.setPixmap(QPixmap(self._get_pokemon_image(pokemon)))
        except Exception:
            print(LoadImageError())

    def _set_pokemons_list_fight_page(self, player, list):
        """Sets the list of player's pokemons on fight page"""
        list.clear()
        for pokemon in player.get_pokemons():
            hp = int(pokemon.get_stat("hp"))
            name = pokemon.get_name()
            text = (f'{name}: {hp}hp')
            item = QListWidgetItem(text)
            if pokemon == player.get_current_pokemon():
                font = item.font()
                font.setBold(True)
                item.setFont(font)
            item.pokemon = pokemon
            list.addItem(item)

    def _set_round_label_fight_page(self, n):
        """Shows the number of round"""
        self.ui.roundLabel.setText(f'Round {n}')

    def _set_comments(self):
        """Shows comments of the recent players' moves"""
        comment1 = self._first_player.get_comment()
        self.ui.commentPlayer1.setText(comment1)
        comment2 = self._second_player.get_comment()
        self.ui.commentPlayer2.setText(comment2)

    def _do_for_both_players(self, func, **kwargs):
        """Shortens the code calling function for both players"""
        widgets = kwargs.get('widgets')
        func(self._first_player, widgets[0] if widgets else kwargs)
        func(self._second_player, widgets[1] if widgets else kwargs)


def gui(args):
    url = './pokemons_fight_simulator/images/background_transparent.jpg'
    stylesheet = (
        'PokemonsFightSimulatorWindow {' +
        f'background-image: url({url});'
        'background-repeat: no-repeat;' +
        'background-position: center;}')
    if not QApplication.instance():
        app = QApplication(args)
    else:
        app = QApplication.instance()
    app.setStyleSheet(stylesheet)
    main_window = PokemonsFightSimulatorWindow()
    main_window.show()
    return app.exec()
