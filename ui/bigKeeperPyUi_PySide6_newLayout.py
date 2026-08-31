# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bigKeeperPyUi_PySide6_newLayout_v158.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 854)
        MainWindow.setMinimumSize(QSize(450, 854))
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
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.label_8 = QLabel(self.splitter)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(30, 0))
        self.label_8.setMaximumSize(QSize(100, 16777215))
        self.splitter.addWidget(self.label_8)
        self.comboBoxProjects = QComboBox(self.splitter)
        self.comboBoxProjects.setObjectName(u"comboBoxProjects")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxProjects.sizePolicy().hasHeightForWidth())
        self.comboBoxProjects.setSizePolicy(sizePolicy1)
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u"../../../bigKeeper/bigKeeperIcon.jpg"))

        self.verticalLayout.addWidget(self.label_9)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_currentOpen = QWidget()
        self.tab_currentOpen.setObjectName(u"tab_currentOpen")
        self.verticalLayout_12 = QVBoxLayout(self.tab_currentOpen)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalGroupBox_2 = QGroupBox(self.tab_currentOpen)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        sizePolicy.setHeightForWidth(self.verticalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_2.setSizePolicy(sizePolicy)
        self.verticalGroupBox_2.setMinimumSize(QSize(0, 270))
        self.verticalLayout_14 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.pushButton_versionUp = QPushButton(self.verticalGroupBox_2)
        self.pushButton_versionUp.setObjectName(u"pushButton_versionUp")
        sizePolicy.setHeightForWidth(self.pushButton_versionUp.sizePolicy().hasHeightForWidth())
        self.pushButton_versionUp.setSizePolicy(sizePolicy)
        self.pushButton_versionUp.setMinimumSize(QSize(170, 23))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        self.pushButton_versionUp.setFont(font)

        self.verticalLayout_14.addWidget(self.pushButton_versionUp)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_14.addItem(self.verticalSpacer_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.pushButton_revive = QPushButton(self.verticalGroupBox_2)
        self.pushButton_revive.setObjectName(u"pushButton_revive")
        sizePolicy.setHeightForWidth(self.pushButton_revive.sizePolicy().hasHeightForWidth())
        self.pushButton_revive.setSizePolicy(sizePolicy)
        self.pushButton_revive.setMinimumSize(QSize(71, 0))

        self.horizontalLayout_15.addWidget(self.pushButton_revive)

        self.pushButton_scnUpdate = QPushButton(self.verticalGroupBox_2)
        self.pushButton_scnUpdate.setObjectName(u"pushButton_scnUpdate")
        sizePolicy.setHeightForWidth(self.pushButton_scnUpdate.sizePolicy().hasHeightForWidth())
        self.pushButton_scnUpdate.setSizePolicy(sizePolicy)
        self.pushButton_scnUpdate.setMinimumSize(QSize(91, 0))

        self.horizontalLayout_15.addWidget(self.pushButton_scnUpdate)


        self.verticalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_5)

        self.pushButton_scnUpdate_2 = QPushButton(self.verticalGroupBox_2)
        self.pushButton_scnUpdate_2.setObjectName(u"pushButton_scnUpdate_2")
        sizePolicy.setHeightForWidth(self.pushButton_scnUpdate_2.sizePolicy().hasHeightForWidth())
        self.pushButton_scnUpdate_2.setSizePolicy(sizePolicy)
        self.pushButton_scnUpdate_2.setMinimumSize(QSize(91, 0))

        self.horizontalLayout_17.addWidget(self.pushButton_scnUpdate_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.pushButton_getFrameRange = QPushButton(self.verticalGroupBox_2)
        self.pushButton_getFrameRange.setObjectName(u"pushButton_getFrameRange")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_getFrameRange.sizePolicy().hasHeightForWidth())
        self.pushButton_getFrameRange.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.pushButton_getFrameRange)

        self.pushButton_NukeReadNodeTempTool = QPushButton(self.verticalGroupBox_2)
        self.pushButton_NukeReadNodeTempTool.setObjectName(u"pushButton_NukeReadNodeTempTool")
        sizePolicy2.setHeightForWidth(self.pushButton_NukeReadNodeTempTool.sizePolicy().hasHeightForWidth())
        self.pushButton_NukeReadNodeTempTool.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.pushButton_NukeReadNodeTempTool)


        self.horizontalLayout_14.addWidget(self.verticalGroupBox_2)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer)


        self.horizontalLayout_14.addLayout(self.verticalLayout_13)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.tabWidget_2 = QTabWidget(self.tab_currentOpen)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.tabWidget_2.setFont(font1)
        self.tabMaya = QWidget()
        self.tabMaya.setObjectName(u"tabMaya")
        self.tabWidget_2.addTab(self.tabMaya, "")
        self.tabNuke = QWidget()
        self.tabNuke.setObjectName(u"tabNuke")
        self.horizontalLayoutWidget_6 = QWidget(self.tabNuke)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(2, 8, 399, 211))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_24 = QLabel(self.horizontalLayoutWidget_6)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label_24.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_24)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_genLightPublishBackdrop = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_genLightPublishBackdrop.setObjectName(u"pushButton_genLightPublishBackdrop")
        sizePolicy3.setHeightForWidth(self.pushButton_genLightPublishBackdrop.sizePolicy().hasHeightForWidth())
        self.pushButton_genLightPublishBackdrop.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(7)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_genLightPublishBackdrop.setFont(font3)

        self.horizontalLayout_20.addWidget(self.pushButton_genLightPublishBackdrop)

        self.pushButton_lightPublishAction = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_lightPublishAction.setObjectName(u"pushButton_lightPublishAction")
        sizePolicy3.setHeightForWidth(self.pushButton_lightPublishAction.sizePolicy().hasHeightForWidth())
        self.pushButton_lightPublishAction.setSizePolicy(sizePolicy3)
        self.pushButton_lightPublishAction.setMaximumSize(QSize(85, 16777215))
        self.pushButton_lightPublishAction.setFont(font3)

        self.horizontalLayout_20.addWidget(self.pushButton_lightPublishAction)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_25 = QLabel(self.horizontalLayoutWidget_6)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)
        self.label_25.setFont(font2)

        self.horizontalLayout_21.addWidget(self.label_25)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_genWritePrerend = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_genWritePrerend.setObjectName(u"pushButton_genWritePrerend")
        self.pushButton_genWritePrerend.setFont(font3)

        self.horizontalLayout_25.addWidget(self.pushButton_genWritePrerend)

        self.horizontalSpacer_3 = QSpacerItem(85, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_3)


        self.verticalLayout_20.addLayout(self.horizontalLayout_25)


        self.verticalLayout_15.addLayout(self.verticalLayout_20)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_26 = QLabel(self.horizontalLayoutWidget_6)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)
        self.label_26.setFont(font2)

        self.verticalLayout_17.addWidget(self.label_26)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_genWriteCompMaster = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_genWriteCompMaster.setObjectName(u"pushButton_genWriteCompMaster")
        self.pushButton_genWriteCompMaster.setFont(font3)

        self.horizontalLayout_22.addWidget(self.pushButton_genWriteCompMaster)

        self.pushButton_genWriteCompMasterV = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_genWriteCompMasterV.setObjectName(u"pushButton_genWriteCompMasterV")
        self.pushButton_genWriteCompMasterV.setFont(font3)

        self.horizontalLayout_22.addWidget(self.pushButton_genWriteCompMasterV)


        self.verticalLayout_17.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_genWriteLayerMask = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_genWriteLayerMask.setObjectName(u"pushButton_genWriteLayerMask")
        self.pushButton_genWriteLayerMask.setFont(font3)

        self.horizontalLayout_23.addWidget(self.pushButton_genWriteLayerMask)

        self.pushButton_genWriteFreeLayerMask = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_genWriteFreeLayerMask.setObjectName(u"pushButton_genWriteFreeLayerMask")
        self.pushButton_genWriteFreeLayerMask.setFont(font3)

        self.horizontalLayout_23.addWidget(self.pushButton_genWriteFreeLayerMask)


        self.verticalLayout_17.addLayout(self.horizontalLayout_23)


        self.verticalLayout_15.addLayout(self.verticalLayout_17)


        self.horizontalLayout_19.addLayout(self.verticalLayout_15)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_21 = QLabel(self.horizontalLayoutWidget_6)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setFont(font2)

        self.verticalLayout_19.addWidget(self.label_21)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.pushButton_FileKnobFreeze = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_FileKnobFreeze.setObjectName(u"pushButton_FileKnobFreeze")
        self.pushButton_FileKnobFreeze.setFont(font3)

        self.horizontalLayout_24.addWidget(self.pushButton_FileKnobFreeze)

        self.pushButton_FileKnobUnFreeze = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_FileKnobUnFreeze.setObjectName(u"pushButton_FileKnobUnFreeze")
        self.pushButton_FileKnobUnFreeze.setFont(font3)

        self.horizontalLayout_24.addWidget(self.pushButton_FileKnobUnFreeze)


        self.verticalLayout_19.addLayout(self.horizontalLayout_24)


        self.verticalLayout_21.addLayout(self.verticalLayout_19)

        self.label_27 = QLabel(self.horizontalLayoutWidget_6)
        self.label_27.setObjectName(u"label_27")
        sizePolicy3.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy3)
        self.label_27.setFont(font2)

        self.verticalLayout_21.addWidget(self.label_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_genCgRenderBackdrop = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_genCgRenderBackdrop.setObjectName(u"pushButton_genCgRenderBackdrop")
        sizePolicy3.setHeightForWidth(self.pushButton_genCgRenderBackdrop.sizePolicy().hasHeightForWidth())
        self.pushButton_genCgRenderBackdrop.setSizePolicy(sizePolicy3)
        self.pushButton_genCgRenderBackdrop.setMinimumSize(QSize(100, 0))
        self.pushButton_genCgRenderBackdrop.setFont(font3)

        self.horizontalLayout_26.addWidget(self.pushButton_genCgRenderBackdrop)

        self.pushButton_genOtherBackdrop = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_genOtherBackdrop.setObjectName(u"pushButton_genOtherBackdrop")
        sizePolicy3.setHeightForWidth(self.pushButton_genOtherBackdrop.sizePolicy().hasHeightForWidth())
        self.pushButton_genOtherBackdrop.setSizePolicy(sizePolicy3)
        self.pushButton_genOtherBackdrop.setFont(font3)

        self.horizontalLayout_26.addWidget(self.pushButton_genOtherBackdrop)


        self.verticalLayout_21.addLayout(self.horizontalLayout_26)


        self.verticalLayout_18.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_30.addItem(self.verticalSpacer_4)


        self.verticalLayout_22.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_7)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")

        self.verticalLayout_22.addLayout(self.horizontalLayout_31)


        self.verticalLayout_18.addLayout(self.verticalLayout_22)


        self.horizontalLayout_19.addLayout(self.verticalLayout_18)

        self.pushButton_closeNukeScript = QPushButton(self.tabNuke)
        self.pushButton_closeNukeScript.setObjectName(u"pushButton_closeNukeScript")
        self.pushButton_closeNukeScript.setGeometry(QRect(0, 220, 171, 23))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_closeNukeScript.setFont(font4)
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
        self.pushButton_sortoutfile.setGeometry(QRect(230, 30, 81, 23))
        self.label_17 = QLabel(self.tabCmd)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 10, 151, 16))
        self.label_17.setTextFormat(Qt.TextFormat.PlainText)
        self.pushButton_exeDel = QPushButton(self.tabCmd)
        self.pushButton_exeDel.setObjectName(u"pushButton_exeDel")
        self.pushButton_exeDel.setGeometry(QRect(320, 60, 31, 23))
        self.label_18 = QLabel(self.tabCmd)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 30, 201, 16))
        self.label_19 = QLabel(self.tabCmd)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 60, 201, 16))
        self.pushButton_exeMove = QPushButton(self.tabCmd)
        self.pushButton_exeMove.setObjectName(u"pushButton_exeMove")
        self.pushButton_exeMove.setGeometry(QRect(230, 60, 81, 23))
        self.tabWidget_2.addTab(self.tabCmd, "")
        self.tabLauncher = QWidget()
        self.tabLauncher.setObjectName(u"tabLauncher")
        self.verticalLayout_11 = QVBoxLayout(self.tabLauncher)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox = QGroupBox(self.tabLauncher)
        self.groupBox.setObjectName(u"groupBox")
        font5 = QFont()
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.groupBox.setFont(font5)
        self.pushButton_LaunchNuke13_0_v2 = QPushButton(self.groupBox)
        self.pushButton_LaunchNuke13_0_v2.setObjectName(u"pushButton_LaunchNuke13_0_v2")
        self.pushButton_LaunchNuke13_0_v2.setGeometry(QRect(50, 70, 61, 41))
        font6 = QFont()
        font6.setPointSize(8)
        font6.setKerning(True)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_LaunchNuke13_0_v2.setFont(font6)
        self.pushButton_LaunchNukeStudio13_0_v2 = QPushButton(self.groupBox)
        self.pushButton_LaunchNukeStudio13_0_v2.setObjectName(u"pushButton_LaunchNukeStudio13_0_v2")
        self.pushButton_LaunchNukeStudio13_0_v2.setGeometry(QRect(190, 70, 41, 41))
        self.pushButton_LaunchNukeStudio13_0_v2.setFont(font6)
        self.pushButton_LaunchNukeX13_0_v2 = QPushButton(self.groupBox)
        self.pushButton_LaunchNukeX13_0_v2.setObjectName(u"pushButton_LaunchNukeX13_0_v2")
        self.pushButton_LaunchNukeX13_0_v2.setGeometry(QRect(110, 70, 41, 41))
        self.pushButton_LaunchNukeX13_0_v2.setFont(font6)
        self.pushButton_LaunchNukeAssist13_0_v2 = QPushButton(self.groupBox)
        self.pushButton_LaunchNukeAssist13_0_v2.setObjectName(u"pushButton_LaunchNukeAssist13_0_v2")
        self.pushButton_LaunchNukeAssist13_0_v2.setGeometry(QRect(150, 70, 41, 41))
        self.pushButton_LaunchNukeAssist13_0_v2.setFont(font6)
        self.pushButton_LaunchMaya2022_update0 = QPushButton(self.groupBox)
        self.pushButton_LaunchMaya2022_update0.setObjectName(u"pushButton_LaunchMaya2022_update0")
        self.pushButton_LaunchMaya2022_update0.setGeometry(QRect(50, 30, 141, 41))
        self.pushButton_LaunchMaya2022_update0.setFont(font6)
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
        self.pushButton_dailyFolder.setGeometry(QRect(50, 150, 181, 21))
        self.pushButton_dailyFolder.setFont(font6)
        self.pushButton_launchHoudini1 = QPushButton(self.groupBox)
        self.pushButton_launchHoudini1.setObjectName(u"pushButton_launchHoudini1")
        self.pushButton_launchHoudini1.setGeometry(QRect(50, 110, 181, 41))
        self.pushButton_launchHoudini1.setFont(font6)
        self.pushButton_houdiniOther = QPushButton(self.groupBox)
        self.pushButton_houdiniOther.setObjectName(u"pushButton_houdiniOther")
        self.pushButton_houdiniOther.setGeometry(QRect(230, 110, 16, 31))
        self.label_houdiniIcon = QLabel(self.groupBox)
        self.label_houdiniIcon.setObjectName(u"label_houdiniIcon")
        self.label_houdiniIcon.setGeometry(QRect(10, 110, 41, 41))
        self.pushButton_LaunchHieroPlayer = QPushButton(self.groupBox)
        self.pushButton_LaunchHieroPlayer.setObjectName(u"pushButton_LaunchHieroPlayer")
        self.pushButton_LaunchHieroPlayer.setGeometry(QRect(250, 70, 61, 41))
        self.pushButton_LaunchHieroPlayer.setFont(font6)
        self.pushButton_hieroPlayerOther = QPushButton(self.groupBox)
        self.pushButton_hieroPlayerOther.setObjectName(u"pushButton_hieroPlayerOther")
        self.pushButton_hieroPlayerOther.setGeometry(QRect(310, 70, 16, 41))
        self.pushButton_LaunchCpuCoreController = QPushButton(self.groupBox)
        self.pushButton_LaunchCpuCoreController.setObjectName(u"pushButton_LaunchCpuCoreController")
        self.pushButton_LaunchCpuCoreController.setGeometry(QRect(50, 170, 91, 41))
        self.pushButton_LaunchCpuCoreController.setFont(font6)
        self.pushButton_LaunchGpuCoreController = QPushButton(self.groupBox)
        self.pushButton_LaunchGpuCoreController.setObjectName(u"pushButton_LaunchGpuCoreController")
        self.pushButton_LaunchGpuCoreController.setGeometry(QRect(140, 170, 91, 41))
        self.pushButton_LaunchGpuCoreController.setFont(font6)
        self.pushButton_LaunchMayaLegacySelection = QPushButton(self.groupBox)
        self.pushButton_LaunchMayaLegacySelection.setObjectName(u"pushButton_LaunchMayaLegacySelection")
        self.pushButton_LaunchMayaLegacySelection.setGeometry(QRect(190, 30, 41, 41))
        font7 = QFont()
        font7.setPointSize(6)
        font7.setKerning(True)
        font7.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_LaunchMayaLegacySelection.setFont(font7)
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
        self.pushButton_LaunchHieroPlayer.raise_()
        self.pushButton_hieroPlayerOther.raise_()
        self.pushButton_LaunchCpuCoreController.raise_()
        self.pushButton_LaunchGpuCoreController.raise_()
        self.pushButton_LaunchMayaLegacySelection.raise_()

        self.verticalLayout_11.addWidget(self.groupBox)

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

        self.verticalLayout_12.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab_currentOpen, "")
        self.tab_assetBrowser = QWidget()
        self.tab_assetBrowser.setObjectName(u"tab_assetBrowser")
        self.verticalLayout_10 = QVBoxLayout(self.tab_assetBrowser)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_16 = QLabel(self.tab_assetBrowser)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_34.addWidget(self.label_16)

        self.pushButton_vBoardAssetTab = QPushButton(self.tab_assetBrowser)
        self.pushButton_vBoardAssetTab.setObjectName(u"pushButton_vBoardAssetTab")

        self.horizontalLayout_34.addWidget(self.pushButton_vBoardAssetTab)


        self.verticalLayout_6.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.tab_assetBrowser)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_18.addWidget(self.label_13)

        self.pushButton_listWidgetAssetRefresh = QPushButton(self.tab_assetBrowser)
        self.pushButton_listWidgetAssetRefresh.setObjectName(u"pushButton_listWidgetAssetRefresh")
        self.pushButton_listWidgetAssetRefresh.setMinimumSize(QSize(0, 23))
        self.pushButton_listWidgetAssetRefresh.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.pushButton_listWidgetAssetRefresh)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.listWidget_AssetType = QListWidget(self.tab_assetBrowser)
        self.listWidget_AssetType.setObjectName(u"listWidget_AssetType")
        self.listWidget_AssetType.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout_7.addWidget(self.listWidget_AssetType)

        self.pushButton_newType = QPushButton(self.tab_assetBrowser)
        self.pushButton_newType.setObjectName(u"pushButton_newType")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_newType.sizePolicy().hasHeightForWidth())
        self.pushButton_newType.setSizePolicy(sizePolicy4)

        self.verticalLayout_7.addWidget(self.pushButton_newType)

        self.pushButton_vBoardType = QPushButton(self.tab_assetBrowser)
        self.pushButton_vBoardType.setObjectName(u"pushButton_vBoardType")

        self.verticalLayout_7.addWidget(self.pushButton_vBoardType)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_14 = QLabel(self.tab_assetBrowser)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_27.addWidget(self.label_14)

        self.label_23 = QLabel(self.tab_assetBrowser)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 23))

        self.horizontalLayout_27.addWidget(self.label_23)


        self.verticalLayout_8.addLayout(self.horizontalLayout_27)

        self.listWidget_Asset = QListWidget(self.tab_assetBrowser)
        self.listWidget_Asset.setObjectName(u"listWidget_Asset")
        self.listWidget_Asset.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout_8.addWidget(self.listWidget_Asset)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_newAsset = QPushButton(self.tab_assetBrowser)
        self.pushButton_newAsset.setObjectName(u"pushButton_newAsset")
        sizePolicy4.setHeightForWidth(self.pushButton_newAsset.sizePolicy().hasHeightForWidth())
        self.pushButton_newAsset.setSizePolicy(sizePolicy4)
        self.pushButton_newAsset.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_28.addWidget(self.pushButton_newAsset)

        self.pushButton_newAssetBatch = QPushButton(self.tab_assetBrowser)
        self.pushButton_newAssetBatch.setObjectName(u"pushButton_newAssetBatch")
        sizePolicy4.setHeightForWidth(self.pushButton_newAssetBatch.sizePolicy().hasHeightForWidth())
        self.pushButton_newAssetBatch.setSizePolicy(sizePolicy4)
        self.pushButton_newAssetBatch.setMaximumSize(QSize(40, 16777215))
        self.pushButton_newAssetBatch.setIconSize(QSize(16, 16))

        self.horizontalLayout_28.addWidget(self.pushButton_newAssetBatch)


        self.verticalLayout_8.addLayout(self.horizontalLayout_28)

        self.pushButton_vBoardAsset = QPushButton(self.tab_assetBrowser)
        self.pushButton_vBoardAsset.setObjectName(u"pushButton_vBoardAsset")

        self.verticalLayout_8.addWidget(self.pushButton_vBoardAsset)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_15 = QLabel(self.tab_assetBrowser)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 23))

        self.verticalLayout_9.addWidget(self.label_15)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_assetAction = QPushButton(self.tab_assetBrowser)
        self.pushButton_assetAction.setObjectName(u"pushButton_assetAction")

        self.verticalLayout_23.addWidget(self.pushButton_assetAction)

        self.pushButton_assetAction2 = QPushButton(self.tab_assetBrowser)
        self.pushButton_assetAction2.setObjectName(u"pushButton_assetAction2")

        self.verticalLayout_23.addWidget(self.pushButton_assetAction2)


        self.verticalLayout_9.addLayout(self.verticalLayout_23)

        self.listWidget_AssetTask = QListWidget(self.tab_assetBrowser)
        self.listWidget_AssetTask.setObjectName(u"listWidget_AssetTask")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.listWidget_AssetTask.sizePolicy().hasHeightForWidth())
        self.listWidget_AssetTask.setSizePolicy(sizePolicy5)
        self.listWidget_AssetTask.setMinimumSize(QSize(0, 120))
        self.listWidget_AssetTask.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout_9.addWidget(self.listWidget_AssetTask)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.pushButton_assetAction3 = QPushButton(self.tab_assetBrowser)
        self.pushButton_assetAction3.setObjectName(u"pushButton_assetAction3")

        self.verticalLayout_24.addWidget(self.pushButton_assetAction3)

        self.pushButton_newAssetTask = QPushButton(self.tab_assetBrowser)
        self.pushButton_newAssetTask.setObjectName(u"pushButton_newAssetTask")
        sizePolicy4.setHeightForWidth(self.pushButton_newAssetTask.sizePolicy().hasHeightForWidth())
        self.pushButton_newAssetTask.setSizePolicy(sizePolicy4)

        self.verticalLayout_24.addWidget(self.pushButton_newAssetTask)


        self.verticalLayout_9.addLayout(self.verticalLayout_24)

        self.pushButton_vBoardAssetTask = QPushButton(self.tab_assetBrowser)
        self.pushButton_vBoardAssetTask.setObjectName(u"pushButton_vBoardAssetTask")

        self.verticalLayout_9.addWidget(self.pushButton_vBoardAssetTask)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setSpacing(6)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_thumbType = QLabel(self.tab_assetBrowser)
        self.label_thumbType.setObjectName(u"label_thumbType")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_thumbType.sizePolicy().hasHeightForWidth())
        self.label_thumbType.setSizePolicy(sizePolicy6)
        self.label_thumbType.setMinimumSize(QSize(123, 60))

        self.horizontalLayout_29.addWidget(self.label_thumbType)

        self.label_thumbAsset = QLabel(self.tab_assetBrowser)
        self.label_thumbAsset.setObjectName(u"label_thumbAsset")
        sizePolicy6.setHeightForWidth(self.label_thumbAsset.sizePolicy().hasHeightForWidth())
        self.label_thumbAsset.setSizePolicy(sizePolicy6)
        self.label_thumbAsset.setMinimumSize(QSize(123, 60))

        self.horizontalLayout_29.addWidget(self.label_thumbAsset)

        self.label_thumbAssetTask = QLabel(self.tab_assetBrowser)
        self.label_thumbAssetTask.setObjectName(u"label_thumbAssetTask")
        sizePolicy6.setHeightForWidth(self.label_thumbAssetTask.sizePolicy().hasHeightForWidth())
        self.label_thumbAssetTask.setSizePolicy(sizePolicy6)
        self.label_thumbAssetTask.setMinimumSize(QSize(123, 60))

        self.horizontalLayout_29.addWidget(self.label_thumbAssetTask)


        self.verticalLayout_6.addLayout(self.horizontalLayout_29)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_assetLocation = QLineEdit(self.tab_assetBrowser)
        self.lineEdit_assetLocation.setObjectName(u"lineEdit_assetLocation")

        self.horizontalLayout_7.addWidget(self.lineEdit_assetLocation)

        self.pushButton_20 = QPushButton(self.tab_assetBrowser)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_7.addWidget(self.pushButton_20)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.verticalLayout_10.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab_assetBrowser, "")
        self.tab_shotBrowser = QWidget()
        self.tab_shotBrowser.setObjectName(u"tab_shotBrowser")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_shotBrowser)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_12 = QLabel(self.tab_shotBrowser)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_32.addWidget(self.label_12)

        self.pushButton_vBoardShotTab = QPushButton(self.tab_shotBrowser)
        self.pushButton_vBoardShotTab.setObjectName(u"pushButton_vBoardShotTab")

        self.horizontalLayout_32.addWidget(self.pushButton_vBoardShotTab)


        self.verticalLayout_5.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
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
        self.listWidget_1.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout_2.addWidget(self.listWidget_1)

        self.pushButton_newSeq = QPushButton(self.tab_shotBrowser)
        self.pushButton_newSeq.setObjectName(u"pushButton_newSeq")
        sizePolicy4.setHeightForWidth(self.pushButton_newSeq.sizePolicy().hasHeightForWidth())
        self.pushButton_newSeq.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.pushButton_newSeq)

        self.pushButton_vBoardSeq = QPushButton(self.tab_shotBrowser)
        self.pushButton_vBoardSeq.setObjectName(u"pushButton_vBoardSeq")

        self.verticalLayout_2.addWidget(self.pushButton_vBoardSeq)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
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
        self.listWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout_3.addWidget(self.listWidget_2)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_newShot = QPushButton(self.tab_shotBrowser)
        self.pushButton_newShot.setObjectName(u"pushButton_newShot")
        sizePolicy4.setHeightForWidth(self.pushButton_newShot.sizePolicy().hasHeightForWidth())
        self.pushButton_newShot.setSizePolicy(sizePolicy4)
        self.pushButton_newShot.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_16.addWidget(self.pushButton_newShot)

        self.pushButton_newShotBatch = QPushButton(self.tab_shotBrowser)
        self.pushButton_newShotBatch.setObjectName(u"pushButton_newShotBatch")
        sizePolicy4.setHeightForWidth(self.pushButton_newShotBatch.sizePolicy().hasHeightForWidth())
        self.pushButton_newShotBatch.setSizePolicy(sizePolicy4)
        self.pushButton_newShotBatch.setMaximumSize(QSize(40, 16777215))
        self.pushButton_newShotBatch.setIconSize(QSize(16, 16))

        self.horizontalLayout_16.addWidget(self.pushButton_newShotBatch)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.pushButton_vBoardShot = QPushButton(self.tab_shotBrowser)
        self.pushButton_vBoardShot.setObjectName(u"pushButton_vBoardShot")

        self.verticalLayout_3.addWidget(self.pushButton_vBoardShot)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.tab_shotBrowser)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 23))

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pushButton_shotAction = QPushButton(self.tab_shotBrowser)
        self.pushButton_shotAction.setObjectName(u"pushButton_shotAction")

        self.verticalLayout_25.addWidget(self.pushButton_shotAction)

        self.pushButton_shotAction2 = QPushButton(self.tab_shotBrowser)
        self.pushButton_shotAction2.setObjectName(u"pushButton_shotAction2")

        self.verticalLayout_25.addWidget(self.pushButton_shotAction2)


        self.verticalLayout_4.addLayout(self.verticalLayout_25)

        self.listWidget_3 = QListWidget(self.tab_shotBrowser)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(0, 120))
        self.listWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout_4.addWidget(self.listWidget_3)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.pushButton_shotAction3 = QPushButton(self.tab_shotBrowser)
        self.pushButton_shotAction3.setObjectName(u"pushButton_shotAction3")

        self.verticalLayout_26.addWidget(self.pushButton_shotAction3)

        self.pushButton_newScnTask = QPushButton(self.tab_shotBrowser)
        self.pushButton_newScnTask.setObjectName(u"pushButton_newScnTask")
        sizePolicy4.setHeightForWidth(self.pushButton_newScnTask.sizePolicy().hasHeightForWidth())
        self.pushButton_newScnTask.setSizePolicy(sizePolicy4)

        self.verticalLayout_26.addWidget(self.pushButton_newScnTask)


        self.verticalLayout_4.addLayout(self.verticalLayout_26)

        self.pushButton_vBoardScnTask = QPushButton(self.tab_shotBrowser)
        self.pushButton_vBoardScnTask.setObjectName(u"pushButton_vBoardScnTask")

        self.verticalLayout_4.addWidget(self.pushButton_vBoardScnTask)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_thumbSeq = QLabel(self.tab_shotBrowser)
        self.label_thumbSeq.setObjectName(u"label_thumbSeq")
        sizePolicy6.setHeightForWidth(self.label_thumbSeq.sizePolicy().hasHeightForWidth())
        self.label_thumbSeq.setSizePolicy(sizePolicy6)
        self.label_thumbSeq.setMinimumSize(QSize(123, 60))

        self.horizontalLayout_11.addWidget(self.label_thumbSeq)

        self.label_thumbShot = QLabel(self.tab_shotBrowser)
        self.label_thumbShot.setObjectName(u"label_thumbShot")
        sizePolicy6.setHeightForWidth(self.label_thumbShot.sizePolicy().hasHeightForWidth())
        self.label_thumbShot.setSizePolicy(sizePolicy6)
        self.label_thumbShot.setMinimumSize(QSize(123, 60))

        self.horizontalLayout_11.addWidget(self.label_thumbShot)

        self.label_thumbTask = QLabel(self.tab_shotBrowser)
        self.label_thumbTask.setObjectName(u"label_thumbTask")
        sizePolicy6.setHeightForWidth(self.label_thumbTask.sizePolicy().hasHeightForWidth())
        self.label_thumbTask.setSizePolicy(sizePolicy6)
        self.label_thumbTask.setMinimumSize(QSize(123, 60))

        self.horizontalLayout_11.addWidget(self.label_thumbTask)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_sceneLocation = QLineEdit(self.tab_shotBrowser)
        self.lineEdit_sceneLocation.setObjectName(u"lineEdit_sceneLocation")

        self.horizontalLayout_4.addWidget(self.lineEdit_sceneLocation)

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
        self.layoutWidget_2.setGeometry(QRect(20, 160, 320, 116))
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
        self.layoutWidget_3.setGeometry(QRect(20, 290, 158, 82))
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
        self.layoutWidget_4.setGeometry(QRect(20, 20, 251, 26))
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
        self.layoutWidget_5.setGeometry(QRect(20, 60, 251, 78))
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
        sizePolicy4.setHeightForWidth(self.toolButton_shotAction.sizePolicy().hasHeightForWidth())
        self.toolButton_shotAction.setSizePolicy(sizePolicy4)
        self.pushButton_CompLatestRv = QPushButton(self.tab_developing)
        self.pushButton_CompLatestRv.setObjectName(u"pushButton_CompLatestRv")
        self.pushButton_CompLatestRv.setGeometry(QRect(190, 410, 151, 21))
        self.tabWidget.addTab(self.tab_developing, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalSlider_echoSwitch = QSlider(self.centralwidget)
        self.horizontalSlider_echoSwitch.setObjectName(u"horizontalSlider_echoSwitch")
        font8 = QFont()
        font8.setPointSize(9)
        self.horizontalSlider_echoSwitch.setFont(font8)
        self.horizontalSlider_echoSwitch.setMaximum(2)
        self.horizontalSlider_echoSwitch.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_echoSwitch)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_openCal.setText(QCoreApplication.translate("MainWindow", u"Open bpvfx Calendar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_openCal2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_openCal2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_openCal2.setText(QCoreApplication.translate("MainWindow", u"Open bpvfx Calendar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Project :", None))
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
        self.pushButton_scnUpdate.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_scnUpdate", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_scnUpdate.setText(QCoreApplication.translate("MainWindow", u"Scene Update", None))
#if QT_CONFIG(tooltip)
        self.pushButton_scnUpdate_2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_scnUpdate", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_scnUpdate_2.setText(QCoreApplication.translate("MainWindow", u"Scene Update", None))
#if QT_CONFIG(tooltip)
        self.pushButton_getFrameRange.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_getFrameRange", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_getFrameRange.setText(QCoreApplication.translate("MainWindow", u"Get Frame Range\n"
"- output setting -", None))
#if QT_CONFIG(tooltip)
        self.pushButton_NukeReadNodeTempTool.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_NukeReadNodeTempTool", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_NukeReadNodeTempTool.setText(QCoreApplication.translate("MainWindow", u"Get Frame Range\n"
