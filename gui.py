import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QIcon
from blueprint import blueprint
from pathlib import Path
import os

rides = [
"Basilisk",
"BlackFalcon",
"Connie",
"CustomLooping",
"Dive",
"ElLoco",
"Floorless",
"Flying",
"FourthDimension",
"FreeFly",
"GigaInvincible",
"GigaRage",
"HypercoasterAnubis",
"HypercoasterEqualizer",
"InvertedBoa",
"InvertedRival",
"IronHorse",
"Junior",
"JuniorDragon",
"JuniorWendigo",
"LaunchedSprint500",
"LaunchedTorque",
"LogFlume",
"LunaAutos",
"MgcKatz",
"MineTrain",
"OverDive",
"PrototypeWing",
"RollingRiver",
"SilvStar",
"Spinning",
"StandupCoaster",
"WingCoaster",
"WoodenSteelHybridMaliceUnchained",
"WoodenSwitchbackReversing",
"WoodenTopperTrack",
"SleighRide",
"VNTR",
"CPRHD",
"Interactive_Shooting_Ride",
"GoKarts",
"SteelHydra",
"Bakasura",
"Trident",
"Bolt",
"Degen",
"ViperOne",
"Gnarler",
"PowerUp",
"ManicMouse",
"SteelVengeance",
"ZenithPowered",
"CCade",
"HopTheGaps",
"MouseHunt",
"GoldFever",
"IVenture",
"LandHo",
"MechArm",
"StudioTour",
"BackToTheFuture",
"Slimer_Kiddie_Coaster",
"Interactive_Ecto_1_Ride",
"KnightRider",
"TheMunsters",
"LoopingShuttle",
"InvertedArrow",
"Tracker",
"Chairlift",
"SteelMultiRole",
"Overhang",
"SpinCoaster",
"DarkBoatRide",
"ClassicCar",
"Gondolalift",
"Zephyrus",
"FTurns",
"Interceptor",
"Jixxer",
]

