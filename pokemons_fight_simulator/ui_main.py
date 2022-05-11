# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pokemons.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStackedWidget,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1050, 565)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(1050, 565))
        mainWindow.setMaximumSize(QSize(1050, 565))
        mainWindow.setWindowTitle(u"Pok\u00e9mon")
        icon = QIcon()
        icon.addFile(u"./pokemons_fight_simulator/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"")
        mainWindow.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.stack.setFont(font)
        self.stack.setAutoFillBackground(False)
        self.stack.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.buttonPlayerVsPlayer = QPushButton(self.page_2)
        self.buttonPlayerVsPlayer.setObjectName(u"buttonPlayerVsPlayer")
        self.buttonPlayerVsPlayer.setGeometry(QRect(435, 250, 180, 60))
        self.buttonPlayerVsPlayer.setFont(font)
        self.buttonPlayerVsPlayer.setAutoFillBackground(False)
        self.buttonPlayerVsPlayer.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonPlayerVsComputer = QPushButton(self.page_2)
        self.buttonPlayerVsComputer.setObjectName(u"buttonPlayerVsComputer")
        self.buttonPlayerVsComputer.setGeometry(QRect(435, 330, 180, 60))
        self.buttonPlayerVsComputer.setFont(font)
        self.buttonPlayerVsComputer.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(375, 150, 300, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.stack.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 100, 171, 51))
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.buttonStartGameVsPlayer = QPushButton(self.page)
        self.buttonStartGameVsPlayer.setObjectName(u"buttonStartGameVsPlayer")
        self.buttonStartGameVsPlayer.setGeometry(QRect(470, 220, 111, 61))
        self.buttonStartGameVsPlayer.setFont(font)
        self.buttonStartGameVsPlayer.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonConfigureFirstPlayer = QPushButton(self.page)
        self.buttonConfigureFirstPlayer.setObjectName(u"buttonConfigureFirstPlayer")
        self.buttonConfigureFirstPlayer.setGeometry(QRect(440, 310, 171, 61))
        self.buttonConfigureFirstPlayer.setFont(font)
        self.buttonConfigureFirstPlayer.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonConfigureSecondPlayer = QPushButton(self.page)
        self.buttonConfigureSecondPlayer.setObjectName(u"buttonConfigureSecondPlayer")
        self.buttonConfigureSecondPlayer.setGeometry(QRect(440, 400, 171, 61))
        self.buttonConfigureSecondPlayer.setFont(font)
        self.buttonConfigureSecondPlayer.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonBack1 = QPushButton(self.page)
        self.buttonBack1.setObjectName(u"buttonBack1")
        self.buttonBack1.setGeometry(QRect(870, 30, 111, 61))
        self.buttonBack1.setFont(font)
        self.buttonBack1.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 220, 171, 61))
        self.groupBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.maxPokemonsSpinbox = QSpinBox(self.page)
        self.maxPokemonsSpinbox.setObjectName(u"maxPokemonsSpinbox")
        self.maxPokemonsSpinbox.setGeometry(QRect(90, 250, 61, 21))
        self.maxPokemonsSpinbox.setMinimum(1)
        self.maxPokemonsSpinbox.setMaximum(30)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 220, 151, 31))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_3.setFont(font3)
        self.stack.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.playerNameEdit = QLineEdit(self.page_4)
        self.playerNameEdit.setObjectName(u"playerNameEdit")
        self.playerNameEdit.setGeometry(QRect(450, 70, 151, 41))
        self.playerNameEdit.setFont(font)
        self.playerNameEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.findPokemonEdit = QLineEdit(self.page_4)
        self.findPokemonEdit.setObjectName(u"findPokemonEdit")
        self.findPokemonEdit.setGeometry(QRect(300, 170, 450, 40))
        self.findPokemonEdit.setFont(font)
        self.findPokemonEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonBack2 = QPushButton(self.page_4)
        self.buttonBack2.setObjectName(u"buttonBack2")
        self.buttonBack2.setGeometry(QRect(870, 30, 111, 61))
        self.buttonBack2.setFont(font)
        self.buttonBack2.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.layoutWidget = QWidget(self.page_4)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(250, 230, 551, 241))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.availablePokemonsList = QListWidget(self.layoutWidget)
        self.availablePokemonsList.setObjectName(u"availablePokemonsList")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.availablePokemonsList.setFont(font4)
        self.availablePokemonsList.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")

        self.horizontalLayout_2.addWidget(self.availablePokemonsList)

        self.chosenPokemonsList = QListWidget(self.layoutWidget)
        self.chosenPokemonsList.setObjectName(u"chosenPokemonsList")
        self.chosenPokemonsList.setFont(font4)
        self.chosenPokemonsList.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")

        self.horizontalLayout_2.addWidget(self.chosenPokemonsList)

        self.stack.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.firstPlayerNameLabel = QLabel(self.page_5)
        self.firstPlayerNameLabel.setObjectName(u"firstPlayerNameLabel")
        self.firstPlayerNameLabel.setGeometry(QRect(30, 30, 120, 40))
        self.firstPlayerNameLabel.setFont(font)
        self.firstPlayerNameLabel.setStyleSheet(u"")
        self.secondPlayerNameLabel = QLabel(self.page_5)
        self.secondPlayerNameLabel.setObjectName(u"secondPlayerNameLabel")
        self.secondPlayerNameLabel.setGeometry(QRect(882, 30, 120, 40))
        self.secondPlayerNameLabel.setFont(font)
        self.secondPlayerNameLabel.setStyleSheet(u"")
        self.roundLabel = QLabel(self.page_5)
        self.roundLabel.setObjectName(u"roundLabel")
        self.roundLabel.setGeometry(QRect(476, 15, 80, 41))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.roundLabel.setFont(font5)
        self.roundLabel.setStyleSheet(u"")
        self.roundLabel.setAlignment(Qt.AlignCenter)
        self.pokemonsList1 = QListWidget(self.page_5)
        self.pokemonsList1.setObjectName(u"pokemonsList1")
        self.pokemonsList1.setGeometry(QRect(0, 330, 150, 200))
        self.pokemonsList1.setFont(font4)
        self.pokemonsList1.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        self.pokemonsList2 = QListWidget(self.page_5)
        self.pokemonsList2.setObjectName(u"pokemonsList2")
        self.pokemonsList2.setGeometry(QRect(880, 330, 150, 200))
        self.pokemonsList2.setFont(font4)
        self.pokemonsList2.setStyleSheet(u"background-color: rgba(255, 255, 255, 150);")
        self.buttonDefense1 = QPushButton(self.page_5)
        self.buttonDefense1.setObjectName(u"buttonDefense1")
        self.buttonDefense1.setGeometry(QRect(60, 90, 100, 40))
        self.buttonDefense1.setFont(font)
        self.buttonDefense1.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonSpecialAttack1 = QPushButton(self.page_5)
        self.buttonSpecialAttack1.setObjectName(u"buttonSpecialAttack1")
        self.buttonSpecialAttack1.setGeometry(QRect(230, 90, 100, 40))
        self.buttonSpecialAttack1.setFont(font)
        self.buttonSpecialAttack1.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonNormalAttack1 = QPushButton(self.page_5)
        self.buttonNormalAttack1.setObjectName(u"buttonNormalAttack1")
        self.buttonNormalAttack1.setGeometry(QRect(60, 170, 100, 40))
        self.buttonNormalAttack1.setFont(font)
        self.buttonNormalAttack1.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonSpecialAttack2 = QPushButton(self.page_5)
        self.buttonSpecialAttack2.setObjectName(u"buttonSpecialAttack2")
        self.buttonSpecialAttack2.setGeometry(QRect(680, 90, 100, 40))
        self.buttonSpecialAttack2.setFont(font)
        self.buttonSpecialAttack2.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonNormalAttack2 = QPushButton(self.page_5)
        self.buttonNormalAttack2.setObjectName(u"buttonNormalAttack2")
        self.buttonNormalAttack2.setGeometry(QRect(840, 170, 100, 40))
        self.buttonNormalAttack2.setFont(font)
        self.buttonNormalAttack2.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.buttonDefense2 = QPushButton(self.page_5)
        self.buttonDefense2.setObjectName(u"buttonDefense2")
        self.buttonDefense2.setEnabled(True)
        self.buttonDefense2.setGeometry(QRect(840, 90, 100, 40))
        self.buttonDefense2.setFont(font)
        self.buttonDefense2.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.currentPokemon1Label = QLabel(self.page_5)
        self.currentPokemon1Label.setObjectName(u"currentPokemon1Label")
        self.currentPokemon1Label.setGeometry(QRect(270, 290, 200, 200))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.currentPokemon1Label.sizePolicy().hasHeightForWidth())
        self.currentPokemon1Label.setSizePolicy(sizePolicy2)
        self.currentPokemon1Label.setMinimumSize(QSize(150, 150))
        self.currentPokemon1Label.setStyleSheet(u"")
        self.currentPokemon1Label.setScaledContents(True)
        self.currentPokemon1Label.setAlignment(Qt.AlignCenter)
        self.currentPokemon2Label = QLabel(self.page_5)
        self.currentPokemon2Label.setObjectName(u"currentPokemon2Label")
        self.currentPokemon2Label.setGeometry(QRect(562, 290, 200, 200))
        sizePolicy2.setHeightForWidth(self.currentPokemon2Label.sizePolicy().hasHeightForWidth())
        self.currentPokemon2Label.setSizePolicy(sizePolicy2)
        self.currentPokemon2Label.setMinimumSize(QSize(150, 150))
        self.currentPokemon2Label.setStyleSheet(u"")
        self.currentPokemon2Label.setScaledContents(True)
        self.buttonEndFight = QPushButton(self.page_5)
        self.buttonEndFight.setObjectName(u"buttonEndFight")
        self.buttonEndFight.setGeometry(QRect(466, 80, 100, 40))
        self.buttonEndFight.setFont(font)
        self.buttonEndFight.setStyleSheet(u"background-color: rgba(255, 255, 255, 123);")
        self.commentPlayer1 = QLabel(self.page_5)
        self.commentPlayer1.setObjectName(u"commentPlayer1")
        self.commentPlayer1.setGeometry(QRect(30, 240, 350, 40))
        self.commentPlayer1.setFont(font)
        self.commentPlayer1.setStyleSheet(u"")
        self.commentPlayer2 = QLabel(self.page_5)
        self.commentPlayer2.setObjectName(u"commentPlayer2")
        self.commentPlayer2.setGeometry(QRect(652, 240, 350, 40))
        self.commentPlayer2.setFont(font)
        self.commentPlayer2.setStyleSheet(u"")
        self.typesList1 = QListWidget(self.page_5)
        self.typesList1.setObjectName(u"typesList1")
        self.typesList1.setGeometry(QRect(230, 180, 130, 46))
        self.typesList1.setFont(font3)
        self.typesList1.setSelectionRectVisible(False)
        self.chooseSpecialTypeLabel1 = QLabel(self.page_5)
        self.chooseSpecialTypeLabel1.setObjectName(u"chooseSpecialTypeLabel1")
        self.chooseSpecialTypeLabel1.setEnabled(True)
        self.chooseSpecialTypeLabel1.setGeometry(QRect(230, 150, 181, 16))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setKerning(True)
        self.chooseSpecialTypeLabel1.setFont(font6)
        self.chooseSpecialTypeLabel2 = QLabel(self.page_5)
        self.chooseSpecialTypeLabel2.setObjectName(u"chooseSpecialTypeLabel2")
        self.chooseSpecialTypeLabel2.setGeometry(QRect(620, 150, 163, 16))
        self.chooseSpecialTypeLabel2.setFont(font6)
        self.chooseSpecialTypeLabel2.setInputMethodHints(Qt.ImhNone)
        self.typesList2 = QListWidget(self.page_5)
        self.typesList2.setObjectName(u"typesList2")
        self.typesList2.setGeometry(QRect(650, 180, 130, 46))
        self.typesList2.setFont(font)
        self.typesList2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stack.addWidget(self.page_5)

        self.horizontalLayout.addWidget(self.stack)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.stack.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        self.buttonPlayerVsPlayer.setText(QCoreApplication.translate("mainWindow", u"Player vs Player", None))
        self.buttonPlayerVsComputer.setText(QCoreApplication.translate("mainWindow", u"Player vs Computer", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"POKEMONS FIGHT SIMULATOR!", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Configuration", None))
        self.buttonStartGameVsPlayer.setText(QCoreApplication.translate("mainWindow", u"Start game", None))
        self.buttonConfigureFirstPlayer.setText(QCoreApplication.translate("mainWindow", u"Configure Player1", None))
        self.buttonConfigureSecondPlayer.setText(QCoreApplication.translate("mainWindow", u"Configure Player2", None))
        self.buttonBack1.setText(QCoreApplication.translate("mainWindow", u"Go back", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Max pokemons in team:", None))
        self.playerNameEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Enter player name", None))
        self.findPokemonEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Enter pokemon name", None))
        self.buttonBack2.setText(QCoreApplication.translate("mainWindow", u"Go back", None))
        self.firstPlayerNameLabel.setText(QCoreApplication.translate("mainWindow", u"Player1 Name", None))
        self.secondPlayerNameLabel.setText(QCoreApplication.translate("mainWindow", u"Player2 Name", None))
        self.roundLabel.setText(QCoreApplication.translate("mainWindow", u"Round N", None))
        self.buttonDefense1.setText(QCoreApplication.translate("mainWindow", u"Defense", None))
        self.buttonSpecialAttack1.setText(QCoreApplication.translate("mainWindow", u"Special Attack", None))
        self.buttonNormalAttack1.setText(QCoreApplication.translate("mainWindow", u"Normal Attack", None))
        self.buttonSpecialAttack2.setText(QCoreApplication.translate("mainWindow", u"Special Attack", None))
        self.buttonNormalAttack2.setText(QCoreApplication.translate("mainWindow", u"Normal Attack", None))
        self.buttonDefense2.setText(QCoreApplication.translate("mainWindow", u"Defense", None))
        self.currentPokemon1Label.setText("")
        self.currentPokemon2Label.setText("")
        self.buttonEndFight.setText(QCoreApplication.translate("mainWindow", u"End fight", None))
        self.commentPlayer1.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
        self.commentPlayer2.setText(QCoreApplication.translate("mainWindow", u"TextLabel", None))
        self.chooseSpecialTypeLabel1.setText(QCoreApplication.translate("mainWindow", u"Choose special attack type", None))
        self.chooseSpecialTypeLabel2.setText(QCoreApplication.translate("mainWindow", u"Choose special attack type", None))
        pass
    # retranslateUi