"- Selected Read Nodes -", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabMaya), QCoreApplication.translate("MainWindow", u"Maya", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Light Publish", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genLightPublishBackdrop.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genLightPublishBackdrop", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genLightPublishBackdrop.setText(QCoreApplication.translate("MainWindow", u"Backdrop\n"
"(only 1)", None))
#if QT_CONFIG(tooltip)
        self.pushButton_lightPublishAction.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LightPublishAction", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_lightPublishAction.setText(QCoreApplication.translate("MainWindow", u"VersionUp + \n"
"LightPublish", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Prerend Write Node", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genWritePrerend.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWritePrerend", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genWritePrerend.setText(QCoreApplication.translate("MainWindow", u"Prerend", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Output Write Node", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genWriteCompMaster.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWriteCompMaster", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genWriteCompMaster.setText(QCoreApplication.translate("MainWindow", u"CompMaster", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genWriteCompMasterV.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWriteCompMasterV", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genWriteCompMasterV.setText(QCoreApplication.translate("MainWindow", u"CompMaster-V", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genWriteLayerMask.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWriteLayerMask", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genWriteLayerMask.setText(QCoreApplication.translate("MainWindow", u"LayerMask", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genWriteFreeLayerMask.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genWriteFreeLayerMask", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genWriteFreeLayerMask.setText(QCoreApplication.translate("MainWindow", u"Free LayerMask", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Freeze Scene Update Node", None))
#if QT_CONFIG(tooltip)
        self.pushButton_FileKnobFreeze.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_FileKnobFreeze\n"
"by select < NODES >", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_FileKnobFreeze.setText(QCoreApplication.translate("MainWindow", u"Freeze", None))
#if QT_CONFIG(tooltip)
        self.pushButton_FileKnobUnFreeze.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_FileKnobUnFreeze\n"
"by select the < Freeze Backdrop >", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_FileKnobUnFreeze.setText(QCoreApplication.translate("MainWindow", u"UnFreeze", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Default Backdrop", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genCgRenderBackdrop.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genCgRenderBackdrop", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genCgRenderBackdrop.setText(QCoreApplication.translate("MainWindow", u"Cg Images of\n"
"Light PreComp", None))
#if QT_CONFIG(tooltip)
        self.pushButton_genOtherBackdrop.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_genOtherBackdrop", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_genOtherBackdrop.setText(QCoreApplication.translate("MainWindow", u"Others", None))
#if QT_CONFIG(tooltip)
        self.pushButton_closeNukeScript.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_closeNukeScript", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_closeNukeScript.setText(QCoreApplication.translate("MainWindow", u"close Nuke Script", None))
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
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"2) Execut Move / Del", None))
#if QT_CONFIG(tooltip)
        self.pushButton_exeMove.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_sortoutfile", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_exeMove.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabCmd), QCoreApplication.translate("MainWindow", u"Cmd", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Studio Dedicated Launcher:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchNuke13_0_v2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchNuke13_0_v2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchNuke13_0_v2.setText(QCoreApplication.translate("MainWindow", u"_Nuke", None))
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
        self.pushButton_LaunchMaya2022_update0.setText(QCoreApplication.translate("MainWindow", u"_Maya", None))
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
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchHieroPlayer.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchHieroPlayer", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchHieroPlayer.setText(QCoreApplication.translate("MainWindow", u"hieroPlayer", None))
#if QT_CONFIG(tooltip)
        self.pushButton_hieroPlayerOther.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_hieroPlayerOther", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_hieroPlayerOther.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchCpuCoreController.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchCpuCoreController", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchCpuCoreController.setText(QCoreApplication.translate("MainWindow", u"Deadline CPU\n"
"Control", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchGpuCoreController.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchCpuCoreController", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchGpuCoreController.setText(QCoreApplication.translate("MainWindow", u"Deadline GPU\n"
"Controller", None))
#if QT_CONFIG(tooltip)
        self.pushButton_LaunchMayaLegacySelection.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_LaunchMayaLegacySelection", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_LaunchMayaLegacySelection.setText(QCoreApplication.translate("MainWindow", u"Outline\n"
"Sel Disp", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_currentOpen), QCoreApplication.translate("MainWindow", u"Currently Open", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ASSET BROWSER", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vBoardAssetTab.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_vBoardAssetTab", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vBoardAssetTab.setText(QCoreApplication.translate("MainWindow", u"Visual Board", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Type", None))
#if QT_CONFIG(tooltip)
        self.pushButton_listWidgetAssetRefresh.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_listWidgetAssetRefresh", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_listWidgetAssetRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.listWidget_AssetType.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_AssetType", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_newType.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newType", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newType.setText(QCoreApplication.translate("MainWindow", u"New Asset Type", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vBoardType.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_vBoardType", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vBoardType.setText(QCoreApplication.translate("MainWindow", u"Visual Board", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Asset", None))
#if QT_CONFIG(tooltip)
        self.label_23.setToolTip(QCoreApplication.translate("MainWindow", u"label_20", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText("")
#if QT_CONFIG(tooltip)
        self.listWidget_Asset.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_Asset", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_newAsset.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newAsset", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newAsset.setText(QCoreApplication.translate("MainWindow", u"New Asset", None))
#if QT_CONFIG(tooltip)
        self.pushButton_newAssetBatch.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newAssetBatch", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newAssetBatch.setText(QCoreApplication.translate("MainWindow", u"Batch", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vBoardAsset.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_vBoardAsset", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vBoardAsset.setText(QCoreApplication.translate("MainWindow", u"Visual Board", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Task Asset", None))
#if QT_CONFIG(tooltip)
        self.pushButton_assetAction.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_assetAction", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_assetAction.setText(QCoreApplication.translate("MainWindow", u"Action...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_assetAction2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_assetAction2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_assetAction2.setText(QCoreApplication.translate("MainWindow", u"Action...", None))
#if QT_CONFIG(tooltip)
        self.listWidget_AssetTask.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_AssetTask", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_assetAction3.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_assetAction3", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_assetAction3.setText(QCoreApplication.translate("MainWindow", u"Action...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_newAssetTask.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newAssetTask", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newAssetTask.setText(QCoreApplication.translate("MainWindow", u"New Task", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vBoardAssetTask.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_vBoardAssetTask", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vBoardAssetTask.setText(QCoreApplication.translate("MainWindow", u"Visual Board", None))
#if QT_CONFIG(tooltip)
        self.label_thumbType.setToolTip(QCoreApplication.translate("MainWindow", u"label_thumbType", None))
#endif // QT_CONFIG(tooltip)
        self.label_thumbType.setText(QCoreApplication.translate("MainWindow", u"label_thumbAssetType", None))
#if QT_CONFIG(tooltip)
        self.label_thumbAsset.setToolTip(QCoreApplication.translate("MainWindow", u"label_thumbAsset", None))
#endif // QT_CONFIG(tooltip)
        self.label_thumbAsset.setText(QCoreApplication.translate("MainWindow", u"label_thumb", None))
#if QT_CONFIG(tooltip)
        self.label_thumbAssetTask.setToolTip(QCoreApplication.translate("MainWindow", u"label_thumbAssetTask", None))
#endif // QT_CONFIG(tooltip)
        self.label_thumbAssetTask.setText(QCoreApplication.translate("MainWindow", u"label_thumbTask", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_assetLocation.setToolTip(QCoreApplication.translate("MainWindow", u"lineEdit_assetLocation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_20.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_20", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"explore...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_assetBrowser), QCoreApplication.translate("MainWindow", u"Asset Browser", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"SHOT BROWSER", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vBoardShotTab.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_vBoardShotTab", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vBoardShotTab.setText(QCoreApplication.translate("MainWindow", u"Visual Board", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sequence", None))
#if QT_CONFIG(tooltip)
        self.pushButton_listWidget1Refresh.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_listWidget1Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_listWidget1Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.listWidget_1.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_1", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_newSeq.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newSeq", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newSeq.setText(QCoreApplication.translate("MainWindow", u"New Sequence", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vBoardSeq.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_vBoardSeq", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vBoardSeq.setText(QCoreApplication.translate("MainWindow", u"Visual Board", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Shot", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("MainWindow", u"label_20", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText("")
#if QT_CONFIG(tooltip)
        self.listWidget_2.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_2", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_newShot.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newShot", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newShot.setText(QCoreApplication.translate("MainWindow", u"New Shot", None))
#if QT_CONFIG(tooltip)
        self.pushButton_newShotBatch.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newShotBatch", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newShotBatch.setText(QCoreApplication.translate("MainWindow", u"Batch", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vBoardShot.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_vBoardShot", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vBoardShot.setText(QCoreApplication.translate("MainWindow", u"Visual Board", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Task Shot", None))
#if QT_CONFIG(tooltip)
        self.pushButton_shotAction.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_shotAction", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_shotAction.setText(QCoreApplication.translate("MainWindow", u"Action...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_shotAction2.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_shotAction2", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_shotAction2.setText(QCoreApplication.translate("MainWindow", u"Action...", None))
#if QT_CONFIG(tooltip)
        self.listWidget_3.setToolTip(QCoreApplication.translate("MainWindow", u"listWidget_3", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_shotAction3.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_shotAction3", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_shotAction3.setText(QCoreApplication.translate("MainWindow", u"Action...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_newScnTask.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_newScnTask", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_newScnTask.setText(QCoreApplication.translate("MainWindow", u"New Task", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vBoardScnTask.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_vBoardScnTask", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vBoardScnTask.setText(QCoreApplication.translate("MainWindow", u"Visual Board", None))
#if QT_CONFIG(tooltip)
        self.label_thumbSeq.setToolTip(QCoreApplication.translate("MainWindow", u"label_thumbSeq", None))
#endif // QT_CONFIG(tooltip)
        self.label_thumbSeq.setText(QCoreApplication.translate("MainWindow", u"label_thumbSeq", None))
#if QT_CONFIG(tooltip)
        self.label_thumbShot.setToolTip(QCoreApplication.translate("MainWindow", u"label_thumbShot", None))
#endif // QT_CONFIG(tooltip)
        self.label_thumbShot.setText(QCoreApplication.translate("MainWindow", u"label_thumb", None))
#if QT_CONFIG(tooltip)
        self.label_thumbTask.setToolTip(QCoreApplication.translate("MainWindow", u"label_thumbTask", None))
#endif // QT_CONFIG(tooltip)
        self.label_thumbTask.setText(QCoreApplication.translate("MainWindow", u"label_thumbTask", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_sceneLocation.setToolTip(QCoreApplication.translate("MainWindow", u"lineEdit_sceneLocation", None))
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
#if QT_CONFIG(tooltip)
        self.pushButton_CompLatestRv.setToolTip(QCoreApplication.translate("MainWindow", u"pushButton_CompLatestRv", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_CompLatestRv.setText(QCoreApplication.translate("MainWindow", u"tmp.RvCompLastVer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_developing), QCoreApplication.translate("MainWindow", u"developing", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider_echoSwitch.setToolTip(QCoreApplication.translate("MainWindow", u"horizontalSlider_echoSwitch", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