elements = [
"default_booster",
"default_brakes",
"default_spline",
"default_chainlift",
"default_blocksection",
"TK_SP_NonInvLoopLeft",
"TK_SP_NonInvLoopRight",
"TK_SP_OverbankedTurnLeft",
"TK_SP_OverbankedTurnRight",
"TK_SP_Helix_UpLeft",
"TK_SP_Helix_UpRight",
"TK_SP_Helix_DownLeft",
"TK_SP_Helix_DownRight",
"TK_SP_HalfHelix_UpLeft",
"TK_SP_HalfHelix_UpRight",
"TK_SP_HalfHelix_DownLeft",
"TK_SP_HalfHelix_DownRight",
"TK_SP_DiveLoopLeft",
"TK_SP_DiveLoopRight",
"TK_SP_Immelmann_180Left",
"TK_SP_Immelmann_180Right",
"TK_SP_Immelmann_90Left",
"TK_SP_Immelmann_90Right",
"TK_SP_InclinedDiveLoopLeft",
"TK_SP_InclinedDiveLoopRight",
"TK_SP_InclinedLoop_80Left",
"TK_SP_InclinedLoop_80Right",
"TK_SP_InclinedLoop_45Left",
"TK_SP_InclinedLoop_45Right",
"TK_SP_NorwegianLoopLeft",
"TK_SP_NorwegianLoopRight",
"TK_SP_PretzelLoopLeft",
"TK_SP_PretzelLoopRight",
"TK_SP_VerticalLoopLeft",
"TK_SP_VerticalLoopRight",
"TK_SP_HalfLoop_Up",
"TK_SP_HalfLoop_Down",
"TK_SP_BananaRollLeft",
"TK_SP_BananaRollRight",
"TK_SP_BatwingLeft",
"TK_SP_BatwingRight",
"TK_SP_BowtieLeft",
"TK_SP_BowtieRight",
"TK_SP_ButterflyInversionLeft",
"TK_SP_ButterflyInversionRight",
"TK_SP_CobraRollLeft",
"TK_SP_CobraRollRight",
"TK_SP_CorkscrewLeft",
"TK_SP_CorkscrewRight",
"TK_SP_Corkscrew_InLeft",
"TK_SP_Corkscrew_InRight",
"TK_SP_Corkscrew_OutLeft",
"TK_SP_Corkscrew_OutRight",
"TK_SP_CutbackLeft",
"TK_SP_CutbackRight",
"TK_SP_DemonicKnotLeft",
"TK_SP_DemonicKnotRight",
"TK_SP_HammerHeadTurnLeft",
"TK_SP_HammerHeadTurnRight",
"TK_SP_HeartlineRoll_InLeft",
"TK_SP_HeartlineRoll_InRight",
"TK_SP_HeartlineRoll_OutLeft",
"TK_SP_HeartlineRoll_OutRight",
"TK_SP_VerticalHeartlineRoll_InLeft",
"TK_SP_VerticalHeartlineRoll_InRight",
"TK_SP_VerticalHeartlineRoll_OutLeft",
"TK_SP_VerticalHeartlineRoll_OutRight",
"TK_SP_InlineTwistLeft",
"TK_SP_InlineTwistRight",
"TK_SP_InlineTwist_InLeft",
"TK_SP_InlineTwist_InRight",
"TK_SP_InlineTwist_OutLeft",
"TK_SP_InlineTwist_OutRight",
"TK_SP_VerticalInlineTwist_InLeft",
"TK_SP_VerticalInlineTwist_InRight",
"TK_SP_VerticalInlineTwist_OutLeft",
"TK_SP_VerticalInlineTwist_OutRight",
"TK_SP_PretzelKnotLeft",
"TK_SP_PretzelKnotRight",
"TK_SP_SeaSerpentLeft",
"TK_SP_SeaSerpentRight",
"TK_SP_TwistedHorseShoeRollLeft",
"TK_SP_TwistedHorseShoeRollRight",
"TK_SP_ZeroGRollLeft",
"TK_SP_ZeroGRollRight",
"TK_SP_SnakeDiveLeft",
"TK_SP_SnakeDiveRight",
"TK_SP_InlineRoll_InLeft",
"TK_SP_InlineRoll_InRight",
"TK_SP_InlineRoll_OutLeft",
"TK_SP_InlineRoll_OutRight",
"TK_SP_VerticalInlineRoll_InLeft",
"TK_SP_VerticalInlineRoll_InRight",
"TK_SP_VerticalInlineRoll_OutLeft",
"TK_SP_VerticalInlineRoll_OutRight",
"TK_SP_Figure8HelixLeft",
"TK_SP_Figure8HelixRight",
"TK_SP_DiveDropLeft",
"TK_SP_DiveDropRight",
"station_leftleft",
"station_leftright",
"station_rightleft",
"station_rightright",
"TK_SP_HeartlineRollLeft",
"TK_SP_HeartlineRollRight",
"TK_SP_VerticalHeartlineRollLeft",
"TK_SP_VerticalHeartlineRollRight",
"TK_SP_InlineRollLeft",
"TK_SP_InlineRollRight",
"TK_SP_VerticalInlineRollLeft",
"TK_SP_VerticalInlineRollRight",
"TK_SP_VerticalInlineTwistLeft",
"TK_SP_VerticalInlineTwistRight",
"TK_SP_WrapAroundCorkscrewLeft",
"TK_SP_WrapAroundCorkscrewRight",
"trim_brakes_TK_038",
"default_LSM",
"default_LSM_HoldingSection",
]

trains = [
"Aethon",
"Anubis",
"BFalcon",
"BLisk",
"Barghest",
"Boa",
"CanyonRunner",
"CloudR",
"Connie",
"Dragon",
"Enigma",
"Eqlzr",
"Fury",
"GASM",
"Invincible",
"IronHorse",
"LTurns",
"LunaAutos",
"MUC",
"MgcKatz",
"Mnstr",
"MtSplash",
"Pioneer",
"Rage",
"Riv",
"RollingRiver",
"SPR",
"SRay",
"SilvStar",
"Sp500",
"TMat",
"TPil",
"Tor",
"WWolf",
"Wend",
"WendJnr",
"Degen",
"SleighRide",
"Gnarler",
"Zephyrus",
"VNTR",
"Slimer_Kiddie_Coaster",
"CPRHD",
"Interactive_Shooting_Ride",
"SuperDrift",
"SHydra",
"Bsura",
"Trident",
"Bolt",
"KnightRider",
"TheMunsters",
"BackToTheFuture",
"ViperOne",
"PowerUp",
"CMouse",
"MUC_SV",
"Zenith",
"CCade",
"HTG",
"MouseHunt",
"GoldFever",
"IVenture",
"LandHo",
"MechArm",
"StudioTour",
"Interactive_Ecto_1_Ride",
"LoopingShuttle",
"InvertedArrow",
"Tracker",
"SteelMultiRole",
"Chairlift",
"Huntsman",
"Overhang",
"SpinCoaster",
"DarkBoatRide",
"ClassicCar",
"Gondolalift",
"Hoax",
"IDescent",
"FTurns",
"Interceptor",
"Jixxer",
"PMover",
"SteelVengeance",
]

