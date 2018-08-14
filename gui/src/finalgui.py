# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalgui.ui'
#
# Created: Fri Jun  1 15:58:25 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1183, 951)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../../../../../../../../Desktop/background.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0)"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1171, 871))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame_4 = QtGui.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(20, 40, 231, 241))
        self.frame_4.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.Serial_Node = QtGui.QCheckBox(self.frame_4)
        self.Serial_Node.setGeometry(QtCore.QRect(10, 60, 191, 22))
        self.Serial_Node.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Serial_Node.setObjectName(_fromUtf8("Serial_Node"))
        self.Drive_2 = QtGui.QCheckBox(self.frame_4)
        self.Drive_2.setGeometry(QtCore.QRect(10, 80, 161, 22))
        self.Drive_2.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Drive_2.setObjectName(_fromUtf8("Drive_2"))
        self.Drive1_2 = QtGui.QCheckBox(self.frame_4)
        self.Drive1_2.setGeometry(QtCore.QRect(10, 100, 131, 22))
        self.Drive1_2.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Drive1_2.setObjectName(_fromUtf8("Drive1_2"))
        self.Drive_Diff_2 = QtGui.QCheckBox(self.frame_4)
        self.Drive_Diff_2.setGeometry(QtCore.QRect(10, 120, 131, 22))
        self.Drive_Diff_2.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Drive_Diff_2.setObjectName(_fromUtf8("Drive_Diff_2"))
        self.label_6 = QtGui.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 101, 21))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Locomotion_Control_2 = QtGui.QCheckBox(self.frame_4)
        self.Locomotion_Control_2.setGeometry(QtCore.QRect(10, 140, 191, 22))
        self.Locomotion_Control_2.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Locomotion_Control_2.setObjectName(_fromUtf8("Locomotion_Control_2"))
        self.GUI_Pinger = QtGui.QCheckBox(self.frame_4)
        self.GUI_Pinger.setGeometry(QtCore.QRect(10, 160, 201, 22))
        self.GUI_Pinger.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.GUI_Pinger.setObjectName(_fromUtf8("GUI_Pinger"))
        self.GUI_Subscriber = QtGui.QCheckBox(self.frame_4)
        self.GUI_Subscriber.setGeometry(QtCore.QRect(10, 180, 201, 22))
        self.GUI_Subscriber.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.GUI_Subscriber.setObjectName(_fromUtf8("GUI_Subscriber"))
        self.Joy_Node_2 = QtGui.QCheckBox(self.frame_4)
        self.Joy_Node_2.setGeometry(QtCore.QRect(10, 200, 201, 22))
        self.Joy_Node_2.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Joy_Node_2.setObjectName(_fromUtf8("Joy_Node_2"))
        self.button2_2 = QtGui.QPushButton(self.tab)
        self.button2_2.setGeometry(QtCore.QRect(20, 420, 151, 41))
        self.button2_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgba(38, 206, 203,200);\n"
"border-color: rgba(255, 85, 0,175);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 63 medium 11pt \"Ubuntu\";\n"
""))
        self.button2_2.setDefault(False)
        self.button2_2.setObjectName(_fromUtf8("button2_2"))
        self.IP_Adress_2 = QtGui.QPlainTextEdit(self.tab)
        self.IP_Adress_2.setGeometry(QtCore.QRect(110, 540, 171, 31))
        self.IP_Adress_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.IP_Adress_2.setObjectName(_fromUtf8("IP_Adress_2"))
        self.run_3 = QtGui.QPushButton(self.tab)
        self.run_3.setGeometry(QtCore.QRect(20, 350, 151, 41))
        self.run_3.setMouseTracking(False)
        self.run_3.setStyleSheet(_fromUtf8("background: url();\n"
"font: 63 medium 11pt \"Ubuntu\";\n"
"background-color: rgba(38, 206, 203,200);\n"
"border-color: rgba(255, 85, 0,175);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;"))
        self.run_3.setDefault(False)
        self.run_3.setObjectName(_fromUtf8("run_3"))
        self.label_25 = QtGui.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(20, 540, 81, 31))
        self.label_25.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.frame_8 = QtGui.QFrame(self.tab)
        self.frame_8.setGeometry(QtCore.QRect(320, 40, 681, 551))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.ErrorBox_2 = QtGui.QPlainTextEdit(self.frame_8)
        self.ErrorBox_2.setGeometry(QtCore.QRect(20, 50, 641, 471))
        self.ErrorBox_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.ErrorBox_2.setObjectName(_fromUtf8("ErrorBox_2"))
        self.label_12 = QtGui.QLabel(self.frame_8)
        self.label_12.setGeometry(QtCore.QRect(260, 20, 161, 21))
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.frame_3 = QtGui.QFrame(self.tab_3)
        self.frame_3.setGeometry(QtCore.QRect(30, 20, 421, 661))
        self.frame_3.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_19 = QtGui.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(130, 20, 201, 51))
        self.label_19.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_19.setScaledContents(False)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.Right_Front_Velocity = QtGui.QPlainTextEdit(self.frame_3)
        self.Right_Front_Velocity.setGeometry(QtCore.QRect(20, 140, 191, 71))
        self.Right_Front_Velocity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Right_Front_Velocity.setObjectName(_fromUtf8("Right_Front_Velocity"))
        self.Left_Front_Velocity = QtGui.QPlainTextEdit(self.frame_3)
        self.Left_Front_Velocity.setGeometry(QtCore.QRect(240, 140, 171, 71))
        self.Left_Front_Velocity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Left_Front_Velocity.setObjectName(_fromUtf8("Left_Front_Velocity"))
        self.Right_Back_Velocity = QtGui.QPlainTextEdit(self.frame_3)
        self.Right_Back_Velocity.setGeometry(QtCore.QRect(20, 290, 191, 71))
        self.Right_Back_Velocity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Right_Back_Velocity.setObjectName(_fromUtf8("Right_Back_Velocity"))
        self.Left_Back_Velocity = QtGui.QPlainTextEdit(self.frame_3)
        self.Left_Back_Velocity.setGeometry(QtCore.QRect(230, 290, 171, 71))
        self.Left_Back_Velocity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Left_Back_Velocity.setObjectName(_fromUtf8("Left_Back_Velocity"))
        self.label_20 = QtGui.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(20, 90, 141, 31))
        self.label_20.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_22 = QtGui.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(240, 90, 141, 31))
        self.label_22.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(20, 230, 151, 31))
        self.label_23.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(240, 230, 131, 31))
        self.label_24.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_26 = QtGui.QLabel(self.frame_3)
        self.label_26.setGeometry(QtCore.QRect(20, 380, 171, 31))
        self.label_26.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.Left_Pot = QtGui.QPlainTextEdit(self.frame_3)
        self.Left_Pot.setGeometry(QtCore.QRect(20, 420, 191, 71))
        self.Left_Pot.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Left_Pot.setObjectName(_fromUtf8("Left_Pot"))
        self.label_27 = QtGui.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(240, 380, 171, 31))
        self.label_27.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.Right_Pot = QtGui.QPlainTextEdit(self.frame_3)
        self.Right_Pot.setGeometry(QtCore.QRect(230, 420, 181, 71))
        self.Right_Pot.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Right_Pot.setObjectName(_fromUtf8("Right_Pot"))
        self.label_41 = QtGui.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(20, 520, 171, 31))
        self.label_41.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.label_42 = QtGui.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(230, 520, 171, 31))
        self.label_42.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.Right_Pot_Zero = QtGui.QPlainTextEdit(self.frame_3)
        self.Right_Pot_Zero.setGeometry(QtCore.QRect(230, 560, 181, 71))
        self.Right_Pot_Zero.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Right_Pot_Zero.setObjectName(_fromUtf8("Right_Pot_Zero"))
        self.Left_Pot_Zero = QtGui.QPlainTextEdit(self.frame_3)
        self.Left_Pot_Zero.setGeometry(QtCore.QRect(20, 560, 181, 71))
        self.Left_Pot_Zero.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Left_Pot_Zero.setObjectName(_fromUtf8("Left_Pot_Zero"))
        self.frame_5 = QtGui.QFrame(self.frame_3)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 421, 661))
        self.frame_5.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.label_28 = QtGui.QLabel(self.frame_5)
        self.label_28.setGeometry(QtCore.QRect(130, 20, 201, 51))
        self.label_28.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_28.setScaledContents(False)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.Right_Front_Velocity_2 = QtGui.QPlainTextEdit(self.frame_5)
        self.Right_Front_Velocity_2.setGeometry(QtCore.QRect(20, 140, 191, 71))
        self.Right_Front_Velocity_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Right_Front_Velocity_2.setObjectName(_fromUtf8("Right_Front_Velocity_2"))
        self.Left_Front_Velocity_2 = QtGui.QPlainTextEdit(self.frame_5)
        self.Left_Front_Velocity_2.setGeometry(QtCore.QRect(240, 140, 171, 71))
        self.Left_Front_Velocity_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Left_Front_Velocity_2.setObjectName(_fromUtf8("Left_Front_Velocity_2"))
        self.Right_Back_Velocity_2 = QtGui.QPlainTextEdit(self.frame_5)
        self.Right_Back_Velocity_2.setGeometry(QtCore.QRect(20, 290, 191, 71))
        self.Right_Back_Velocity_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Right_Back_Velocity_2.setObjectName(_fromUtf8("Right_Back_Velocity_2"))
        self.Left_Back_Velocity_2 = QtGui.QPlainTextEdit(self.frame_5)
        self.Left_Back_Velocity_2.setGeometry(QtCore.QRect(230, 290, 171, 71))
        self.Left_Back_Velocity_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Left_Back_Velocity_2.setObjectName(_fromUtf8("Left_Back_Velocity_2"))
        self.label_29 = QtGui.QLabel(self.frame_5)
        self.label_29.setGeometry(QtCore.QRect(20, 90, 141, 31))
        self.label_29.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.frame_5)
        self.label_30.setGeometry(QtCore.QRect(240, 90, 141, 31))
        self.label_30.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_32 = QtGui.QLabel(self.frame_5)
        self.label_32.setGeometry(QtCore.QRect(20, 230, 151, 31))
        self.label_32.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.frame_5)
        self.label_33.setGeometry(QtCore.QRect(240, 230, 131, 31))
        self.label_33.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_37 = QtGui.QLabel(self.frame_5)
        self.label_37.setGeometry(QtCore.QRect(20, 380, 171, 31))
        self.label_37.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.Left_Pot_2 = QtGui.QPlainTextEdit(self.frame_5)
        self.Left_Pot_2.setGeometry(QtCore.QRect(20, 420, 191, 71))
        self.Left_Pot_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Left_Pot_2.setObjectName(_fromUtf8("Left_Pot_2"))
        self.label_38 = QtGui.QLabel(self.frame_5)
        self.label_38.setGeometry(QtCore.QRect(240, 380, 171, 31))
        self.label_38.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.Right_Pot_2 = QtGui.QPlainTextEdit(self.frame_5)
        self.Right_Pot_2.setGeometry(QtCore.QRect(230, 420, 181, 71))
        self.Right_Pot_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Right_Pot_2.setObjectName(_fromUtf8("Right_Pot_2"))
        self.label_44 = QtGui.QLabel(self.frame_5)
        self.label_44.setGeometry(QtCore.QRect(20, 520, 171, 31))
        self.label_44.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.label_59 = QtGui.QLabel(self.frame_5)
        self.label_59.setGeometry(QtCore.QRect(230, 520, 171, 31))
        self.label_59.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.Right_Pot_Zero_2 = QtGui.QPlainTextEdit(self.frame_5)
        self.Right_Pot_Zero_2.setGeometry(QtCore.QRect(230, 560, 181, 71))
        self.Right_Pot_Zero_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Right_Pot_Zero_2.setObjectName(_fromUtf8("Right_Pot_Zero_2"))
        self.Left_Pot_Zero_2 = QtGui.QPlainTextEdit(self.frame_5)
        self.Left_Pot_Zero_2.setGeometry(QtCore.QRect(20, 560, 181, 71))
        self.Left_Pot_Zero_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Left_Pot_Zero_2.setObjectName(_fromUtf8("Left_Pot_Zero_2"))
        self.frame = QtGui.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(470, 20, 591, 171))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_36 = QtGui.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(70, 1, 41, 20))
        self.label_36.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_36.setScaledContents(False)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.Operating_Mode = QtGui.QPlainTextEdit(self.frame)
        self.Operating_Mode.setGeometry(QtCore.QRect(170, 10, 181, 31))
        self.Operating_Mode.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Operating_Mode.setObjectName(_fromUtf8("Operating_Mode"))
        self.Set_Motor_1 = QtGui.QPlainTextEdit(self.frame)
        self.Set_Motor_1.setGeometry(QtCore.QRect(60, 90, 141, 61))
        self.Set_Motor_1.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Set_Motor_1.setObjectName(_fromUtf8("Set_Motor_1"))
        self.Set_Motor_2 = QtGui.QPlainTextEdit(self.frame)
        self.Set_Motor_2.setGeometry(QtCore.QRect(230, 90, 141, 61))
        self.Set_Motor_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Set_Motor_2.setObjectName(_fromUtf8("Set_Motor_2"))
        self.label_47 = QtGui.QLabel(self.frame)
        self.label_47.setGeometry(QtCore.QRect(60, 60, 91, 20))
        self.label_47.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_47.setScaledContents(False)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.label_48 = QtGui.QLabel(self.frame)
        self.label_48.setGeometry(QtCore.QRect(230, 60, 91, 20))
        self.label_48.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_48.setScaledContents(False)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.frame_7 = QtGui.QFrame(self.tab_3)
        self.frame_7.setGeometry(QtCore.QRect(490, 200, 641, 571))
        self.frame_7.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.label_39 = QtGui.QLabel(self.frame_7)
        self.label_39.setGeometry(QtCore.QRect(110, 10, 161, 21))
        self.label_39.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_39.setScaledContents(False)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.Loco_Right_Front_Velocity = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Right_Front_Velocity.setGeometry(QtCore.QRect(20, 80, 191, 71))
        self.Loco_Right_Front_Velocity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Loco_Right_Front_Velocity.setObjectName(_fromUtf8("Loco_Right_Front_Velocity"))
        self.Loco_Left_Front_Velocity = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Left_Front_Velocity.setGeometry(QtCore.QRect(240, 80, 171, 71))
        self.Loco_Left_Front_Velocity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Left_Front_Velocity.setObjectName(_fromUtf8("Loco_Left_Front_Velocity"))
        self.Loco_Right_Back_Velocity = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Right_Back_Velocity.setGeometry(QtCore.QRect(20, 210, 191, 71))
        self.Loco_Right_Back_Velocity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Right_Back_Velocity.setObjectName(_fromUtf8("Loco_Right_Back_Velocity"))
        self.Loco_Left_Back_Velocity = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Left_Back_Velocity.setGeometry(QtCore.QRect(250, 210, 171, 71))
        self.Loco_Left_Back_Velocity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Left_Back_Velocity.setObjectName(_fromUtf8("Loco_Left_Back_Velocity"))
        self.label_40 = QtGui.QLabel(self.frame_7)
        self.label_40.setGeometry(QtCore.QRect(20, 40, 141, 31))
        self.label_40.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_60 = QtGui.QLabel(self.frame_7)
        self.label_60.setGeometry(QtCore.QRect(240, 40, 141, 31))
        self.label_60.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.label_61 = QtGui.QLabel(self.frame_7)
        self.label_61.setGeometry(QtCore.QRect(20, 170, 151, 31))
        self.label_61.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.label_62 = QtGui.QLabel(self.frame_7)
        self.label_62.setGeometry(QtCore.QRect(250, 170, 131, 31))
        self.label_62.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.label_63 = QtGui.QLabel(self.frame_7)
        self.label_63.setGeometry(QtCore.QRect(20, 300, 171, 31))
        self.label_63.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.Loco_Left_Steer = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Left_Steer.setGeometry(QtCore.QRect(20, 340, 191, 71))
        self.Loco_Left_Steer.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Left_Steer.setObjectName(_fromUtf8("Loco_Left_Steer"))
        self.label_64 = QtGui.QLabel(self.frame_7)
        self.label_64.setGeometry(QtCore.QRect(250, 300, 171, 31))
        self.label_64.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.Loco_Right_Steer = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Right_Steer.setGeometry(QtCore.QRect(240, 340, 181, 71))
        self.Loco_Right_Steer.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Right_Steer.setObjectName(_fromUtf8("Loco_Right_Steer"))
        self.label_65 = QtGui.QLabel(self.frame_7)
        self.label_65.setGeometry(QtCore.QRect(20, 430, 171, 31))
        self.label_65.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.label_66 = QtGui.QLabel(self.frame_7)
        self.label_66.setGeometry(QtCore.QRect(240, 430, 171, 31))
        self.label_66.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.Loco_Right_Steer_Vel = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Right_Steer_Vel.setGeometry(QtCore.QRect(240, 470, 181, 71))
        self.Loco_Right_Steer_Vel.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Right_Steer_Vel.setObjectName(_fromUtf8("Loco_Right_Steer_Vel"))
        self.Loco_Left_Steer_Vel = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Left_Steer_Vel.setGeometry(QtCore.QRect(20, 470, 181, 71))
        self.Loco_Left_Steer_Vel.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Left_Steer_Vel.setObjectName(_fromUtf8("Loco_Left_Steer_Vel"))
        self.label_67 = QtGui.QLabel(self.frame_7)
        self.label_67.setGeometry(QtCore.QRect(480, 40, 141, 31))
        self.label_67.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.label_68 = QtGui.QLabel(self.frame_7)
        self.label_68.setGeometry(QtCore.QRect(480, 170, 131, 31))
        self.label_68.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.label_69 = QtGui.QLabel(self.frame_7)
        self.label_69.setGeometry(QtCore.QRect(480, 300, 131, 31))
        self.label_69.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.Loco_Pan_Joy = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Pan_Joy.setGeometry(QtCore.QRect(440, 80, 171, 71))
        self.Loco_Pan_Joy.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Pan_Joy.setObjectName(_fromUtf8("Loco_Pan_Joy"))
        self.Loco_Tilt_Joy = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Tilt_Joy.setGeometry(QtCore.QRect(450, 210, 171, 71))
        self.Loco_Tilt_Joy.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Tilt_Joy.setObjectName(_fromUtf8("Loco_Tilt_Joy"))
        self.Loco_Mode = QtGui.QPlainTextEdit(self.frame_7)
        self.Loco_Mode.setGeometry(QtCore.QRect(450, 340, 181, 71))
        self.Loco_Mode.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Loco_Mode.setObjectName(_fromUtf8("Loco_Mode"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.frame_11 = QtGui.QFrame(self.tab_2)
        self.frame_11.setGeometry(QtCore.QRect(290, 150, 591, 351))
        self.frame_11.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.label_49 = QtGui.QLabel(self.frame_11)
        self.label_49.setGeometry(QtCore.QRect(60, 10, 201, 51))
        self.label_49.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_49.setScaledContents(False)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.Luminosity = QtGui.QPlainTextEdit(self.frame_11)
        self.Luminosity.setGeometry(QtCore.QRect(10, 120, 171, 41))
        self.Luminosity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Luminosity.setObjectName(_fromUtf8("Luminosity"))
        self.Altitude = QtGui.QPlainTextEdit(self.frame_11)
        self.Altitude.setGeometry(QtCore.QRect(220, 120, 161, 41))
        self.Altitude.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Altitude.setObjectName(_fromUtf8("Altitude"))
        self.Absolute_Pressure = QtGui.QPlainTextEdit(self.frame_11)
        self.Absolute_Pressure.setGeometry(QtCore.QRect(400, 120, 171, 41))
        self.Absolute_Pressure.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Absolute_Pressure.setObjectName(_fromUtf8("Absolute_Pressure"))
        self.CPM = QtGui.QPlainTextEdit(self.frame_11)
        self.CPM.setGeometry(QtCore.QRect(220, 230, 161, 31))
        self.CPM.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.CPM.setObjectName(_fromUtf8("CPM"))
        self.label_50 = QtGui.QLabel(self.frame_11)
        self.label_50.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.label_50.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.label_51 = QtGui.QLabel(self.frame_11)
        self.label_51.setGeometry(QtCore.QRect(220, 90, 91, 31))
        self.label_51.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.label_52 = QtGui.QLabel(self.frame_11)
        self.label_52.setGeometry(QtCore.QRect(220, 200, 131, 31))
        self.label_52.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_53 = QtGui.QLabel(self.frame_11)
        self.label_53.setGeometry(QtCore.QRect(10, 190, 171, 31))
        self.label_53.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.UVIntensity = QtGui.QPlainTextEdit(self.frame_11)
        self.UVIntensity.setGeometry(QtCore.QRect(10, 230, 171, 31))
        self.UVIntensity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.UVIntensity.setObjectName(_fromUtf8("UVIntensity"))
        self.label_54 = QtGui.QLabel(self.frame_11)
        self.label_54.setGeometry(QtCore.QRect(20, 270, 151, 31))
        self.label_54.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.label_55 = QtGui.QLabel(self.frame_11)
        self.label_55.setGeometry(QtCore.QRect(410, 90, 161, 31))
        self.label_55.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.label_56 = QtGui.QLabel(self.frame_11)
        self.label_56.setGeometry(QtCore.QRect(400, 200, 141, 31))
        self.label_56.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.Soil_Temperature = QtGui.QPlainTextEdit(self.frame_11)
        self.Soil_Temperature.setGeometry(QtCore.QRect(400, 230, 181, 31))
        self.Soil_Temperature.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Soil_Temperature.setObjectName(_fromUtf8("Soil_Temperature"))
        self.label_57 = QtGui.QLabel(self.frame_11)
        self.label_57.setGeometry(QtCore.QRect(220, 270, 121, 31))
        self.label_57.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.Relative_Humidity = QtGui.QPlainTextEdit(self.frame_11)
        self.Relative_Humidity.setGeometry(QtCore.QRect(10, 300, 171, 41))
        self.Relative_Humidity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Relative_Humidity.setObjectName(_fromUtf8("Relative_Humidity"))
        self.Temperature = QtGui.QPlainTextEdit(self.frame_11)
        self.Temperature.setGeometry(QtCore.QRect(220, 300, 171, 41))
        self.Temperature.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Temperature.setObjectName(_fromUtf8("Temperature"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.frame_9 = QtGui.QFrame(self.tab_4)
        self.frame_9.setGeometry(QtCore.QRect(0, 10, 421, 131))
        self.frame_9.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.Yaw = QtGui.QPlainTextEdit(self.frame_9)
        self.Yaw.setGeometry(QtCore.QRect(40, 50, 221, 61))
        self.Yaw.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Yaw.setObjectName(_fromUtf8("Yaw"))
        self.label_34 = QtGui.QLabel(self.frame_9)
        self.label_34.setGeometry(QtCore.QRect(160, 10, 81, 31))
        self.label_34.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.frame_9)
        self.label_35.setGeometry(QtCore.QRect(40, 10, 261, 31))
        self.label_35.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.frame_12 = QtGui.QFrame(self.tab_4)
        self.frame_12.setGeometry(QtCore.QRect(0, 150, 351, 131))
        self.frame_12.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))
        self.Status = QtGui.QPlainTextEdit(self.frame_12)
        self.Status.setGeometry(QtCore.QRect(40, 50, 221, 61))
        self.Status.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Status.setObjectName(_fromUtf8("Status"))
        self.label_58 = QtGui.QLabel(self.frame_12)
        self.label_58.setGeometry(QtCore.QRect(40, 10, 111, 31))
        self.label_58.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.frame_6 = QtGui.QFrame(self.tab_4)
        self.frame_6.setGeometry(QtCore.QRect(10, 290, 321, 331))
        self.frame_6.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.label_21 = QtGui.QLabel(self.frame_6)
        self.label_21.setGeometry(QtCore.QRect(130, 10, 71, 51))
        self.label_21.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_21.setScaledContents(False)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.Bearing = QtGui.QPlainTextEdit(self.frame_6)
        self.Bearing.setGeometry(QtCore.QRect(20, 110, 111, 71))
        self.Bearing.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Bearing.setObjectName(_fromUtf8("Bearing"))
        self.Distance = QtGui.QPlainTextEdit(self.frame_6)
        self.Distance.setGeometry(QtCore.QRect(180, 110, 111, 71))
        self.Distance.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Distance.setObjectName(_fromUtf8("Distance"))
        self.Stop = QtGui.QPlainTextEdit(self.frame_6)
        self.Stop.setGeometry(QtCore.QRect(20, 240, 111, 71))
        self.Stop.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Stop.setObjectName(_fromUtf8("Stop"))
        self.State = QtGui.QPlainTextEdit(self.frame_6)
        self.State.setGeometry(QtCore.QRect(180, 230, 121, 71))
        self.State.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.State.setObjectName(_fromUtf8("State"))
        self.label_31 = QtGui.QLabel(self.frame_6)
        self.label_31.setGeometry(QtCore.QRect(20, 60, 141, 31))
        self.label_31.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_43 = QtGui.QLabel(self.frame_6)
        self.label_43.setGeometry(QtCore.QRect(180, 60, 101, 31))
        self.label_43.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.label_45 = QtGui.QLabel(self.frame_6)
        self.label_45.setGeometry(QtCore.QRect(20, 190, 151, 31))
        self.label_45.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.label_46 = QtGui.QLabel(self.frame_6)
        self.label_46.setGeometry(QtCore.QRect(180, 190, 131, 31))
        self.label_46.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Team Anveshak", None))
        self.Serial_Node.setText(_translate("MainWindow", "Serial Node", None))
        self.Drive_2.setText(_translate("MainWindow", "Drive", None))
        self.Drive1_2.setText(_translate("MainWindow", "Drive1", None))
        self.Drive_Diff_2.setText(_translate("MainWindow", "Drive_Diff", None))
        self.label_6.setText(_translate("MainWindow", "N O D E S ", None))
        self.Locomotion_Control_2.setText(_translate("MainWindow", "Locomotion_Contr", None))
        self.GUI_Pinger.setText(_translate("MainWindow", "GUI_Pinger", None))
        self.GUI_Subscriber.setText(_translate("MainWindow", "GUI_Subscriber", None))
        self.Joy_Node_2.setText(_translate("MainWindow", "Joy_Node", None))
        self.button2_2.setText(_translate("MainWindow", "RUN LOGGER", None))
        self.run_3.setText(_translate("MainWindow", "RUN ROVER", None))
        self.label_25.setText(_translate("MainWindow", "IP_Address", None))
        self.label_12.setText(_translate("MainWindow", "NODE INFORMATION", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "NODE_DETECTION", None))
        self.label_19.setText(_translate("MainWindow", "DIAGNOSTICS WHEEL", None))
        self.label_20.setText(_translate("MainWindow", "Right Front Velocity", None))
        self.label_22.setText(_translate("MainWindow", "Left Front Velocity", None))
        self.label_23.setText(_translate("MainWindow", "Right Back Velocity", None))
        self.label_24.setText(_translate("MainWindow", "Left Back Velocity", None))
        self.label_26.setText(_translate("MainWindow", "Left Pot", None))
        self.label_27.setText(_translate("MainWindow", "Right Rot", None))
        self.label_41.setText(_translate("MainWindow", "Left Pot Zero", None))
        self.label_42.setText(_translate("MainWindow", "Right Pot Zero", None))
        self.label_28.setText(_translate("MainWindow", "DIAGNOSTICS WHEEL", None))
        self.label_29.setText(_translate("MainWindow", "Right Front Velocity", None))
        self.label_30.setText(_translate("MainWindow", "Left Front Velocity", None))
        self.label_32.setText(_translate("MainWindow", "Right Back Velocity", None))
        self.label_33.setText(_translate("MainWindow", "Left Back Velocity", None))
        self.label_37.setText(_translate("MainWindow", "Left Pot", None))
        self.label_38.setText(_translate("MainWindow", "Right Rot", None))
        self.label_44.setText(_translate("MainWindow", "Left Pot Zero", None))
        self.label_59.setText(_translate("MainWindow", "Right Pot Zero", None))
        self.label_36.setText(_translate("MainWindow", "S E T", None))
        self.label_47.setText(_translate("MainWindow", "M O T O R 1", None))
        self.label_48.setText(_translate("MainWindow", "M O T O R 2", None))
        self.label_39.setText(_translate("MainWindow", "LOCOMOTION WHEEL", None))
        self.label_40.setText(_translate("MainWindow", "Right Front Velocity", None))
        self.label_60.setText(_translate("MainWindow", "Left Front Velocity", None))
        self.label_61.setText(_translate("MainWindow", "Right Back Velocity", None))
        self.label_62.setText(_translate("MainWindow", "Left Back Velocity", None))
        self.label_63.setText(_translate("MainWindow", "Left Steer", None))
        self.label_64.setText(_translate("MainWindow", "Right Steer", None))
        self.label_65.setText(_translate("MainWindow", "Left Steer Vel", None))
        self.label_66.setText(_translate("MainWindow", "Right Steer Vel", None))
        self.label_67.setText(_translate("MainWindow", "Pan_Joy", None))
        self.label_68.setText(_translate("MainWindow", "Tilt_Joy", None))
        self.label_69.setText(_translate("MainWindow", "Mode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ERDT + EQST", None))
        self.label_49.setText(_translate("MainWindow", "S E N S O R   D A T A ", None))
        self.label_50.setText(_translate("MainWindow", "Luminosity (Lux)", None))
        self.label_51.setText(_translate("MainWindow", "Altitude (m)", None))
        self.label_52.setText(_translate("MainWindow", "Counts per Minute", None))
        self.label_53.setText(_translate("MainWindow", "UV Intensity (mW/cm2)", None))
        self.label_54.setText(_translate("MainWindow", "Relative Humidity(%)", None))
        self.label_55.setText(_translate("MainWindow", "Absolute Pressure(mb)", None))
        self.label_56.setText(_translate("MainWindow", "Soil Temperature (C)", None))
        self.label_57.setText(_translate("MainWindow", "Temperature (C)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Science_Task", None))
        self.label_34.setText(_translate("MainWindow", "Yaw", None))
        self.label_35.setText(_translate("MainWindow", "IMU", None))
        self.label_58.setText(_translate("MainWindow", "S T A T U S", None))
        self.label_21.setText(_translate("MainWindow", "G  O A L", None))
        self.label_31.setText(_translate("MainWindow", "Bearing", None))
        self.label_43.setText(_translate("MainWindow", "Distance", None))
        self.label_45.setText(_translate("MainWindow", "Stop", None))
        self.label_46.setText(_translate("MainWindow", "State", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Autonomous", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

