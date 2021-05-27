# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(927, 543)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(92, 92, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 8px;\n"
"\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_title.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 40))
        self.frame_btns.setStyleSheet(u"background-color: none;")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 0, 150), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 150), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius:8px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 150), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color:none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background-color: none;")
        self.horizontalLayout_5 = QHBoxLayout(self.page_home)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_content_home)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_circle_3 = QFrame(self.frame)
        self.frame_circle_3.setObjectName(u"frame_circle_3")
        self.frame_circle_3.setMinimumSize(QSize(250, 250))
        self.frame_circle_3.setMaximumSize(QSize(250, 250))
        self.frame_circle_3.setStyleSheet(u"QFrame {\n"
"	border: 5px solid rgb(116, 255, 255);\n"
"	border-radius: 125px\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(0, 94, 94)\n"
"}")
        self.frame_circle_3.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_circle_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(60, 30, 131, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"border:none;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame_circle_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 70, 171, 91))
        font2 = QFont()
        font2.setFamily(u"MV Boli")
        font2.setPointSize(60)
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"border:none;\n"
"color: rgb(105, 138, 255);")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_19 = QLabel(self.frame_circle_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(70, 170, 111, 21))
        self.label_19.setStyleSheet(u"border:none;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.frame_circle_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(70, 200, 111, 21))
        self.label_20.setStyleSheet(u"border:none;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.frame_circle_3)

        self.frame_circle_ram = QFrame(self.frame)
        self.frame_circle_ram.setObjectName(u"frame_circle_ram")
        self.frame_circle_ram.setMinimumSize(QSize(250, 250))
        self.frame_circle_ram.setMaximumSize(QSize(250, 250))
        self.frame_circle_ram.setStyleSheet(u"QFrame {\n"
"	border: 5px solid rgb(116, 255, 255);\n"
"	border-radius: 125px\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(0, 94, 94)\n"
"}")
        self.frame_circle_ram.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_ram.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_circle_ram)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 131, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border:none;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_circle_ram)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 171, 91))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border:none;\n"
"color: rgb(105, 138, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame_circle_ram)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 170, 111, 21))
        self.label_3.setStyleSheet(u"border:none;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frame_circle_ram)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 200, 111, 21))
        self.label_4.setStyleSheet(u"border:none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.frame_circle_ram)

        self.frame_circle_gpu = QFrame(self.frame)
        self.frame_circle_gpu.setObjectName(u"frame_circle_gpu")
        self.frame_circle_gpu.setMinimumSize(QSize(250, 250))
        self.frame_circle_gpu.setMaximumSize(QSize(250, 250))
        self.frame_circle_gpu.setStyleSheet(u"QFrame {\n"
"	border: 5px solid rgb(116, 255, 255);\n"
"	border-radius: 125px\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 5px solid rgb(0, 94, 94)\n"
"}")
        self.frame_circle_gpu.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_gpu.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_circle_gpu)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 30, 131, 31))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"border:none;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_14 = QLabel(self.frame_circle_gpu)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 70, 171, 91))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"border:none;\n"
"color: rgb(105, 138, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.frame_circle_gpu)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(70, 170, 111, 21))
        self.label_15.setStyleSheet(u"border:none;")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.frame_circle_gpu)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(70, 200, 111, 21))
        self.label_16.setStyleSheet(u"border:none;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.frame_circle_gpu)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_title_2 = QFrame(self.frame_content_home)
        self.frame_title_2.setObjectName(u"frame_title_2")
        self.frame_title_2.setMaximumSize(QSize(16777215, 100))
        self.frame_title_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_title_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.frame_title_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(500, 60))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setItalic(True)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"background-color: rgb(85, 85, 0);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_9)


        self.verticalLayout_3.addWidget(self.frame_title_2)


        self.horizontalLayout_5.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.page_home)
        self.page_title = QWidget()
        self.page_title.setObjectName(u"page_title")
        self.page_title.setStyleSheet(u"background-color: none;")
        self.stackedWidget.addWidget(self.page_title)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(0, 30))
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: none;")
        self.credits_bar.setFrameShape(QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.label_text = QLabel(self.credits_bar)
        self.label_text.setObjectName(u"label_text")

        self.horizontalLayout_4.addWidget(self.label_text)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"This is my App - Title Bar", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Resize Window", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CPU USAGE", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"25%", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"intel i9-9900k: 8 core", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Temp 45C", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"GPU USAGE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"40%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RTX 3080Ti", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Temp 45C", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"RAM USAGE", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total 64GB", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Temp 45C", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"If you control the code, you control the World", None))
        self.label_text.setText(QCoreApplication.translate("MainWindow", u"By: Truong Cao", None))
    # retranslateUi