class Table(QTableWidget):
    def __init__(self):
        global rides
        super(Table, self).__init__()
        self.setHorizontalHeaderLabels(["Test","Test1","Test2"])
        self.item = QTableWidgetItem("New")
        self.setItem(0, 0, self.item)

        self.com = QComboBox(self)
        self.com.addItem("1")
        self.com.addItem("2")
        self.com.setStyleSheet("QComboBox{margin:3px};")
        self.setCellWidget(0, 1, self.com)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
  
        self.setWindowTitle("PC Blueprint Editor")
        self.initDir = ("{}/{}".format(str(Path.home()), "Saved Games/Frontier Developments/Planet Coaster/76561198169991941/Saves"))
        print(self.initDir)
        self.resize(420,500)
        self.setWindowIcon(QtGui.QIcon('logo.jpg')) 

        self.infoBoxes = []

        newfont = QFontComboBox
        self.text = QLabel("Coaster: ", self)
        self.text.setFont((QtGui.QFont("Verdana", 10)))
        self.text.move(10, 25)

        # Create new action
        injectAction = QAction(QIcon('new.png'), '&Inject', self)        
        injectAction.setShortcut('Ctrl+N')
        injectAction.setStatusTip('Inject File into Game')
        injectAction.triggered.connect(self.saveCall)

        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open document')
        openAction.triggered.connect(self.openCall)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        #Settings action
        dirAction = QAction(QIcon('exit.png'), '&Dir', self)        
        dirAction.setShortcut('Ctrl+P')
        dirAction.setStatusTip('Set PC Dir')
        dirAction.triggered.connect(self.setDirCall)

        # Create menu bar and add action
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('&File')
        fileMenu.addAction(injectAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        settingsMenu = self.menuBar.addMenu("&Settings")
        settingsMenu.addAction(dirAction)

    def setDirCall(self):
        self.fileOpener = QFileDialog()
        self.pcDir = self.fileOpener.getExistingDirectory(self, 'PC Folder', self.initDir)

    def openCall(self):
        self.fileOpener = QFileDialog()
        self.file = self.fileOpener.getExistingDirectory(self, 'Audio Files', self.initDir)
        print(self.file)
        if self.file:
            self.bp = blueprint(self.file, self.pcDir)
            self.text.setText("Coaster: {}".format(self.bp.name))
            self.text.setFixedWidth(500)
            self.initCombos()

    def saveCall(self):
        print('Save')
        try:
            self.out = self.bp.strings
            print(self.out)
            self.out[0] = self.coms[0].currentText()
            self.out[1] = self.coms[1].currentText()
            self.out[2] = self.bp.strings[2]
            if self.out[2] == "NO_MUSIC":
                for i, item in enumerate(self.trackComs):
                    self.out[3+i] = str(item.currentText())
            else:
                self.out[3] = "NO_MUSIC"
                for i, item in enumerate(self.coms):
                    self.out[2+i] = str(item.currentText())
            print(self.bp.strings)
            print(self.out)
        except:
            pass
            
        self.bp.write_strings(self.out)

    def exitCall(self):
        print('Exit app')
        QtCore.QCoreApplication.quit()

    def clickMethod(self):
        for item in self.infoBoxes:
            print(item.currentText())

    def initCombos(self):
        global rides
        global elements
        global trains

        self.coms = []
        self.trackComs = []

        self.type = self.bp.strings[0]
        self.train = self.bp.strings[1]
        print("TRAIN: " + str(self.train))
        if self.bp.strings[2] == "NO_MUSIC":
            self.tracks = self.bp.strings[3:]
        if self.bp.strings[3] == "NO_MUSIC":
            self.tracks = self.bp.strings[4:]

        self.table = QTableWidget(self)
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()
        self.table.setRowCount(self.bp.stringsCount-2)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Key","Value"])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self.typeCom = self.addItemToTable(self.table, "Type", rides, 0)
        self.typeCom.setCurrentText(self.type)
        self.coms.append(self.typeCom)

        self.trainCom = self.addItemToTable(self.table, "Train", trains, 1)
        self.trainCom.setCurrentText(self.train)
        self.coms.append(self.trainCom)

        for i in range(len(self.tracks)):
            ret = self.addItemToTable(self.table, self.tracks[i], elements, 2+i)
            ret.setCurrentText(self.tracks[i])
            self.coms.append(ret)
            self.trackComs.append(ret)
        self.table.show()

    def addItemToTable(self, table, title, options, row):

        self.table.move(10,60)
        self.table.resize(400,500)

        self.com = comboItem(title, options)
        self.table.setItem(row ,0, QTableWidgetItem(title))
        self.table.setCellWidget(row, 1, self.com)
        return self.com

class comboItem(QComboBox):
    def __init__(self, title, options):
        super(QComboBox, self).__init__()
        for option in options:
            self.addItem(option)
        self.setStyleSheet("QComboBox{margin:3px};")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )