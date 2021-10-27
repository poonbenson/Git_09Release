# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bigKeeperPyUi_newLayout_v127.ui'
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
        MainWindow.resize(477, 829)
        MainWindow.setMinimumSize(QSize(432, 829))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_openCal = QPushButton(self.centralwidget)
        self.pushButton_openCal.setObjectName(u"pushButton_openCal")

        self.horizontalLayout_9.addWidget(self.pushButton_openCal)

        self.pushButton_openCal2 = QPushButton(self.centralwidget)
        self.pushButton_openCal2.setObjectName(u"pushButton_openCal2")

        self.horizontalLayout_9.addWidget(self.pushButton_openCal2)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_8 = QLabel(self.splitter)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setMaximumSize(QSize(100, 16777215))
        self.splitter.addWidget(self.label_8)
        self.comboBoxProjects = QComboBox(self.splitter)
        self.comboBoxProjects.setObjectName(u"comboBoxProjects")
        self.splitter.addWidget(self.comboBoxProjects)

        self.horizontalLayout_8.addWidget(self.splitter)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_8.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_shotlist = QPushButton(self.centralwidget)
        self.pushButton_shotlist.setObjectName(u"pushButton_shotlist")

        self.horizontalLayout_10.addWidget(self.pushButton_shotlist)

        self.pushButton_roughcut = QPushButton(self.centralwidget)
        self.pushButton_roughcut.setObjectName(u"pushButton_roughcut")

        self.horizontalLayout_10.addWidget(self.pushButton_roughcut)

        self.pushButton_dailyFolder2 = QPushButton(self.centralwidget)
        self.pushButton_dailyFolder2.setObjectName(u"pushButton_dailyFolder2")

        self.horizontalLayout_10.addWidget(self.pushButton_dailyFolder2)

        self.pushButton_commentClient = QPushButton(self.centralwidget)
        self.pushButton_commentClient.setObjectName(u"pushButton_commentClient")

        self.horizontalLayout_10.addWidget(self.pushButton_commentClient)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u"../../../bigKeeper/bigKeeperIcon.jpg"))

        self.verticalLayout.addWidget(self.label_9)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_currentOpen = QWidget()
        self.tab_currentOpen.setObjectName(u"tab_currentOpen")
        self.pushButton_versionUp = QPushButton(self.tab_currentOpen)
        self.pushButton_versionUp.setObjectName(u"pushButton_versionUp")
        self.pushButton_versionUp.setGeometry(QRect(0, 100, 171, 23))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        self.pushButton_versionUp.setFont(font)
        self.pushButton_revive = QPushButton(self.tab_currentOpen)
        self.pushButton_revive.setObjectName(u"pushButton_revive")
        self.pushButton_revive.setGeometry(QRect(0, 160, 71, 23))
        self.pushButton_getFrameRange = QPushButton(self.tab_currentOpen)
        self.pushButton_getFrameRange.setObjectName(u"pushButton_getFrameRange")
        self.pushButton_getFrameRange.setGeometry(QRect(0, 190, 171, 41))
        self.pushButton_NukeReadNodeTempTool = QPushButton(self.tab_currentOpen)
        self.pushButton_NukeReadNodeTempTool.setObjectName(u"pushButton_NukeReadNodeTempTool")
        self.pushButton_NukeReadNodeTempTool.setGeometry(QRect(0, 240, 171, 41))
        self.tabWidget_2 = QTabWidget(self.tab_currentOpen)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 290, 451, 311))
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.tabWidget_2.setFont(font1)
        self.tabMaya = QWidget()
        self.tabMaya.setObjectName(u"tabMaya")
        self.tabWidget_2.addTab(self.tabMaya, "")
        self.tabNuke = QWidget()
        self.tabNuke.setObjectName(u"tabNuke")
        self.pushButton_closeNukeScript = QPushButton(self.tabNuke)
        self.pushButton_closeNukeScript.setObjectName(u"pushButton_closeNukeScript")
        self.pushButton_closeNukeScript.setGeometry(QRect(0, 250, 121, 23))
        self.pushButton_genWriteCompMaster = QPushButton(self.tabNuke)
        self.pushButton_genWriteCompMaster.setObjectName(u"pushButton_genWriteCompMaster")
        self.pushButton_genWriteCompMaster.setGeometry(QRect(0, 150, 121, 23))
        self.pushButton_genWriteLayerMask = QPushButton(self.tabNuke)
        self.pushButton_genWriteLayerMask.setObjectName(u"pushButton_genWriteLayerMask")
        self.pushButton_genWriteLayerMask.setGeometry(QRect(0, 170, 121, 23))
        self.label_16 = QLabel(self.tabNuke)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 130, 121, 16))
        self.label_21 = QLabel(self.tabNuke)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 80, 121, 16))
        self.pushButton_genWritePrerend = QPushButton(self.tabNuke)
        self.pushButton_genWritePrerend.setObjectName(u"pushButton_genWritePrerend")
        self.pushButton_genWritePrerend.setGeometry(QRect(0, 100, 121, 23))
        self.tabWidget_2.addTab(self.tabNuke, "")
        self.tabHoudini = QWidget()
        self.tabHoudini.setObjectName(u"tabHoudini")
        self.tabWidget_2.addTab(self.tabHoudini, "")
        self.tabBlender = QWidget()
        self.tabBlender.setObjectName(u"tabBlender")
        self.tabWidget_2.addTab(self.tabBlender, "")
        self.tabCmd = QWidget()
        self.tabCmd.setObjectName(u"tabCmd")
        self.pushButton_sortoutfile = QPushButton(self.tabCmd)
        self.pushButton_sortoutfile.setObjectName(u"pushButton_sortoutfile")
        self.pushButton_sortoutfile.setGeometry(QRect(200, 30, 75, 23))
        self.label_17 = QLabel(self.tabCmd)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 10, 151, 16))
        self.label_17.setTextFormat(Qt.PlainText)
        self.pushButton_exeDel = QPushButton(self.tabCmd)
        self.pushButton_exeDel.setObjectName(u"pushButton_exeDel")
        self.pushButton_exeDel.setGeometry(QRect(370, 30, 31, 23))
        self.label_18 = QLabel(self.tabCmd)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 30, 211, 16))
        self.label_19 = QLabel(self.tabCmd)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(300, 30, 71, 16))
        self.tabWidget_2.addTab(self.tabCmd, "")
        self.tabLauncher = QWidget()
        self.tabLauncher.setObjectName(u"tabLauncher")
        self.groupBox = QGroupBox(self.tabLauncher)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 331, 251))
        self.pushButton_LaunchNuke13_0_v2 = QPushButton(self.groupBox)
        self.pushButton_LaunchNuke13_0_v2.setObjectName(u"pushButton_LaunchNuke13_0_v2")
        self.pushButton_LaunchNuke13_0_v2.setGeometry(QRect(50, 70, 61, 41))
        self.pushButton_LaunchNukeStudio13_0_v2 = QPushButton(self.groupBox)
        self.pushButton_LaunchNukeStudio13_0_v2.setObjectName(u"pushButton_LaunchNukeStudio13_0_v2")
        self.pushButton_LaunchNukeStudio13_0_v2.setGeometry(QRect(190, 70, 41, 41))
        self.pushButton_LaunchNukeX13_0_v2 = QPushButton(self.groupBox)
        self.pushButton_LaunchNukeX13_0_v2.setObjectName(u"pushButton_LaunchNukeX13_0_v2")
        self.pushButton_LaunchNukeX13_0_v2.setGeometry(QRect(110, 70, 41, 41))
        self.pushButton_LaunchNukeAssist13_0_v2 = QPushButton(self.groupBox)
        self.pushButton_LaunchNukeAssist13_0_v2.setObjectName(u"pushButton_LaunchNukeAssist13_0_v2")
        self.pushButton_LaunchNukeAssist13_0_v2.setGeometry(QRect(150, 70, 41, 41))
        self.pushButton_LaunchMaya2022_update0 = QPushButton(self.groupBox)
        self.pushButton_LaunchMaya2022_update0.setObjectName(u"pushButton_LaunchMaya2022_update0")
        self.pushButton_LaunchMaya2022_update0.setGeometry(QRect(50, 30, 181, 41))
        self.pushButton_mayaOther = QPushButton(self.groupBox)
        self.pushButton_mayaOther.setObjectName(u"pushButton_mayaOther")
        self.pushButton_mayaOther.setGeometry(QRect(230, 30, 16, 41))
        self.pushButton_nukeOther = QPushButton(self.groupBox)
        self.pushButton_nukeOther.setObjectName(u"pushButton_nukeOther")
        self.pushButton_nukeOther.setGeometry(QRect(230, 70, 16, 41))
        self.label_mayaIcon = QLabel(self.groupBox)
        self.label_mayaIcon.setObjectName(u"label_mayaIcon")
        self.label_mayaIcon.setGeometry(QRect(10, 30, 41, 41))
        self.label_nukeIcon = QLabel(self.groupBox)
        self.label_nukeIcon.setObjectName(u"label_nukeIcon")
        self.label_nukeIcon.setGeometry(QRect(10, 70, 41, 41))
        self.pushButton_dailyFolder = QPushButton(self.groupBox)
        self.pushButton_dailyFolder.setObjectName(u"pushButton_dailyFolder")
        self.pushButton_dailyFolder.setGeometry(QRect(50, 150, 181, 41))
        self.pushButton_launchHoudini1 = QPushButton(self.groupBox)
        self.pushButton_launchHoudini1.setObjectName(u"pushButton_launchHoudini1")
        self.pushButton_launchHoudini1.setGeometry(QRect(50, 110, 181, 41))
        self.pushButton_houdiniOther = QPushButton(self.groupBox)
        self.pushButton_houdiniOther.setObjectName(u"pushButton_houdiniOther")
        self.pushButton_houdiniOther.setGeometry(QRect(230, 110, 16, 41))
        self.label_houdiniIcon = QLabel(self.groupBox)
        self.label_houdiniIcon.setObjectName(u"label_houdiniIcon")
        self.label_houdiniIcon.setGeometry(QRect(10, 110, 41, 41))
        self.pushButton_LaunchNuke13_0_v2.raise_()
        self.pushButton_LaunchNukeStudio13_0_v2.raise_()
        self.pushButton_LaunchNukeX13_0_v2.raise_()
        self.pushButton_LaunchNukeAssist13_0_v2.raise_()
        self.pushButton_LaunchMaya2022_update0.raise_()
        self.pushButton_mayaOther.raise_()
        self.pushButton_nukeOther.raise_()
        self.label_mayaIcon.raise_()
        self.label_nukeIcon.raise_()
        self.pushButton_dailyFolder.raise_()
        self.pushButton_houdiniOther.raise_()
        self.label_houdiniIcon.raise_()
        self.pushButton_launchHoudini1.raise_()
        self.tabWidget_2.addTab(self.tabLauncher, "")
        self.tabMisc = QWidget()
        self.tabMisc.setObjectName(u"tabMisc")
        self.pushButton_miscCookbook = QPushButton(self.tabMisc)
        self.pushButton_miscCookbook.setObjectName(u"pushButton_miscCookbook")
        self.pushButton_miscCookbook.setGeometry(QRect(10, 30, 121, 23))
        self.label_22 = QLabel(self.tabMisc)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 121, 16))
        self.pushButton_miscLoginInfo = QPushButton(self.tabMisc)
        self.pushButton_miscLoginInfo.setObjectName(u"pushButton_miscLoginInfo")
        self.pushButton_miscLoginInfo.setGeometry(QRect(10, 60, 121, 23))
        self.pushButton_miscStaffContact = QPushButton(self.tabMisc)
        self.pushButton_miscStaffContact.setObjectName(u"pushButton_miscStaffContact")
        self.pushButton_miscStaffContact.setGeometry(QRect(10, 90, 121, 23))
        self.tabWidget_2.addTab(self.tabMisc, "")
        self.pushButton_scnUpdate = QPushButton(self.tab_currentOpen)
        self.pushButton_scnUpdate.setObjectName(u"pushButton_scnUpdate")
        self.pushButton_scnUpdate.setGeometry(QRect(80, 160, 91, 23))
        self.tabWidget.addTab(self.tab_currentOpen, "")
        self.tab_shotBrowser = QWidget()
        self.tab_shotBrowser.setObjectName(u"tab_shotBrowser")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_shotBrowser)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.tab_shotBrowser)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_5.addWidget(self.label_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.tab_shotBrowser)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_12.addWidget(self.label_5)

        self.pushButton_listWidget1Refresh = QPushButton(self.tab_shotBrowser)
        self.pushButton_listWidget1Refresh.setObjectName(u"pushButton_listWidget1Refresh")
        self.pushButton_listWidget1Refresh.setMinimumSize(QSize(0, 23))
        self.pushButton_listWidget1Refresh.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_12.addWidget(self.pushButton_listWidget1Refresh)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.listWidget_1 = QListWidget(self.tab_shotBrowser)
        self.listWidget_1.setObjectName(u"listWidget_1")
        self.listWidget_1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.listWidget_1)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_7 = QLabel(self.tab_shotBrowser)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_13.addWidget(self.label_7)

        self.label_20 = QLabel(self.tab_shotBrowser)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_13.addWidget(self.label_20)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.listWidget_2 = QListWidget(self.tab_shotBrowser)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_3.addWidget(self.listWidget_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.tab_shotBrowser)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 23))

        self.verticalLayout_4.addWidget(self.label_6)

        self.pushButton_CompLatestRv = QPushButton(self.tab_shotBrowser)
        self.pushButton_CompLatestRv.setObjectName(u"pushButton_CompLatestRv")

        self.verticalLayout_4.addWidget(self.pushButton_CompLatestRv)

        self.pushButton_shotAction = QPushButton(self.tab_shotBrowser)
        self.pushButton_shotAction.setObjectName(u"pushButton_shotAction")

        self.verticalLayout_4.addWidget(self.pushButton_shotAction)

        self.listWidget_3 = QListWidget(self.tab_shotBrowser)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(0, 200))
        self.listWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_4.addWidget(self.listWidget_3)

        self.pushButton_newTask = QPushButton(self.tab_shotBrowser)
        self.pushButton_newTask.setObjectName(u"pushButton_newTask")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_newTask.sizePolicy().hasHeightForWidth())
        self.pushButton_newTask.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.pushButton_newTask)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_Location = QLineEdit(self.tab_shotBrowser)
        self.lineEdit_Location.setObjectName(u"lineEdit_Location")

        self.horizontalLayout_4.addWidget(self.lineEdit_Location)

        self.pushButton_19 = QPushButton(self.tab_shotBrowser)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_4.addWidget(self.pushButton_19)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.tab_shotBrowser, "")
        self.tab_developing = QWidget()
        self.tab_developing.setObjectName(u"tab_developing")
        self.layoutWidget_2 = QWidget(self.tab_developing)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 160, 320, 112))
        self.gridLayout = QGridLayout(self.layoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_num9 = QPushButton(self.layoutWidget_2)
        self.pushButton_num9.setObjectName(u"pushButton_num9")

        self.gridLayout.addWidget(self.pushButton_num9, 0, 0, 1, 1)

        self.pushButton_num8 = QPushButton(self.layoutWidget_2)
        self.pushButton_num8.setObjectName(u"pushButton_num8")

        self.gridLayout.addWidget(self.pushButton_num8, 0, 1, 1, 1)

        self.pushButton_num7 = QPushButton(self.layoutWidget_2)
        self.pushButton_num7.setObjectName(u"pushButton_num7")

        self.gridLayout.addWidget(self.pushButton_num7, 0, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.layoutWidget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 0, 3, 1, 1)

        self.pushButton_num6 = QPushButton(self.layoutWidget_2)
        self.pushButton_num6.setObjectName(u"pushButton_num6")

        self.gridLayout.addWidget(self.pushButton_num6, 1, 0, 1, 1)

        self.pushButton_num5 = QPushButton(self.layoutWidget_2)
        self.pushButton_num5.setObjectName(u"pushButton_num5")

        self.gridLayout.addWidget(self.pushButton_num5, 1, 1, 1, 1)

        self.pushButton_num4 = QPushButton(self.layoutWidget_2)
        self.pushButton_num4.setObjectName(u"pushButton_num4")

        self.gridLayout.addWidget(self.pushButton_num4, 1, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.layoutWidget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 1, 3, 1, 1)

        self.pushButton_num3 = QPushButton(self.layoutWidget_2)
        self.pushButton_num3.setObjectName(u"pushButton_num3")

        self.gridLayout.addWidget(self.pushButton_num3, 2, 0, 1, 1)

        self.pushButton_num2 = QPushButton(self.layoutWidget_2)
        self.pushButton_num2.setObjectName(u"pushButton_num2")

        self.gridLayout.addWidget(self.pushButton_num2, 2, 1, 1, 1)

        self.pushButton_num1 = QPushButton(self.layoutWidget_2)
        self.pushButton_num1.setObjectName(u"pushButton_num1")

        self.gridLayout.addWidget(self.pushButton_num1, 2, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.layoutWidget_2)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 2, 3, 1, 1)

        self.pushButton_calculate = QPushButton(self.layoutWidget_2)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")

        self.gridLayout.addWidget(self.pushButton_calculate, 3, 0, 1, 3)

        self.pushButton_16 = QPushButton(self.layoutWidget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout.addWidget(self.pushButton_16, 3, 3, 1, 1)

        self.layoutWidget_3 = QWidget(self.tab_developing)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 290, 158, 77))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 2)

        self.label_4 = QLabel(self.layoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 2)

        self.pushButton_17 = QPushButton(self.layoutWidget_3)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_2.addWidget(self.pushButton_17, 2, 0, 1, 2)

        self.pushButton_18 = QPushButton(self.layoutWidget_3)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_2.addWidget(self.pushButton_18, 2, 2, 1, 1)

        self.layoutWidget_4 = QWidget(self.tab_developing)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 20, 251, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_childUi = QPushButton(self.layoutWidget_4)
        self.pushButton_childUi.setObjectName(u"pushButton_childUi")

        self.horizontalLayout.addWidget(self.pushButton_childUi)

        self.layoutWidget_5 = QWidget(self.tab_developing)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 60, 251, 72))
        self.gridLayout_3 = QGridLayout(self.layoutWidget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_action1 = QPushButton(self.layoutWidget_5)
        self.pushButton_action1.setObjectName(u"pushButton_action1")

        self.horizontalLayout_2.addWidget(self.pushButton_action1)

        self.pushButton_7zip = QPushButton(self.layoutWidget_5)
        self.pushButton_7zip.setObjectName(u"pushButton_7zip")

        self.horizontalLayout_2.addWidget(self.pushButton_7zip)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 2, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.toolButton = QToolButton(self.tab_developing)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(190, 290, 151, 19))
        self.pushButton_Location_2 = QPushButton(self.tab_developing)
        self.pushButton_Location_2.setObjectName(u"pushButton_Location_2")
        self.pushButton_Location_2.setGeometry(QRect(350, 480, 61, 23))
        self.lineEdit_Location_2 = QLineEdit(self.tab_developing)
        self.lineEdit_Location_2.setObjectName(u"lineEdit_Location_2")
        self.lineEdit_Location_2.setGeometry(QRect(20, 480, 321, 20))
        self.label_10 = QLabel(self.tab_developing)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 460, 321, 16))
        self.pushButton_overrideFrameRange = QPushButton(self.tab_developing)
        self.pushButton_overrideFrameRange.setObjectName(u"pushButton_overrideFrameRange")
        self.pushButton_overrideFrameRange.setGeometry(QRect(190, 380, 151, 23))
        self.toolButton_shotAction = QToolButton(self.tab_developing)
        self.toolButton_shotAction.setObjectName(u"toolButton_shotAction")
        self.toolButton_shotAction.setGeometry(QRect(190, 360, 123, 19))
        sizePolicy1.setHeightForWidth(self.toolButton_shotAction.sizePolicy().hasHeightForWidth())
        self.toolButton_shotAction.setSizePolicy(sizePolicy1)
        self.tabWidget.addTab(self.tab_developing, "")
        self.tab_assetBrowser = QWidget()
        self.tab_assetBrowser.setObjectName(u"tab_assetBrowser")
        self.verticalLayout_10 = QVBoxLayout(self.tab_assetBrowser)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_12 = QLabel(self.tab_assetBrowser)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_13 = QLabel(self.tab_assetBrowser)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)

        self.listWidget_assetType = QListWidget(self.tab_assetBrowser)
        self.listWidget_assetType.setObjectName(u"listWidget_assetType")
        self.listWidget_assetType.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_7.addWidget(self.listWidget_assetType)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.tab_assetBrowser)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.listWidget_asset = QListWidget(self.tab_assetBrowser)
        self.listWidget_asset.setObjectName(u"listWidget_asset")
        self.listWidget_asset.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_8.addWidget(self.listWidget_asset)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_15 = QLabel(self.tab_assetBrowser)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_9.addWidget(self.label_15)

        self.listWidget_assetTask = QListWidget(self.tab_assetBrowser)
        self.listWidget_assetTask.setObjectName(u"listWidget_assetTask")
        self.listWidget_assetTask.setMinimumSize(QSize(0, 200))
        self.listWidget_assetTask.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_9.addWidget(self.listWidget_assetTask)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_Location_3 = QLineEdit(self.tab_assetBrowser)
        self.lineEdit_Location_3.setObjectName(u"lineEdit_Location_3")

        self.horizontalLayout_7.addWidget(self.lineEdit_Location_3)

        self.pushButton_20 = QPushButton(self.tab_assetBrowser)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_7.addWidget(self.pushButton_20)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.verticalLayout_10.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab_assetBrowser, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 477, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_openCal.setText(QCoreApplication.translate("MainWindow", u"Open bpvfx Calendar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_openCal2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_openCal2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_openCal2.setText(QCoreApplication.translate("MainWindow", u"Open bpvfx Calendar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Project Name :", None))
#if QT_CONFIG(tooltip)
        self.comboBoxProjects.setToolTip(QCoreApplication.translate("MainWindow", u"comboBoxProjects", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Open Project Folder in explore.\n"
"(pushButton_2)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"explore...", None))
        self.pushButton_shotlist.setText(QCoreApplication.translate("MainWindow", u"_Shotlist", None))
        self.pushButton_roughcut.setText(QCoreApplication.translate("MainWindow", u"_Roughcut", None))
        self.pushButton_dailyFolder2.setText(QCoreApplication.translate("MainWindow", u"Daily Folder", None))
        self.pushButton_commentClient.setText(QCoreApplication.translate("MainWindow", u"_Comment (of Client)", None))
        self.label_9.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_versionUp.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_versionUp", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_versionUp.setText(QCoreApplication.translate("MainWindow", u"Version Up (Save WIP) ...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_revive.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_revive", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_revive.setText(QCoreApplication.translate("MainWindow", u"Revive...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_getFrameRange.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_getFrameRange", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_getFrameRange.setText(QCoreApplication.translate("MainWindow", u"Get Frame Range\n"
"- output setting -", None))
#if QT_CONFIG(tooltip)
        self.pushButton_NukeReadNodeTempTool.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_NukeReadNodeTempTool", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_NukeReadNodeTempTool.setText(QCoreApplication.translate("MainWindow", u"Get Frame Range\n"
"- Nuke Read Nodes -", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabMaya), QCoreApplication.translate("MainWindow", u"Maya", None))
#if QT_CONFIG(tooltip)
        self.pushButton_closeNukeScript.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_closeNukeScript", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_closeNukeScript.setText(QCoreApplication.translate("MainWindow", u"close Nuke Script", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genWriteCompMaster.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWriteCompMaster", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genWriteCompMaster.setText(QCoreApplication.translate("MainWindow", u"CompMaster (only 1)", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genWriteLayerMask.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWriteLayerMask", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genWriteLayerMask.setText(QCoreApplication.translate("MainWindow", u"LayerMasks", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Output Write Node :", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Prerend Write Node :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genWritePrerend.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWritePrerend", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genWritePrerend.setText(QCoreApplication.translate("MainWindow", u"Prerend", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabNuke), QCoreApplication.translate("MainWindow", u"Nuke", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabHoudini), QCoreApplication.translate("MainWindow", u"Houdini", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabBlender), QCoreApplication.translate("MainWindow", u"Blender", None))
#if QT_CONFIG(tooltip)
        self.pushButton_sortoutfile.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_sortoutfile", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_sortoutfile.setText(QCoreApplication.translate("MainWindow", u"Sort Out", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Clean Up Comp Versions:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_exeDel.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_sortoutfile", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_exeDel.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"1) Sort Out by Keeping Versions & Days :", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"2) Execut Del", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabCmd), QCoreApplication.translate("MainWindow", u"Cmd", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Studio Dedicated Launcher:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchNuke13_0_v2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchNuke13_0_v2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchNuke13_0_v2.setText(QCoreApplication.translate("MainWindow", u"_Nuke\n"
"13.0v2", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchNukeStudio13_0_v2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchNukeStudio13_0_v2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchNukeStudio13_0_v2.setText(QCoreApplication.translate("MainWindow", u"studio", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchNukeX13_0_v2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchNukeX13_0_v2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchNukeX13_0_v2.setText(QCoreApplication.translate("MainWindow", u"X", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchNukeAssist13_0_v2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchNukeAssist13_0_v2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchNukeAssist13_0_v2.setText(QCoreApplication.translate("MainWindow", u"assist", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchMaya2022_update0.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchMaya2022_update0", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchMaya2022_update0.setText(QCoreApplication.translate("MainWindow", u"_Maya 2022 update0", None))
#if QT_CONFIG(tooltip)
        self.pushButton_mayaOther.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_mayaOther", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_mayaOther.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(tooltip)
        self.pushButton_nukeOther.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_nukeOther", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_nukeOther.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(tooltip)
        self.label_mayaIcon.setToolTip(QCoreApplication.translate("MainWindow", u"label_mayaIcon", None))
#endif // QT_CONFIG(tooltip)
        self.label_mayaIcon.setText(QCoreApplication.translate("MainWindow", u"MayaIcon", None))
#if QT_CONFIG(tooltip)
        self.label_nukeIcon.setToolTip(QCoreApplication.translate("MainWindow", u"label_nukeIcon", None))
#endif // QT_CONFIG(tooltip)
        self.label_nukeIcon.setText(QCoreApplication.translate("MainWindow", u"NukeIcon", None))
#if QT_CONFIG(tooltip)
        self.pushButton_dailyFolder.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_dailyFolder", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_dailyFolder.setText(QCoreApplication.translate("MainWindow", u"Daily Folder", None))
#if QT_CONFIG(tooltip)
        self.pushButton_launchHoudini1.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_launchHoudini1", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_launchHoudini1.setText(QCoreApplication.translate("MainWindow", u"launchHoudini1", None))
#if QT_CONFIG(tooltip)
        self.pushButton_houdiniOther.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_houdiniOther", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_houdiniOther.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(tooltip)
        self.label_houdiniIcon.setToolTip(QCoreApplication.translate("MainWindow", u"label_houdiniIcon", None))
#endif // QT_CONFIG(tooltip)
        self.label_houdiniIcon.setText(QCoreApplication.translate("MainWindow", u"HoudiniIcon", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabLauncher), QCoreApplication.translate("MainWindow", u"Launcher", None))
#if QT_CONFIG(tooltip)
        self.pushButton_miscCookbook.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWritePrerend", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_miscCookbook.setText(QCoreApplication.translate("MainWindow", u"_bigKeeper Cookbook", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Misc:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_miscLoginInfo.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWritePrerend", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_miscLoginInfo.setText(QCoreApplication.translate("MainWindow", u"_Login ID & Password", None))
#if QT_CONFIG(tooltip)
        self.pushButton_miscStaffContact.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWritePrerend", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_miscStaffContact.setText(QCoreApplication.translate("MainWindow", u"_Staff Contact", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabMisc), QCoreApplication.translate("MainWindow", u"Misc.", None))
#if QT_CONFIG(tooltip)
        self.pushButton_scnUpdate.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_scnUpdate", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_scnUpdate.setText(QCoreApplication.translate("MainWindow", u"Scene Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_currentOpen), QCoreApplication.translate("MainWindow", u"Currently Open", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"SHOT BROWSER", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sequence", None))
#if QT_CONFIG(tooltip)
        self.pushButton_listWidget1Refresh.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_listWidget1Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_listWidget1Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.listWidget_1.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_1", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Shot", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("MainWindow", u"label_20", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText("")
#if QT_CONFIG(tooltip)
        self.listWidget_2.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_2", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Task Shot", None))
#if QT_CONFIG(tooltip)
        self.pushButton_CompLatestRv.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_CompLatestRv", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_CompLatestRv.setText(QCoreApplication.translate("MainWindow", u"tmp.RvCompLastVer", None))
#if QT_CONFIG(tooltip)
        self.pushButton_shotAction.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_shotAction", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_shotAction.setText(QCoreApplication.translate("MainWindow", u"Action...", None))
#if QT_CONFIG(tooltip)
        self.listWidget_3.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_3", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_newTask.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newTask", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newTask.setText(QCoreApplication.translate("MainWindow", u"New Task", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Location.setToolTip(QCoreApplication.translate("MainWindow", u"lineEdit_Location", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_19.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_19", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"explore...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_shotBrowser), QCoreApplication.translate("MainWindow", u"Shot Browser", None))
        self.pushButton_num9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_num8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_num7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_num6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_num5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_num4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_num3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_num2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_num1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PW", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton_childUi.setText(QCoreApplication.translate("MainWindow", u"Launch Child Ui", None))
        self.pushButton_action1.setText(QCoreApplication.translate("MainWindow", u"call a blender bat", None))
        self.pushButton_7zip.setText(QCoreApplication.translate("MainWindow", u"Launch 7-zip", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"ACTIONS ...", None))
        self.pushButton_Location_2.setText(QCoreApplication.translate("MainWindow", u"explore...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Location of currently opened wip:", None))
        self.pushButton_overrideFrameRange.setText(QCoreApplication.translate("MainWindow", u"Override Frame Range", None))
#if QT_CONFIG(tooltip)
        self.toolButton_shotAction.setToolTip(QCoreApplication.translate("MainWindow", u"toolButton_shotAction", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_shotAction.setText(QCoreApplication.translate("MainWindow", u"ACTIONS ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_developing), QCoreApplication.translate("MainWindow", u"developing", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ASSET BROWSER", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Asset Type", None))
#if QT_CONFIG(tooltip)
        self.listWidget_assetType.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_assetType", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Asset", None))
#if QT_CONFIG(tooltip)
        self.listWidget_asset.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_asset", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Asset Task", None))
#if QT_CONFIG(tooltip)
        self.listWidget_assetTask.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_assetTask", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_Location_3.setToolTip(QCoreApplication.translate("MainWindow", u"lineEdit_Location_3", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_20.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_20", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"explore...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_assetBrowser), QCoreApplication.translate("MainWindow", u"developing Browser", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider.setToolTip(QCoreApplication.translate("MainWindow", u"horizontalSlider", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

