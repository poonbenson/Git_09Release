winTitlePrefix = 'BigKeeper_20220713a'

# path of bigKeeperTest_publish : N:\BigKeeper
# WIP of bigKeeperTest_publish : I:\iCloud~com~omz-software~Pythonista3\pySide2UI\wip

# To import QT modules
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# To import standard modules
import subprocess, os, sys, time, webbrowser


if sys.version_info.major >= 3:
    import configparser


# ref: https://www.daniweb.com/programming/software-development/threads/265576/how-can-i-specify-the-size-of-the-python-command-line-window-in-my-code
os.system("mode con cols=100 lines=10")

# To import XML modules
import xml.etree.ElementTree as ET

# To determine current software environment at
sys.path.append(r'N:\bpPipeline\bigKeeperPy\py\BigKeeperGlob\wip\published')
import bigCodingAssistant_publish
CurrentSoftwareName = bigCodingAssistant_publish.tool().bigCheckSoftware()

import bigKeeperInfoGlobal_published
getBigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
print('currentSoftwareName is: {}'.format(CurrentSoftwareName))

try:
    print('__file__:')
    print(__file__)
    thisPyPath = __file__
except:
    print('sys argv:')
    print(sys.argv[0])
    print('sys argv done')
    thisPyPath = sys.argv[0]

# Pre-Define Global Variables
pathOfIconPathsStudio = r'N:\bpPipeline\bigKeeperPyIni\bigPathsStudio.ini'

edge_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

# To determine current version mode (developer, tester or release)
pathOfDeveloper = r'N:\bpPipeline\bigKeeperPy\repo_01Developer'
pathOfTester = r'N:\bpPipeline\bigKeeperPy\repo_03Tester'
pathOfRelease = r'N:\bpPipeline\bigKeeperPy\repo_09Release'
pathOfEnvIni = r'N:\bpPipeline\bigKeeperPyIni\env.ini'




thisPath = (os.path.dirname(os.path.abspath(thisPyPath)))
print('this Path ' + thisPath)


if thisPath == pathOfDeveloper:
    bannerImage = r"N:\bpPipeline\bigKeeperPy\bigKeeperPyIcon_developer.jpg"
    uiPath = os.path.join(pathOfDeveloper, 'ui')
    iconPath = os.path.join(pathOfDeveloper, 'icon')
elif thisPath == pathOfTester:
    bannerImage = r"N:\bpPipeline\bigKeeperPy\bigKeeperPyIcon_tester.jpg"
    uiPath = os.path.join(pathOfTester, 'ui')
    iconPath = os.path.join(pathOfTester, 'icon')
elif thisPath == pathOfRelease:
    bannerImage = r"N:\bpPipeline\bigKeeperPy\bigKeeperPyIcon_release.jpg"
    uiPath = os.path.join(pathOfRelease, 'ui')
    iconPath = os.path.join(pathOfRelease, 'icon')
else:
    #eg. for In Python IDE, Standalone
    bannerImage = r"N:\bpPipeline\bigKeeperPy\bigKeeperPyIcon_InPythongOrDCC.jpg"
    uiPath = os.path.join(pathOfRelease, 'ui')
    iconPath = os.path.join(pathOfRelease, 'icon')

##print('line52')
##print(CurrentSoftwareName)
##print('line54')

import bigKeeperInfoGlobal_published

##print('line58')
##print(CurrentSoftwareName)
##print('line60')
#bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()

# To import compiled UI that created from QT Designer

#sys.path.append(r'N:\bpPipeline\bigKeeperPy')
#import bigKeeperPyUi as UiPy # path of compiled py : N:\BigKeeper          WIP : N:\BigKeeper\py\pySide2UI\ui
#import childMenu as UiPyChild # path : N:\BigKeeper         WIP : N:\BigKeeper\py\pySide2UI\ui
#import listView as UiList  # path : N:\BigKeeper         WIP : N:\BigKeeper\py\pySide2UI\ui
#sys.path.remove(r'N:\bpPipeline\bigKeeperPy')



sys.path.append(uiPath)
import bigKeeperPyUi_newLayout as UiPy
sys.path.remove(uiPath)

sys.path.append(r'N:\bpPipeline\bigKeeperPy\py\pySide2UI\ui')
import listView_dev as UiList
import DialogWindow as UiDialog # path : N:\BigKeeper\py\pySide2UI\ui        WIP : I:\iCloud~com~omz-software~Pythonista3\pySide2UI\ui
import doneWindow as UiDone
import nukeReadNodeFrameInOut as UiNukeTemp
import newTaskWindow as UiNewTask
import presetWindow as UiPreset
sys.path.remove(r'N:\bpPipeline\bigKeeperPy\py\pySide2UI\ui')

sys.path.append(r'N:\bpPipeline\bigKeeperPy\py\externalPyModule')



# To initiate current software environment variables
externalToolPath = r'N:\bpPipeline\bigKeeperPy\py\externalTool'
rvPath = r'C:\Program Files\Shotgun\RV-2021.0.0\bin\rv.exe'
rvTemplate = r'N:\bpPipeline\rv\_bigkeeperPyData\rv.template'
in_nuke = None
in_maya = None
in_houdini = None
in_blender  = None
in_python = None
nukeWrongFormatProj = ['WOF', 'PoonFilm']
bigKeeperCacheFolderPath = os.path.join(os.environ['LOCALAPPDATA'], 'bigKeeperPy')

print(os.path.isdir(bigKeeperCacheFolderPath))
if not os.path.isdir(bigKeeperCacheFolderPath):
    os.mkdir(bigKeeperCacheFolderPath)
print(os.path.isdir(bigKeeperCacheFolderPath))

##print('line98')
if CurrentSoftwareName == 'nuke':
    ##print('line100')
    in_nuke = True
    import nuke
    import nukescripts
    cacheProjName = r'projCache_nuke.txt'
    wipExtension = r'.nk'
elif CurrentSoftwareName == 'maya':
    in_maya = True
    import maya.cmds as cmds
    cacheProjName = r'projCache_maya.txt'
    wipExtension = r'.mb'
elif CurrentSoftwareName == 'houdini':
    in_houdini = True
    import hou
    cacheProjName = r'projCache_houdini.txt'
    wipExtension = r'.hip'
elif CurrentSoftwareName == 'blender':
    in_blender = True
    import bpy
    cacheProjName = r'projCache_blender.txt'
    wipExtension = r'.blend'
elif CurrentSoftwareName == 'python':
    in_python = True
    cacheProjName = r'projCache_python.txt'
    wipExtension = r'.py'

if in_python:
    try:
        app = QApplication()
    except:
        pass
else:
    pass

print(cacheProjName)



# The QT MainWindow Class
class BigMainWindow(UiPy.Ui_MainWindow, QMainWindow):

    dlg_instance = None # maintain a single instance of the dialog in Production
    @classmethod
    def show_window(cls):
        try:
            if not cls.dlg_instance:
                cls.dlg_instance = BigMainWindow()

            if cls.dlg_instance.isHidden():
                cls.dlg_instance.show()
            else:
                cls.dlg_instance.raise_()
                cls.dlg_instance.activateWindow()
        except:
            window = BigMainWindow()
            window.show()

    def printdbug(self, isToken, inText):
        if isToken:
            print(inText)

    def SoftwareMainWindow(self):
        self.main_window_ptr = QApplication.activeWindow()
        return self.main_window_ptr

    def __init__(self):
        super(BigMainWindow, self).__init__(parent = self.SoftwareMainWindow())
        self.setupUi(self)
        #self.setWindowTitle(r'BigKeeper Py - alpha version - Developer Mode')
        WindowTitleName = winTitlePrefix + ' BigKeeperPy-alpha ' + os.path.basename(thisPath)
        self.setWindowTitle(WindowTitleName)
        self.setWindowIcon(QIcon(os.path.join(iconPath, 'standalone.png')))
        self.prerendKeyword = ""

        #self.label_9.setPixmap(QPixmap(r"N:/bpPipeline/bigKeeperPy/bigKeeperPyIcon_developer.jpg"))
        self.label_9.setPixmap(QPixmap(bannerImage))
        self.label_9.setScaledContents(False)
        self.label_mayaIcon.setPixmap(QPixmap(os.path.join(iconPath, 'maya.png')))
        self.label_mayaIcon.setScaledContents(True)
        self.label_nukeIcon.setPixmap(QPixmap(os.path.join(iconPath, 'nuke.png')))
        self.label_nukeIcon.setScaledContents(True)
        self.label_houdiniIcon.setPixmap(QPixmap(os.path.join(iconPath, 'houdini.png')))
        self.label_houdiniIcon.setScaledContents(True)


        self.comboBoxEntries = self.listBigKeeperProject()
        self.comboBoxEntries.sort()
        self.comboBoxProjects.addItems(self.comboBoxEntries)
        self.pushButton_2.clicked.connect(self.launchProjExplorer)

        # prepare for storing and reload last selected project
        previousSelDetail = self.readProjCache()
        previousProj = previousSelDetail[0]
        print('previousProj is :')
        print(previousProj)

        try:
            self.comboBoxProjects.setCurrentText(previousProj)
            self.comboBoxAction2(previousProj)
        except:
            pass


        #self.comboBoxProjects.activated.connect(self.comboBoxAction1) #show position of the items
        self.comboBoxProjects.activated[str].connect(self.comboBoxAction2) #show content of the items as a string

        self.listWidget_1.itemClicked.connect(self.listWidget_2_appear2)
        self.listWidget_1.itemClicked.connect(self.listWidget_1_receivedList)

        self.listWidget_2.itemClicked.connect(self.listWidget_3_appear)
        #self.listWidget_3.itemDoubleClicked.connect(self.listWidget_3B_action)
        self.listWidget_3.itemDoubleClicked.connect(self.listWidget_3C_action)
        self.listWidget_3.itemClicked.connect(self.listWidget_shotTask_action)
        self.pushButton_listWidget1Refresh.clicked.connect(self.listWidget_1_appear)

        self.listWidget_1.setSelectionMode(QListWidget.ExtendedSelection)


        #nukeLabel = self.envRead('NUKE', 'label')
        #mayaLabel = self.envRead('MAYA', 'label')

        self.pushButton_LaunchMaya2022_update0.clicked.connect(self.launchStudioEnvMaya)
        self.pushButton_LaunchMaya2022_update0.setText(self.envRead('MAYA', 'label'))
        #self.pushButton_LaunchNuke13_0_v2.clicked.connect(self.launchStudioEnvNuke)
        self.pushButton_LaunchNuke13_0_v2.clicked.connect(self.launchStudioEnvNuke)
        self.pushButton_LaunchNuke13_0_v2.setText(self.envRead('NUKE', 'label'))

        #Temp workaround !!!!!!!!!! #Temp workaround !!!!!!!!!! #Temp workaround !!!!!!!!!! #Temp workaround !!!!!!!!!!
        #if os.path.isdir(r'c:\Program Files\Nuke13.0v3'):
            #self.pushButton_LaunchNuke13_0_v2.setText(nukeLabel)
        self.pushButton_LaunchNukeX13_0_v2.clicked.connect(self.launchStudioEnvNukeX)
        self.pushButton_LaunchNukeX13_0_v2.setEnabled(True)
        self.pushButton_LaunchNukeAssist13_0_v2.clicked.connect(self.launchStudioEnvNukeAssist)
        self.pushButton_LaunchNukeAssist13_0_v2.setEnabled(True)
        self.pushButton_LaunchNukeStudio13_0_v2.clicked.connect(self.launchStudioEnvNukeStudio)
        self.pushButton_LaunchNukeStudio13_0_v2.setEnabled(True)
        self.pushButton_LaunchHieroPlayer.clicked.connect(self.launchStudioEnvNukeStudioHiero)
        self.pushButton_LaunchHieroPlayer.setEnabled(True)
        self.pushButton_LaunchHieroPlayer.setText(self.envRead('HIERO', 'label'))

        self.pushButton_launchHoudini1.clicked.connect(self.launchStudioEnvHoudini)
        self.pushButton_launchHoudini1.setText(self.envRead('HOUDINI', 'label'))


        self.pushButton_mayaOther.clicked.connect(self.launchStudioEnvMayaFolder)
        self.pushButton_mayaOther.setText(self.envRead('MAYA', 'batFolderPathLabel'))
        self.pushButton_nukeOther.clicked.connect(self.launchStudioEnvNukeFolder)
        self.pushButton_nukeOther.setText(self.envRead('NUKE', 'batFolderPathLabel'))
        self.pushButton_houdiniOther.clicked.connect(self.launchStudioEnvHoudiniFolder)
        self.pushButton_houdiniOther.setText(self.envRead('HOUDINI', 'batFolderPathLabel'))
        self.pushButton_hieroPlayerOther.clicked.connect(self.launchStudioEnvNukeStudioHieroOther)
        self.pushButton_hieroPlayerOther.setText(self.envRead('HIERO', 'batFolderPathLabel'))

        self.pushButton_dailyFolder.clicked.connect(self.launchDailyFolder)
        self.pushButton_dailyFolder2.clicked.connect(self.launchDailyFolder)

        self.pushButton_LaunchCpuCoreController.clicked.connect(lambda: self.deadlineCoreOverride())
        self.pushButton_LaunchCpuCoreController.setText('Deadline Override CPU Core\n Controller')


        self.pushButton_shotlist.clicked.connect(self.launchShotlist)
        self.pushButton_shotlist.setText(self.iconPathRead(pathOfIconPathsStudio, 'SHOTLIST', 'label'))

        self.pushButton_roughcut.clicked.connect(self.launchRoughcut)
        self.pushButton_roughcut.setText(self.iconPathRead(pathOfIconPathsStudio, 'ROUGHCUT', 'label'))

        self.pushButton_commentClient.clicked.connect(self.launchCommentClient)
        self.pushButton_commentClient.setText(self.iconPathRead(pathOfIconPathsStudio, 'COMMENTCLIENT', 'label'))

        self.pushButton_miscCookbook.clicked.connect(self.launchMiscCookbook)
        self.pushButton_miscCookbook.setText(self.iconPathRead(pathOfIconPathsStudio, 'LEARNING', 'label'))

        self.pushButton_miscLoginInfo.clicked.connect(self.launchMiscLoginInfo)
        self.pushButton_miscLoginInfo.setText(self.iconPathRead(pathOfIconPathsStudio, 'LOGINS', 'label'))

        self.pushButton_miscStaffContact.clicked.connect(self.launchStaffContact)
        self.pushButton_miscStaffContact.setText(self.iconPathRead(pathOfIconPathsStudio, 'STAFFCONTACT', 'label'))






        self.pushButton_7zip.clicked.connect(self.myAction2)
        self.pushButton_action1.clicked.connect(self.myAction3)
        #self.pushButton_action1.clicked.connect(self.dialog)

        self.pushButton_19.clicked.connect(self.myAction5)
        self.pushButton_Location_2.clicked.connect(self.openCurrentOpeningLocationPath)
        self.pushButton_versionUp.clicked.connect(self.versionUpSaveWIP)
        self.pushButton_versionUp.setStyleSheet("background-color:rgb(204,153,128); color:rgb(136, 77, 85)")
        #self.pushButton_versionUp.setVisible(False)



        self.childUi = ChildWindow(parent = self)
        self.wrongFormatUi = subListView(parent = self)
        self.wrongFormatUi.listWidget.itemDoubleClicked.connect(self.listWidget_A_action)
        self.wrongFormatUi.pushButton_exec.clicked.connect(lambda : self.listWidget_A_action(self.wrongFormatUi.listWidget.currentItem()))
        self.wrongFormatUi.setWindowTitle('Edit task in Wrong-Format-Projects')

        self.compPreviousVerUi = subListView(parent = self)
        self.compPreviousVerUi.listWidget.itemDoubleClicked.connect(self.shotAction3Action)
        self.compPreviousVerUi.pushButton_exec.clicked.connect(lambda : self.shotAction3Action(self.compPreviousVerUi.listWidget.currentItem()))
        self.compPreviousVerUi.setWindowTitle('RV Review Comp Previous ver')

        #self.prerendKeywordListUi  = prerendKeywordListView(parent = self)

        self.dialogUi = NewWIPDialogWindow(parent = self)
        self.doneUi = doneWindow(parent = self)
        self.initializeNewWIPDialogWindow()
        self.createShotNewTaskUi = createShotNewTaskWindow(parent = self)
        self.prerendKeywordUi = nukeAskKeywordWindow(parent = self)
        self.initializePrerendKeywordUi()


        self.pushButton_scnUpdate.clicked.connect(self.launchSceneUpdate)

        self.reviveUi = subListView(parent = self)
        self.reviveUi.listWidget.itemDoubleClicked.connect(self.reviveOpenAction)
        self.reviveUi.pushButton_exec.clicked.connect(lambda : self.reviveOpenAction(self.reviveUi.listWidget.currentItem()))
        self.reviveUi.setWindowTitle('Revive previous version')
        self.pushButton_revive.clicked.connect(self.reviveAction)
        self.pushButton_revive.setStyleSheet("background-color:rgb(128,179,179); color:rgb(10, 10, 10)")
        self.pushButton_revive.setEnabled(True)
        self.pushButton_closeNukeScript.clicked.connect(self.pretendCloseNukeScript)
        self.pushButton_newTask.clicked.connect(self.createShotNewTask_appear)
        self.pushButton_getFrameRange.clicked.connect(self.getCurrentFrameInfo)
        self.pushButton_getFrameRange.setStyleSheet("background-color:rgb(128,179,179); color:rgb(10, 10, 10)")
        if in_nuke:
            self.pushButton_getFrameRange.setText('Get Frame Range\n- Project Setting-')

            self.nukeTempUi = nukeTempWindow(parent = self)
            self.pushButton_NukeReadNodeTempTool.clicked.connect(self.nukeTempTool1)
            #self.pushButton_NukeReadNodeTempTool.clicked.connect(self.nukeTempUi.LoadInOutFrame())
            self.nukeTempUi.initializeNukeTempWindow()

        else:
            self.pushButton_getFrameRange.setText('Get Frame Range')
            self.pushButton_NukeReadNodeTempTool.setVisible(False)

        self.createShotNewTaskUi.pushButton_execute.clicked.connect(self.createShotNewTaskAction)
        self.createShotNewTaskUi.pushButton_cancel.clicked.connect(self.createShotNewTaskClose)

        self.pushButton_CompLatestRv.clicked.connect(self.compLatestRvAction)



        self.initDummy()

        #self.getBigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()




        #self.pushButton_openCal.clicked.connect(lambda: self.openScheduleLink())
        self.pushButton_openCal.clicked.connect(lambda: self.openTeam11Folder())
        self.pushButton_openCal.setText('Team11 Schedule')
        self.pushButton_openCal2.clicked.connect(lambda: self.openTeam12Folder())
        self.pushButton_openCal2.setText('Team12 Schedule')


        # Nuke Tab
        #self.pushButton_genWritePrerend.clicked.connect(lambda : self.nukeBornWriteNode('PreRend'))
        self.pushButton_genWritePrerend.clicked.connect(lambda: self.prerendKeywordShow())
        self.pushButton_genWritePrerend.setText('Prerend')
        self.pushButton_genWriteLayerMask.clicked.connect(lambda : self.nukeBornWriteNode('LayerMask'))
        self.pushButton_genWriteLayerMask.setText('LayerMask')
        self.pushButton_genWriteCompMaster.clicked.connect(lambda : self.nukeBornWriteNode('CompMaster'))
        self.pushButton_genWriteCompMaster.setText('CompMaster')
        self.pushButton_genWriteCompMasterV.clicked.connect(lambda : self.nukeBornWriteNode('CompMasterToV'))
        self.pushButton_genWriteCompMasterV.setText('CompMaster-V')

        #Cmd Tab
        self.pushButton_sortoutfile.clicked.connect(lambda: self.cleanUpCompOutput(self.listWidget_1.selectedItems()))
        self.pushButton_exeDel.clicked.connect(lambda: self.cleanUpDelAction())


        self.listBigKeeperProject()

        self.updateCurrentOpeningLocationPath()
        self.tabWidget.setCurrentIndex(0)

        self.pushButton_shotAction.setText('shotActionMenu')
        self.shotActionMenu = QMenu(self.pushButton_shotAction)
        self.shotAction1 = QAction('Edit Shot Task', self)
        #self.shotAction2 = QAction('RV latest Comp Output', self)
        self.shotAction3 = QAction('RV Build & Review Comp Latest ver', self)
        self.shotAction4 = QAction('RV Review Comp Previous ver', self)
        self.shotActionMenu.addAction(self.shotAction1)
        #self.shotActionMenu.addAction(self.shotAction2)
        self.shotActionMenu.addAction(self.shotAction3)
        self.shotActionMenu.addAction(self.shotAction4)
        self.pushButton_shotAction.setMenu(self.shotActionMenu)
        self.shotAction1.triggered.connect(self.shotAction1Action)
        #self.shotAction2.triggered.connect(self.shotAction2Action)
        self.shotAction3.triggered.connect(self.shotAction3Action)
        self.shotAction4.triggered.connect(self.shotAction4Action)

        # set the only active tab in related software.
        tabCount = self.tabWidget_2.count()
        print('\n\n\n\n\n\tabCount : \n\n\n\n\n\n\n')
        print(tabCount)
        for i in range(0, tabCount):
            self.tabWidget_2.setTabEnabled(i, False)

        self.tabWidget_2.setTabEnabled(6, True)

        if sys.version_info.major >= 3:
            self.tabWidget_2.setTabEnabled(5, True)

        if in_maya:
            self.tabWidget_2.setTabEnabled(0, True)
            self.tabWidget_2.setCurrentIndex(0)
        elif in_nuke:
            self.tabWidget_2.setTabEnabled(1, True)
            self.tabWidget_2.setTabEnabled(4, True)
            self.tabWidget_2.setCurrentIndex(1)
        elif in_houdini:
            self.tabWidget_2.setTabEnabled(2, True)
            self.tabWidget_2.setCurrentIndex(2)
        elif in_blender:
            self.tabWidget_2.setTabEnabled(3, True)
            self.tabWidget_2.setCurrentIndex(3)
        elif in_python:
            self.tabWidget_2.setTabEnabled(4, True)
            self.tabWidget_2.setCurrentIndex(5)


        if in_python == False and in_blender == False:
            # to avoid "hard to find it back after minimize", workaroun is to disable the minimize
            self.setWindowFlags(Qt.WindowCloseButtonHint)



        # This to a temp. and bad way to parenet on the working software and on-top. Current can't find correct way to do so.
        if in_blender:
            self.setWindowFlags(Qt.WindowStaysOnTopHint)

        #if not in_python and not in_nuke and not in_houdini and not is_iDriveDeveloper:
        if not in_python:
            #self.pushButton_shotAction.setEnabled(False)
            self.shotAction3.setDisabled(True)
            self.shotAction4.setDisabled(True)


        '''# ref : https://www.qtcentre.org/threads/34073-QTabWidget-tab-button-color(-how-to-set-)
        # ref : https://www.youtube.com/watch?v=ou1ynsJxRLA
        stylesheet = """

        QWidget {
            background-color: rgba(70,70,70,250);
            color : rgba(250, 250, 250, 255);
            font-size: 6pt;
            text-shadow: none;
        }

        QPushButton {
            text-shadow: none;
        }

        QTabWidget {
            font-size: 6pt;
            background-color: rgba(0,100,0,255);
            border-width: 2px;
            border-style: solid;
            border-color: rgba(5, 5, 5, 255);
        }

        QListWidget {
           background-color: rgba(0,100,0,255);
        }

        QTabBar::tab  {
            background : rgba(90, 90, 90, 255);
            color : rgba(250, 250, 250, 255);
        }

        QTabWidget::pane {
            margin: 1px,1px,1px,1px;
            background-color: rgba(255,255,255, 255);
            border: 2px solid rgb(0,149,48);
            border-bottom-color: rgb(255,255,255);
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            border-color: rgba(5, 5, 5, 255);
            background-color: rgb(255,255,255);
        }

        QTabBar::tab:selected {
            color: red;
            background-color: rgb(255,255,255);
        }

        """
        self.setStyleSheet(stylesheet)'''


        '''if in_houdini:
            #ref: https://www.sidefx.com/docs/houdini/hom/hou/qt/styleSheet.html
            stylesheet = hou.qt.styleSheet()
            self.setStyleSheet(stylesheet)'''

        # ref : https://www.qtcentre.org/threads/34073-QTabWidget-tab-button-color(-how-to-set-)
        # ref : https://www.youtube.com/watch?v=ou1ynsJxRLA
        if in_houdini:
            stylesheet = """
            QWidget {
                background-color: rgba(70,70,70,255);
                color : rgba(250, 250, 250, 255);
                font-size : 10pt;
            }




            """
            self.setStyleSheet(stylesheet)
            #self.setStyleSheet(hou.qt.styleSheet())





    def initDummy(self):
        '''
        #self.pushButton_childUi.clicked.connect(self.myAction4)
        #self.pushButton_num3.clicked.connect(lambda: self.cleanUpCheckFolderSize(self.selProjScnPath))
        #self.pushButton_num3.clicked.connect(lambda: self.cleanUpCheckFolderSize(self.selProjScnShotTaskPath))
        self.pushButton_num3.clicked.connect(lambda : self.nukeBornWriteNode('CompMasterToV'))
        self.pushButton_num3.setText('*Write to V:*')
        #self.pushButton_num3.clicked.connect(lambda: self.cleanUpCheckFolderSize(self.selProjScnShotTaskWIPPath))
        self.pushButton_num2.clicked.connect(lambda : self.prerendKeywordPresetShow())
        self.pushButton_num2.setText('*presetButton*')
        self.pushButton_num1.clicked.connect(self.listWidget_1_appear)
        self.pushButton_num1.setText('refresh seq')
        self.pushButton_num4.clicked.connect(lambda: self.envRead('NUKE', 'label'))
        self.pushButton_num4.setText('label')
        self.pushButton_num5.clicked.connect(self.launchSceneUpdate)
        self.pushButton_num5.setText('Scn Update')
        self.pushButton_num6.clicked.connect(lambda: self.nukeUpdateReadNodeVer())
        self.pushButton_num6.setText('UpReadVer')
        self.pushButton_num9.clicked.connect(lambda: self.cleanUpDelAction())
        self.pushButton_num9.setText('cleanUpDelAction')
        self.pushButton_num8.clicked.connect(lambda: self.openScheduleLink())
        self.pushButton_num8.setText('openScheduleLink')
        '''
        self.pushButton_num7.clicked.connect(lambda: self.listWidget_1_receivedListB())
        self.pushButton_num7.setText('listMulti')

    def listWidget_1_receivedList(self, item):
        print('my listWidget_1_receivedList')
        print(item.text())
        #print(self.listWidget_1.)
        for i in self.listWidget_1.selectedItems():
            print(i.text())

    def listWidget_1_receivedListB(self):
        print('my listWidget_1_receivedListB')

        for i in self.listWidget_1.selectedItems():
            print(i.text())


    def deadlineCoreOverride(self):
        subprocess.call(r'python N:\bpPipeline\miscScriptTools\deadline_cmd\get_cmd_output_deadlineInfo_publish.py', shell=True)
        #os.system(r'N:\bpPipeline\miscScriptTools\deadline_cmd\get_cmd_output_deadlineInfo_publish.py')




    def envRead(self, inSection, inKey):
        print('my envRead')

        try:
            def addLine(inStr):
                seperator = r'\n'
                splitText = inStr.split(seperator)
                joinText = '\n'.join(splitText)

                return joinText

            config = configparser.ConfigParser()
            #config.read(r'./myConfigINI.py')
            config.read(pathOfEnvIni)

            theInfo = config[inSection]

            if inKey == 'label':
                return str(addLine(theInfo[inKey]))
            else:
                return theInfo[inKey]
        except:
            print('configparser fail, pass.')


    def vDrivePathRead(self, inPath, inSection, inKey):
        print('vDrivePathRead')

        config = configparser.ConfigParser()
        config.read(inPath)

        theInfo = config[inSection]

        return str(theInfo[inKey])




    def iconPathRead(self, inPath, inSection, inKey):
        print('my inconPathRead')

        config = configparser.ConfigParser()
        config.read(inPath)

        theInfo = config[inSection]

        return str(theInfo[inKey])


    def launchShotlist(self):
        print('my launchShotlist')

        getBigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
        print(os.path.join(self.subDict[self.selProjPath], 'bigPathsProject.ini'))
        #print(os.path.join(self.selProjRootPath, 'bigPathsProject.ini'))

        #webbrowser.open(self.iconPathRead('SHOTLIST', 'Path'), new = 2)
        #webbrowser.open(self.iconPathRead(os.path.join(self.subDict[self.selProjPath], 'bigPathsProject.ini'), 'SHOTLIST', 'Path'), new = 2)
        webbrowser.get('edge').open(self.iconPathRead(os.path.join(self.subDict[self.selProjPath], 'bigPathsProject.ini'), 'SHOTLIST', 'Path'))

    def launchCommentClient(self):
        print('my launchCommentClient')

        os.startfile(os.path.normpath(os.path.join(self.selProjRootPath, 'Comment')))


    def launchRoughcut(self):
        print('my launchRoughcut')

        try:
            os.startfile(os.path.normpath(os.path.join(self.selProjRootPath, 'Roughcut', '__latestMov')))
        except:
            os.startfile(os.path.normpath(os.path.join(self.selProjRootPath, 'Roughcut')))


    def launchMiscCookbook(self):
        print('my launchMiscCookbook')
        print(self.iconPathRead(pathOfIconPathsStudio, 'LEARNING', 'Path'))

        os.startfile(self.iconPathRead(pathOfIconPathsStudio, 'LEARNING', 'Path'))



    def launchMiscLoginInfo(self):
        print('my launchMiscLoginInfo')
        print(self.iconPathRead(pathOfIconPathsStudio, 'LOGINS', 'Path'))

        os.startfile(self.iconPathRead(pathOfIconPathsStudio, 'LOGINS', 'Path'))



    def launchStaffContact(self):
        print('my launchStaffContact')
        print(self.iconPathRead(pathOfIconPathsStudio, 'STAFFCONTACT', 'Path'))

        os.startfile(self.iconPathRead(pathOfIconPathsStudio, 'STAFFCONTACT', 'Path'))




    def launchStudioEnvMaya(self):
        #theCmd = 'start {}'.format(studioEnvMaya)
        theCmd = 'start {}'.format(os.path.join(self.envRead('MAYA', 'batPath'), 'studioEnv.bat'))
        print(theCmd)
        os.system(theCmd)

    def launchStudioEnvNuke(self):

        #theCmd = 'start {}'.format(studioEnvNuke)
        theCmd = 'start {}'.format(os.path.join(self.envRead('NUKE', 'batPath'), 'studioEnv.bat'))
        print(theCmd)
        os.system(theCmd)

    def launchStudioEnvNukeAssist(self):
        #theCmd = 'start {}'.format(studioEnvNukeAssist)
        theCmd = 'start {}'.format(os.path.join(self.envRead('NUKE', 'batPath'), 'studioEnvAssist.bat'))
        print(theCmd)
        os.system(theCmd)

    def launchStudioEnvNukeX(self):
        #theCmd = 'start {}'.format(studioEnvNukeX)
        theCmd = 'start {}'.format(os.path.join(self.envRead('NUKE', 'batPath'), 'studioEnvX.bat'))
        print(theCmd)
        os.system(theCmd)

    def launchStudioEnvNukeStudio(self):
        #theCmd = 'start {}'.format(studioEnvNukeStudio)
        theCmd = 'start {}'.format(os.path.join(self.envRead('NUKE', 'batPath'), 'studioEnvStudio.bat'))
        print(theCmd)
        os.system(theCmd)

    def launchStudioEnvNukeStudioHiero(self):
        theCmd = 'start {}'.format(os.path.join(self.envRead('HIERO', 'batPath'), 'nukeHieroPlayer.bat'))
        print(theCmd)
        os.system(theCmd)


    def launchStudioEnvHoudini(self):
        theCmd = 'start {}'.format(os.path.join(self.envRead('HOUDINI', 'batPath'), 'studioEnv.bat'))
        print(theCmd)
        os.system(theCmd)

    def launchStudioEnvMayaFolder(self):
        theCmd = self.envRead('MAYA', 'batFolderPath')
        os.startfile(theCmd)

    def launchStudioEnvNukeFolder(self):
        theCmd = self.envRead('NUKE', 'batFolderPath')
        os.startfile(theCmd)

    def launchStudioEnvNukeStudioHieroOther(self):
        theCmd = self.envRead('HIERO', 'batFolderPath')
        os.startfile(theCmd)


    def launchStudioEnvHoudiniFolder(self):
        theCmd = self.envRead('HOUDINI', 'batFolderPath')
        os.startfile(theCmd)

    def launchDailyFolder(self):
        dailyPath = os.path.join(self.subDict[self.selProjPath], 'daily')

        if os.path.isdir(dailyPath):
            print('selProjPath is {}'.format(dailyPath))
        else:
            print('no daily fold exist, created now.')
            os.mkdir(dailyPath)
            QMessageBox.information(self, 'Daily Folder not found', 'No existing Daily folder.\nFolder is created: {}'.format(dailyPath))


        os.startfile(dailyPath)

    def launchProjExplorer(self):
        print(self.selProjRootPath)
        os.startfile(self.selProjRootPath)


    def launchSceneUpdate(self):
        if in_maya:
            from daniel import sceneUpdate_maya as susu
        elif in_nuke:
            from daniel import sceneUpdate_nuke as susu
        else:
            from daniel import sceneUpdate as susu
        susu.run()


    def nukeUpdateReadNodeVer(self):
        print('my nukeUpdateReadNodeVer')

        allNodes = nuke.allNodes(filter = 'Read')
        print(allNodes)
        print(len(allNodes))
        print(type(allNodes))

        for i in allNodes:
            print(i.name())
            print(i.knob('file').getValue())
            filePath = i.knob('file').getValue()
            sepList = filePath.split('/')
            print(sepList)

            frameFullName = sepList[-1]
            frameFolder = sepList[-2]
            frameCurrentVer = sepList[-3]

            self.nukeReadNodeFindOtherVer(filePath, frameCurrentVer)



    def nukeReadNodeFindOtherVer(self, inFullPath, inSeperator):
        print('my nukeReadNodeFindOtherVer')

        sepList = inFullPath.split('')

    def openScheduleLink(self):
        print(' my openScheduleLink')
        webbrowser.open('https://calendar.google.com/calendar/r', new = 2)

    def openScheduleFolder(self):
        print('my openScheduleFolder')
        thePath = r'N:\mnt\job\21044ChongFilm\Doc\Schedule\_publishPDF'
        os.startfile(thePath)

    def openTeam11Folder(self):
        print('my openTeam11Folder')
        thePath = r'N:\mnt\job\21044ChongFilm\Doc\Schedule\_publishPDF\team11'
        theLastPath = bigCodingAssistant_publish.tool.findLatestFolderVer(thePath)
        print(theLastPath)
        os.startfile(os.path.join(thePath, theLastPath))

    def openTeam12Folder(self):
        print('my openTeam12Folder')
        thePath = r'N:\mnt\job\21044ChongFilm\Doc\Schedule\_publishPDF\team12'
        theLastPath = bigCodingAssistant_publish.tool.findLatestFolderVer(thePath)
        print(theLastPath)
        os.startfile(os.path.join(thePath, theLastPath))


    """
    def loopQMessage(self):
        theMsg = ''
        QMessageBox.information(self, 'message', theMsg)
        for i in range(10):
            print(i)
            theMsg = str(i)
            time.sleep(1)

    '''def QMessageLoopTest(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setWindowTitle("Title")
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.setText("Start")
        self.msgBox.show()

        for x in range(100):
            self.msgBox.setText(str(x+1))
            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()'''

    def handleButton(self, inPathRoot):
        self.msgBox = QMessageBox(self)
        self.msgBox.setWindowTitle("Title")
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.setText("Start")
        self.msgBox.show()
        start_path = inPathRoot
        start_path = r'N:\mnt\job\19901BigPicture_TestProj'
        total_size = 0

        loop = QEventLoop()
        for path, dirs, files in os.walk(start_path):

            for f in files:
                fp = os.path.join(path, f)
                fileSize = os.path.getsize(fp)
                total_size += fileSize
                #print('\r>> total_size : %d' %total_size, end='', flush = True)
                self.msgBox.setText(str(total_size))
        loop.exec_()
        loop.quit

    def loopMessage2(self):
        loopWin = QMainWindow(self)
        loopWin.setWindowTitle('loop Win')


        label1 = QLabel('abc abc')
        label1.setAlignment(Qt.AlignCenter)
        loopWin.setCentralWidget(label1)

        loopWin.show()

        for i in range(999999):
            print(i)
            if i%199 == 0 :
                print('199')
                label1.setText(str(i))

        '''#start_path = inPathRoot
        start_path = r'N:\mnt\job\19901BigPicture_TestProj'
        total_size = 0

        for path, dirs, files in os.walk(start_path):

            for f in files:
                fp = os.path.join(path, f)
                fileSize = os.path.getsize(fp)
                total_size += fileSize
                print('\r>> total_size : %d' %total_size, end='', flush = True)
                label1.setText(str(total_size))'''

    """

    def activateCurrentTab(self):
        print('my activateCurrentTab')
        self.tabWidget.setCurrentIndex(0)
        self.updateCurrentOpeningLocationPath()


    def initializeMainWindow(self):
        pass


    '''
    def comboBoxAction1(self, item):
        self.comboBoxAction1ReceiveItem = item
        print("my comboBoxAction1")
        print(type(self.comboBoxAction1ReceiveItem))
        print(self.comboBoxAction1ReceiveItem)
        self.listWidget_2.clear()
        return self.comboBoxAction1ReceiveItem
    '''

    def listWidget_1_appear(self, item):
        print('my listWidget_1_appear')
        print(self.selProj)
        folderList = os.listdir(self.selProjScnPath)
        listSeq = []
        for i in folderList:
            if os.path.isdir(os.path.join(self.selProjScnPath, i)):
                listSeq.append(i)
        listSeq.sort()
        print('listSeq is :')
        print(listSeq) # eg. ['animaticSeq', 'balloonSeq', 'edits', 'socialSeq', 'testSeq', 'turnTableSeq', 'tvcSeq']
        self.list1Entries = []
        self.list1Entries = listSeq
        #self.listWidget_3.clear()
        #self.listWidget_2.clear()
        self.listWidget_1.clear()
        self.listWidget_1.addItems(self.list1Entries)


    def comboBoxAction2(self, item):
        if item != " ":
            self.comboBoxAction1ReceiveItem = item
            print('my comboBoxAction2')
            self.selProj = item
            self.selProjName = 'name'
            self.selProjPath = 'path'
            self.selProjLibCode = 'libraryfolder'
            self.selProjScnCode = 'scenesfolder'
            self.selProjWipCode = 'workshopname'
            self.selProjPublishCode = 'mastername'
            self.subDict = self.dictProj[self.selProj]

            # generating project Root path by split the path that read from xml information
            splitPath = os.path.splitdrive(os.path.normpath(self.subDict[self.selProjPath]))
            splitDrive = splitPath[0]
            splitTail = splitPath[1].split(os.path.sep)
            print('splitPath : {}'.format(splitPath))
            print('splitDrive : {}'.format(splitDrive))
            print('splitTail : {}'.format(splitTail))
            self.selProjRootPath = os.path.join(splitDrive, os.path.sep, splitTail[1], splitTail[2], splitTail[3])
            print('self.selProjRootPath : {}'.format(self.selProjRootPath))


            print('self.subDict[self.selProjName]:' + self.subDict[self.selProjName]) # eg. kfcPoke
            print('self.subDict[self.selProjPath]:' + self.subDict[self.selProjPath]) # eg. N:/mnt/job/19005kfcPoke/WorkingFile/kfcPoke/
            self.selProjScnPath = os.path.join(self.subDict[self.selProjPath], self.subDict[self.selProjScnCode])
            print('self.selProjScnPath:' + self.selProjScnPath) # eg. N:/mnt/job/19005kfcPoke/WorkingFile/kfcPoke/scenes
            print('self.subDict[self.selProjWipCode]:' + self.subDict[self.selProjWipCode]) # eg. wip
            print('self.subDict[self.selProjPublishCode]:' + self.subDict[self.selProjPublishCode]) # eg. published
            folderList = os.listdir(self.selProjScnPath)
            listSeq = []
            for i in folderList:
                if os.path.isdir(os.path.join(self.selProjScnPath, i)):
                    listSeq.append(i)
            listSeq.sort()
            print('listSeq is :')
            print(listSeq) # eg. ['animaticSeq', 'balloonSeq', 'edits', 'socialSeq', 'testSeq', 'turnTableSeq', 'tvcSeq']
            self.list1Entries = []
            self.list1Entries = listSeq
            self.listWidget_3.clear()
            self.listWidget_2.clear()
            self.listWidget_1.clear()
            self.listWidget_1.addItems(self.list1Entries)
            self.locationPath = self.subDict[self.selProjPath]
            self.lineEdit_Location.setText(self.locationPath)
            self.writeProjCache(self.selProj)


    def writeProjCache(self, item):
        thepath = os.path.join(bigKeeperCacheFolderPath, cacheProjName)
        f = open(thepath, 'w')
        cacheProj = (item)
        f.write(cacheProj)
        f.close()


    def readProjCache(self):
        try:
            thepath = os.path.join(bigKeeperCacheFolderPath, cacheProjName)
            f = open(thepath, 'r')
            readAllLines = f.readlines()
            f.close()
            return readAllLines
        except:
            return str(" ")




    def listWidget_2_appear2(self, item2):
        print('listWidget_2_appear2')

        #self.printdbug()

        self.listWidget_3.clear()
        print(item2)
        self.selProjScnItem = item2
        self.selProjScnName = item2.text()
        self.selProjScnShotPath = os.path.join(self.selProjScnPath, item2.text())
        folderList = os.listdir(self.selProjScnShotPath)
        self.listShot = []
        for i in folderList:
            if os.path.isdir(os.path.join(self.selProjScnShotPath, i)):
                self.listShot.append(str(i))
        print(self.selProjScnShotPath)
        print(self.listShot)
        self.listShot.sort()
        self.listWidget_2.clear()
        self.listWidget_2.addItems(self.listShot)
        self.locationPath = os.path.join(self.selProjScnPath, item2.text())
        self.lineEdit_Location.setText(self.locationPath)


    def listWidget_3_appear(self, item3):
        print('my listWidget_3_appear')



        print(item3.text())
        self.selShot = item3.text()
        self.selProjScnShotTaskPath = os.path.join(self.selProjScnShotPath, item3.text(), "components")
        folderList = os.listdir(self.selProjScnShotTaskPath)
        listTask = []
        for i in folderList:
            if os.path.isdir(os.path.join(self.selProjScnShotTaskPath, i)):
                listTask.append(str(i))
        print(listTask)
        listTask.sort()
        self.listWidget_3.clear()
        self.listWidget_3.addItems(listTask)
        self.locationPath = os.path.join(self.selProjScnShotPath, item3.text())
        self.lineEdit_Location.setText(self.locationPath)


    def listWidget_3C_action(self, item):
        print('my listWidget_3C_action')
        try:
            theItem = item.text()
        except:
            theItem = item
        self.selProjScnShotTaskWIPPath = os.path.join(self.selProjScnShotTaskPath, theItem, self.subDict[self.selProjWipCode])
        print(self.selProjScnShotTaskWIPPath)
        print(theItem)
        self.selTask = theItem

        #checkResult = self.createNewWIP(item)
        #print('checkResult is :')
        #print(checkResult)

        checkResult = 'yes'

        if checkResult != 'no' :
            self.listFile = self.listOutFilesInFolder()
            print(len(self.listFile))
            #fileCount = len(listFile)

            if in_nuke or in_houdini:
                if len(self.listFile) == 0:
                    self.myDialogShow2(r'Create New WIP?', r'You are about to edit a WIP for the 1st time. Would you like to start with an empty new WIP, or with the currently open WIP?')

                    #fileCount + 1
                else:
                    self.openLastestWIP()

            else:
                QMessageBox.information(self, 'message', 'Double-click to open\nis currently activate in Houdini and Nuke only.')

    def openLastestWIP(self):
        print('my openLastestWIP')

        self.listFile = self.listOutFilesInFolder()
        self.listFile.sort()
        print(self.listFile[-1])
        self.wrongFormatUi.listWidget.clear()
        if self.selProj in nukeWrongFormatProj:
            print('WRONG WRONG WRONG')
            #self.childUi.show()
            self.wrongFormatUi.listWidget.addItems(self.listFile)
            #self.wrongFormatUi.listWidget.itemDoubleClicked.connect(self.listWidget_A_action)
            #self.wrongFormatUi.listWidget.itemDoubleClicked.connect(self.listWidget_A_action)
            self.wrongFormatUi.show()

        else:
            if in_nuke:
                self.tabWidget.setCurrentIndex(0)
                if nuke.Root().modified() == True:
                    print('current changes have not yet been saved!')
                    nuke.scriptClose() ### pop a dialog instead of close.
                    if nuke.Root().modified() == False:
                        nuke.scriptOpen(os.path.join(self.selProjScnShotTaskWIPPath, self.listFile[-1]))
                        self.activateCurrentTab()

                else:

                    nuke.scriptClose()
                    nuke.scriptOpen(os.path.join(self.selProjScnShotTaskWIPPath, self.listFile[-1]))

                    # To avoid error message when launchSceneUpdate on a v0000
                    try:
                        #disabled this upon Apple and Sally request for a heavy shot.
                        #nuke.onScriptLoad(self.launchSceneUpdate())
                        QMessageBox.information(self, 'Auto Scene Update', 'Check if Scene Update is needed ?')
                    except:
                        pass

                    self.activateCurrentTab()
                    #window.close()
            elif in_houdini:
                    hou.hipFile.load(os.path.join(self.selProjScnShotTaskWIPPath, self.listFile[-1]))
                    self.activateCurrentTab()


            else:
                print('will open:', os.path.join(self.selProjScnShotTaskWIPPath, self.listFile[-1]))
                #subprocess.Popen([r'C:/Program Files/Nuke11.3v3/Nuke11.3.exe', os.path.join(self.selProjScnShotTaskWIPPath, listFile[-1])])
                #window.close()

        self.updateCurrentOpeningLocationPath()


    '''def initializeReviveListView(self):
        print('my initializeReviveListView')
        self.reviveUi.listWidget.itemDoubleClicked.connect(self.reviveOpenAction)
        self.COUNTinitializeReviveListView += 1
        print(self.COUNTinitializeReviveListView)'''

    def reviveAction(self):
        print('my reviveAction')
        bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
        listFile = bigKInfo.listOutFilesInFolder()
        print(listFile)

        self.reviveUi.listWidget.clear()
        self.reviveUi.listWidget.addItems(listFile)
        #self.reviveUi.listWidget.itemDoubleClicked.connect(self.reviveOpenAction)
        self.reviveUi.show()

    def reviveOpenAction(self, item):
        print('my reviveOpenAction')
        bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()

        self.reviveUi.close()
        if in_nuke:
            if nuke.Root().modified() == True:
                print('current changes have not yet been saved!')
                nuke.scriptClose() ### pop a dialog instead of close.
                if nuke.Root().modified() == False:
                    print(os.path.join(bigKInfo.currentPath(), item.text()))
                    nuke.scriptOpen(os.path.join(bigKInfo.currentPath(), item.text()))
                    self.activateCurrentTab()

            else:
                nuke.scriptClose()
                print(os.path.join(bigKInfo.currentPath(), item.text()))
                nuke.scriptOpen(os.path.join(bigKInfo.currentPath(), item.text()))
                self.activateCurrentTab()


        elif in_houdini:
            hou.hipFile.load(os.path.join(bigKInfo.currentPath(), item.text()))
            self.activateCurrentTab()


    def listOutFilesInFolder(self):
        print ('my listOutFilesInFolder')
        fileList = os.listdir(self.selProjScnShotTaskWIPPath)
        listFile = []
        for i in fileList:
            if i.find(self.subDict[self.selProjWipCode]) and os.path.isfile(os.path.join(self.selProjScnShotTaskWIPPath, i)):
                if i.endswith(wipExtension):
                    listFile.append(i)
        print(r'listFile in listOutFilesInFolder:')
        print(listFile)
        return listFile


    def listWidget_A_action(self, item):

        print('listWidget_A_action listWidget_A_action listWidget_A_action')
        print(item.text())
        print(os.path.join(self.selProjScnShotTaskWIPPath, item.text()))
        self.wrongFormatUi.close()
        if in_nuke:
            if nuke.Root().modified() == True:
                print('current changes have not yet been saved!')
                nuke.scriptClose() ### pop a dialog instead of close.
                if nuke.Root().modified() == False:
                    print(os.path.join(self.selProjScnShotTaskWIPPath, item.text()))
                    nuke.scriptOpen(os.path.join(self.selProjScnShotTaskWIPPath, item.text()))
                    self.activateCurrentTab()


            else:
                nuke.scriptClose()
                print((os.path.join(self.selProjScnShotTaskWIPPath, item.text())))
                nuke.scriptOpen(os.path.join(self.selProjScnShotTaskWIPPath, item.text()))
                self.activateCurrentTab()

        elif in_houdini:
            hou.hipFile.load(os.path.join(self.selProjScnShotTaskWIPPath, self.listFile[-1]))


    def listWidget_shotTask_action(self, item):
        print('my listWidget_shotTask_action')

        print(self.selProjScnShotTaskPath)
        print(item.text())
        print(self.subDict[self.selProjWipCode])

        self.selProjScnShotTaskWIPPath = os.path.join(self.selProjScnShotTaskPath, item.text(), self.subDict[self.selProjWipCode])
        print(self.selProjScnShotTaskWIPPath)

        self.locationPath = os.path.join(self.selProjScnShotTaskPath, item.text())
        print(self.locationPath)
        self.lineEdit_Location.setText(self.locationPath)
        print(os.listdir(os.path.join(self.locationPath, self.subDict[self.selProjWipCode])))
        self.selTask = item.text()
        #return item

    def myAction1(self):
        print("my myAction1")

    def myAction2(self):
        print('my myAction2')
        subprocess.Popen([r'C:/Program Files/7-Zip/7zFM.exe'])

    def myAction3(self):
        print('my myAction3')
        #"C:/Program Files/Blender Foundation/Blender 2.81/blender.exe" "C:/Users/poonb/Documents/twoCube.blend" Suppose this works in cmd prompt, but not work in python.
        #So need to create a .bat and launch it.
        fullpath = r'I:/iCloud~com~omz-software~Pythonista3/learnpyqt/bookSample/2_Designing with Qt Creator/test/pyBlender.bat'
        #fullpath = ''
        print(fullpath)
        subprocess.Popen([fullpath])

    def myAction4(self):
        print('my myAction4')
        self.childUi.show()

    def myAction5(self):
        print('my myAction5')
        os.startfile(self.locationPath)

    def openCurrentOpeningLocationPath(self):
        print('my openCurrentOpeningLocationPath')
        #os.startfile(self.currentOpeningLocationPath)
        os.startfile(self.lineEdit_Location_2.text())

    def listBigKeeperProject(self):
        print('my listBigKeeperProject')

        #this def is to read infomation from bigKeeperMel xml file
        f = open(r'N:/bpPipeline/maya/plugins/BigKeeper/bigKeeper_projectDatabase/bigPicture_projects.xml', "r")
        startLineNo = 1
        xmlStr = str()
        for x in f:
            if startLineNo > 1:
                xmlStr += x
            startLineNo += 1
        xmlRoot = ET.fromstring(xmlStr)


        ''' # EXAMPLE for CODING : Then the xml detail is stored as a nested Dictionary structure, for example:
            self.dictProj{
                'BigPicture_TestProj':
                    {'name': 'BigPicture_TestProj', 'path': 'N:/mnt/job/17901BigPicture_TestProj/WorkingFile/BigPicture_TestProj/', 'libraryfolder': 'lib', 'scenesfolder': 'scenes', 'workshopname': 'wip', 'mastername': 'published'},
                'BigPicture18_TestProj':
                    {'name': 'BigPicture18_TestProj', 'path': 'N:/mnt/job/18901BigPicture_TestProj/WorkingFile/BigPicture18_TestProj/', 'libraryfolder': 'lib', 'scenesfolder': 'scenes', 'workshopname': 'wip', 'mastername': 'published'},
                'PoonFilm':
                    {'name': 'PoonFilm', 'path': 'N:/mnt/job/18035PoonFilm/WorkingFile/PoonFilm/', 'libraryfolder': 'lib', 'scenesfolder': 'scenes', 'workshopname': 'wip', 'mastername': 'published'},
                'WOF':
                    {'name': 'WOF', 'path': 'N:/mnt/job/18012WOF/WorkingFile/WOF/', 'libraryfolder': 'lib', 'scenesfolder': 'scenes', 'workshopname': 'wip', 'mastername': 'published'}
                }'''
        self.dictProj = {}
        for i in xmlRoot.findall("project"):
            if os.path.exists(i.find('path').text): # To filter out those Proj Folder not on N Drive
                j = i.find('name').text
                k = i.find('path').text
                l = i.find('libraryfolder').text
                m = i.find('scenesfolder').text
                n = i.find('workshopname').text
                o = i.find('mastername').text
                print(j)
                dictDetail = {}
                dictDetail.update({"name" :j})
                dictDetail.update({"path":k})
                dictDetail.update({"libraryfolder" : l })
                dictDetail.update({"scenesfolder" : m})
                dictDetail.update({"workshopname" : n})
                dictDetail.update({"mastername" : o})
                self.dictProj.update({j : dictDetail})
                print(self.dictProj[j])


        print(self.dictProj)
        listdictProjKey = []
        for i in self.dictProj:
            listdictProjKey.append(i)
        print(listdictProjKey)
        print(type(listdictProjKey))

        return listdictProjKey


    def versionUpSaveWIP(self):
        print('my versionUpSaveWIP')
        if in_nuke:
            bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
            thisWipVer = bigKInfo.currentThisWipVerNum()
            print(thisWipVer)
            nukescripts.script.script_version_up()

            bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
            print(bigKInfo.currentThisWipVerNum())
            if thisWipVer != bigKInfo.currentThisWipVerNum():
                print('another WIP ver.')
                self.nukeUpdateMetadataNodeFps()
                self.nukeUpdateWriteNodeVer()
                nuke.scriptSave()

                nukeEnv = nuke.env
                isAssist = nukeEnv['assist']

                if isAssist:
                    theMessage = 'Be Careful !\nBe Careful !!\nBe Careful !!!\n' + 'Currently in < Nuke Assist >.\n\n' + 'Only <Nuke Script WIP version _v#### > and <fps metadata> are updated.\n\nNone of <Write Nodes> are updated. Therefore :\n\n'+ '     1) Do not render this nuke script verion.\n' + '     2) Before submit render, you must <Version Up> in Nuke or NukeX to align the write node version number.'
                    QMessageBox.information(self, 'WARNING !!! ', theMessage)
                else:
                    theMessage = 'WIP version up, Done.\n\nbigK_Write nodes --- version numbers aligned.\nbigK_ModifyMetadata nodes --- fps metadata aligned to Project Setting.'
                    QMessageBox.information(self, 'version up33 ', theMessage)


        elif in_houdini:
            hou.hipFile.saveAndIncrementFileName()
            hou.ui.displayMessage('Done.', buttons=('OK',), default_choice=0, close_choice=0)


    def myDialogShow2(self, inTitle = 'inTitle', inMessage = 'inMessage'):
        print('my myDialogShow2')

        self.dialogUi.setWindowTitle(inTitle)
        self.dialogUi.label.setText(inMessage)

        self.dialogUi.show()

    def initializeNewWIPDialogWindow(self):
        print('my initializeNewWIPDialogWindow')
        self.dialogUi.setWindowTitle('my inTitle')
        self.dialogUi.label.setText('my inMessage')
        self.dialogUi.label.setWordWrap(True)
        self.dialogUi.pushButton_new.setText('NEW Wip')
        self.dialogUi.pushButton_current.setText('Use Currently Open Wip')
        self.dialogUi.pushButton_current.setVisible(True)
        self.dialogUi.pushButton_cancel.setText('cancel')

        self.dialogUi.pushButton_new.clicked.connect(self.createNewWIP2)
        self.dialogUi.pushButton_current.clicked.connect(self.useCurrentWIP)

        self.dialogUi.pushButton_cancel.clicked.connect(self.dialogUi.close)

    def prerendKeywordShow(self):
        print('my prerendKeywordShow')

        getBigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
        print(getBigKInfo.currentProjWorkPath())

        self.prerendKeywordUi.comboBox.clear()
        self.prerendKeywordUi.lineEdit.clear()

        with open(os.path.join(getBigKInfo.currentProjWorkPath(), 'compPrerendPreset.txt')) as file:
            contents = file.readlines()
        print(contents)

        keywords = [""]

        for i in contents:
            keywords.append(i.replace('\n', ""))

        print(keywords)

        self.prerendKeywordUi.label.setText('Input a sub-name for sub-folderName and sub-framename :')
        self.prerendKeywordUi.comboBox.addItems(keywords)

        self.prerendKeywordUi.show()

    def initializePrerendKeywordUi(self):
        print('my initializePrerendKeywordUi')

        self.prerendKeywordUi.setWindowTitle('Prerend Keyword')

        self.prerendKeywordUi.pushButton_2.setText('OK')
        self.prerendKeywordUi.pushButton_3.setText('Cancel')
        self.prerendKeywordUi.pushButton_2.clicked.connect(lambda : self.prerendOKButtonAction(self.prerendKeywordUi.lineEdit.text()))
        #self.prerendKeywordUi.pushButton_2.clicked.connect(lambda : self.nukeBornWriteNode('Prerend', self.prerendKeywordUi.lineEdit.text()))
        #self.prerendKeywordUi.pushButton_2.clicked.connect(lambda : self.prerendKeywordUi.close())
        self.prerendKeywordUi.pushButton_3.clicked.connect(lambda : self.prerendKeywordUi.close())
        self.prerendKeywordUi.comboBox.activated[str].connect(self.prerendKeywordAction)


    def prerendKeywordAction(self, item):
        print('my prerendKeywordAction')
        print(item)

        self.prerendKeywordUi.lineEdit.setText(item)
        keywordLength = len(self.prerendKeywordUi.lineEdit.text())
        print(len(self.prerendKeywordUi.lineEdit.text()))
        self.prerendKeywordUi.lineEdit.setFocus()
        self.prerendKeywordUi.lineEdit.setCursorPosition(int(keywordLength))

        #self.prerendKeywordUi.lineEdit.setCursorPosition(100)


    def prerendOKButtonAction(self, item):
        print('my prerendOKButtonAction')
        print(item)

        if item != "":
            self.nukeBornWriteNode('Prerend', item)
            self.prerendKeywordUi.close()
        else:
            print('empty is not accepted')
            self.prerendKeywordUi.lineEdit.setFocus()









    def createNewWIP2(self):
        print ('my createNewWIP2')

        self.selProjScnShotTaskWIPPath = os.path.join(self.selProjScnShotTaskPath, self.selTask, self.subDict[self.selProjWipCode])
        print(self.selProjScnShotTaskWIPPath)


        newWipName = (self.selShot + "_" + self.selTask + "_" + self.subDict[self.selProjWipCode] + "_v0000" + wipExtension)
        print(newWipName)

        if nuke.Root().modified() == True:
            print('current changes have not yet been saved!')
            nuke.scriptClose() ### pop a dialog instead of close.
            if nuke.Root().modified() == False:

                thepath = os.path.join(self.selProjScnShotTaskWIPPath, newWipName)
                f = open(thepath, 'w')
                f.close()

                self.dialogUi.close()
                self.openLastestWIP()
        else:
            thepath = os.path.join(self.selProjScnShotTaskWIPPath, newWipName)
            f = open(thepath, 'w')
            f.close()

            self.dialogUi.close()
            self.openLastestWIP()
            self.updateCurrentOpeningLocationPath()

        sys.path.append(r'N:\bpPipeline\bigKeeperPy\py\externalPyModule\compTeamNukePy')
        import projectRoot_published
        projectRoot_published.projectSetting()
        nuke.scriptSave()
        os.remove(os.path.join(self.selProjScnShotTaskWIPPath, newWipName+'~'))
        sys.path.remove(r'N:\bpPipeline\bigKeeperPy\py\externalPyModule\compTeamNukePy')



    def useCurrentWIP(self):
        print('my useCurrentWIP')

        if nuke.Root().modified() == True:
            print('current changes have not yet been saved!')
            nuke.scriptClose() ### pop a dialog instead of close.
            if nuke.Root().modified() == False:

                self.selProjScnShotTaskWIPPath = os.path.join(self.selProjScnShotTaskPath, self.selTask, self.subDict[self.selProjWipCode])
                print(self.selProjScnShotTaskWIPPath)


                newWipName = (self.selShot + "_" + self.selTask + "_" + self.subDict[self.selProjWipCode] + "_v0000" + wipExtension)
                print(newWipName)
                saveName = os.path.join(self.selProjScnShotTaskWIPPath,newWipName)
                print(saveName)
                nuke.scriptSaveAs(saveName)

                print(nuke.root()['name'].value())
                print(os.path.dirname( nuke.root().name() ))
                self.dialogUi.close()
        else:
            self.selProjScnShotTaskWIPPath = os.path.join(self.selProjScnShotTaskPath, self.selTask, self.subDict[self.selProjWipCode])
            print(self.selProjScnShotTaskWIPPath)


            newWipName = (self.selShot + "_" + self.selTask + "_" + self.subDict[self.selProjWipCode] + "_v0000" + wipExtension)
            print(newWipName)
            saveName = os.path.join(self.selProjScnShotTaskWIPPath,newWipName)
            print(saveName)
            nuke.scriptSaveAs(saveName)

            print(nuke.root()['name'].value())
            print(os.path.dirname( nuke.root().name() ))
            self.dialogUi.close()

            self.updateCurrentOpeningLocationPath()

    def pretendCloseNukeScript(self):
        print('my pretendCloseNukeScript')

        nuke.scriptClear()

        '''
        # script before knowing there is a nuke.scriptClear()
        nuke.scriptClose()

        thepath = os.path.join(os.environ['LOCALAPPDATA'], 'bigKeeperPy', 'tmpNukeScript.nk')
        f = open(thepath, 'w')
        f.close()

        nuke.scriptOpen(os.path.join(os.environ['LOCALAPPDATA'], 'bigKeeperPy', 'tmpNukeScript.nk'))
        '''

    def checkCurrentUnsaveStatus(self):
        print('my checkCurrentUnsaveStatus')
        if in_nuke:
            if nuke.Root().modified() == True:
                print('current changes have not yet been saved!')
                nuke.scriptClose() ### pop a dialog instead of close.
                if nuke.Root().modified() == False:
                    nuke.scriptOpen(os.path.join(self.selProjScnShotTaskWIPPath, self.listFile[-1]))

            else:

                nuke.scriptClose()
                nuke.scriptOpen(os.path.join(self.selProjScnShotTaskWIPPath, self.listFile[-1]))
                #window.close()

    def updateCurrentOpeningLocationPath(self):
        print('my updateCurrentOpeningLocationPath')

        if in_nuke:
            self.currentOpeningLocationPath = os.path.dirname(nuke.root().name())
        elif in_houdini:
            self.currentOpeningLocationPath = os.path.dirname(hou.hipFile.path())
        elif in_maya:
            self.currentOpeningLocationPath = os.path.dirname(cmds.file(q=True, sn=True))
        elif in_python:
            self.currentOpeningLocationPath = os.path.dirname(os.getcwd())
        elif in_blender:
            self.currentOpeningLocationPath = os.path.dirname(bpy.data.filepath)


        if self.currentOpeningLocationPath == '':
            self.currentOpeningLocationPath = '-NONE-'
        print(self.currentOpeningLocationPath)
        self.lineEdit_Location_2.setText(self.currentOpeningLocationPath)

    def createShotNewTask(self):
        print('my createShotNewTask')
        folderList = ['cache', 'daily/yyyymmdd', 'notes', 'preview', self.subDict[self.selProjPublishCode], 'research', 'textures/PSD', 'version', self.subDict[self.selProjWipCode]]
        taskName = str(input('Please input New Task Name :'))
        for folder in folderList:
            print(os.path.join(self.selProjScnShotTaskPath, taskName, folder))
            os.makedirs(os.path.join(self.selProjScnShotTaskPath, taskName, folder))
        self.listWidget_3.addItem(str(taskName))

    '''def compareCurrentFrameInfo(self):
        bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()

        if in_nuke:
            if (nuke.Root().knob('first_frame').value() != float(bigKInfo.currentShotFrameIn())) or (nuke.Root().knob('last_frame').value() != float(bigKInfo.currentShotFrameOut())) or (nuke.Root().knob('fps').value() != float(bigKInfo.currentShotFrameFps())):
                self.pushButton_getFrameRange.setStyleSheet("background-color:rgb(250,5,5); color:rgb(10, 10, 10)")
            else:
                self.pushButton_getFrameRange.setStyleSheet("background-color:rgb(128,179,179); color:rgb(10, 10, 10)")'''

    def getCurrentFrameInfo(self):
        print('my getCurrentFrameInfo')
        bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()

        if in_nuke:
            nuke.Root().knob('first_frame').setValue(float(bigKInfo.currentShotFrameIn()))
            nuke.Root().knob('last_frame').setValue(float(bigKInfo.currentShotFrameOut()))
            nuke.Root().knob('fps').setValue(float(bigKInfo.currentShotFrameFps()))
            self.nukeUpdateMetadataNodeFps()

            print(nuke.Root().knob('first_frame').value())
            print(nuke.Root().knob('last_frame').value())
            print(nuke.Root().knob('fps').value())

            #nuke.message('Done.')
            QMessageBox.information(self, 'message', "Done.\nAll fps in output <Metadata Node> aligned to Project Setting.")

        if in_houdini:
            getFrameIn = float(bigKInfo.currentShotFrameIn())
            getFrameOut = float(bigKInfo.currentShotFrameOut())
            getFps = float(bigKInfo.currentShotFrameFps())


            # Assign Frame Start and Frame End in Global Animation Options
            hou.hscript("tset " + str((getFrameIn-1)/getFps) + " " + str((getFrameOut)/getFps))
            hou.playbar.setPlaybackRange(getFrameIn,getFrameOut)
            hou.setFrame(getFrameIn)
            hou.setFps(getFps)

            #print(" The *** Frame Start *** is assigned to " + str(getFrameIn))
            #print(" The *** Frame End *** is assigned to " + str(getFrameOut))
            # For this section, I cannot find any suitable python function to set Global Animation Options : Start frame and End frame
            # The above is just copy from internet source : https://forums.odforce.net/topic/16709-how-can-i-set-the-playback-range/
            # Don't really how to set the frame range by the line <hou.hscript> & the line <hou.playbar.setPlaybackRange>.
            # please teach me what the follow means, if you know about it.
            # by Benson

            hou.ui.displayMessage('Done.', buttons=('OK',), default_choice=0, close_choice=0)

    def nukeTempTool1(self):
        print('nukeTempTool1')
        self.nukeTempUi.LoadInOutFrame()
        self.nukeTempUi.show()

        #bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
        #self.nukeTempUi.initializeNukeTempWindow()

    def createShotNewTask_appear(self):
        print('my createShotNewTask_appear')
        if self.listWidget_2.currentRow() > -1:
            self.createShotNewTaskUi.show()
        else:
            #buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            # QMessageBox ref: https://pythonspot.com/pyqt5-messagebox/
            QMessageBox.information(self, 'message', "no shot is selected.")
            '''if buttonReply == QMessageBox.Yes:
                print('Yes clicked.')
            else:
                print('No clicked.')'''




    def createShotNewTaskAction(self):
        print('my createShotNewTaskAction')
        print(self.createShotNewTaskUi.lineEdit.text())
        folderList = ['cache', 'daily/yyyymmdd', 'notes', 'preview', self.subDict[self.selProjPublishCode], 'research', 'textures/PSD', 'version', self.subDict[self.selProjWipCode]]
        taskName = self.createShotNewTaskUi.lineEdit.text()
        for folder in folderList:
            print(os.path.join(self.selProjScnShotTaskPath, taskName, folder))
            os.makedirs(os.path.join(self.selProjScnShotTaskPath, taskName, folder))
        self.listWidget_3.addItem(str(taskName))
        self.createShotNewTaskUi.close()

    def createShotNewTaskClose(self):
        print('my createShotNewTaskClose')
        self.createShotNewTaskUi.close()

    def tempchecklist2selected(self):
        print('my tempchecklist2selected')
        status = self.listWidget_2.currentRow()
        print(status)

    def compLatestRvAction(self):
        print('my compLatestRvAction')
        print(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output'))
        thePath = os.path.join(self.selProjScnShotTaskPath, 'comp', 'output')
        if self.listWidget_2.currentRow() > -1:
            try:
                folderList = os.listdir(thePath)
            except:
                QMessageBox.information(self, 'message', 'Standard "Comp" & "Output" folder not found.')

            print(folderList)
            listSeq = []
            for i in folderList:
                if (len(i) <= 5) and (i[0] == 'v') and i[1::].isnumeric():
                    print(i)
                    print(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', i))
                    if os.path.isdir(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', i)):
                        listSeq.append(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', i))
            listSeq.sort()
            print(listSeq)
            if len(listSeq) > 0:
                print(listSeq[-1])
                subprocess.Popen([rvPath, listSeq[-1]])
            else:
                QMessageBox.information(self, 'message', r'No folder in ...\comp\output')
        else:
            QMessageBox.information(self, 'message', "no shot is selected.")

    def shotAction1Action(self):
        print('my shotAction1Action')
        if self.listWidget_3.currentRow() > -1:
            print(self.selTask)
            self.listWidget_3C_action(self.selTask)
        else:
            QMessageBox.information(self, 'message', "no task is selected.")

    def shotAction2Action(self):
        print('my shotAction2Action')
        self.compLatestRvAction()

    def shotAction4Action(self):
        print('my shotAction4Action')
        self.compPreviousVerUi.listWidget.clear()

        if self.listWidget_2.currentRow() > -1:

            #listDir = ['v00010', 'v00020']

            # Asked Lik decided only 'comp' task use this general RV preview. Therefore hardcode 'comp' & ' output' for now.
            print(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output'))
            thePath = os.path.join(self.selProjScnShotTaskPath, 'comp', 'output')
            listDir = os.listdir(thePath)
            folderOnlyList = []
            for i in listDir:
                print(i)
                print(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', i))
                if os.path.isdir(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', i)):
                    folderOnlyList.append(i)
            folderOnlyList.sort(reverse=True)



            #self.childUi.show()
            self.compPreviousVerUi.listWidget.addItems(folderOnlyList)
            #self.wrongFormatUi.listWidget.itemDoubleClicked.connect(self.listWidget_A_action)
            #self.compPreviousVerUi.listWidget.itemDoubleClicked.connect(self.speak)

            #self.compPreviousVerUi.listWidget.itemDoubleClicked.connect(self.shotAction3Action)

            self.compPreviousVerUi.show()
        else:
            QMessageBox.information(self, 'message', "no shot is selected.")

        return folderOnlyList[2]


    def shotAction3Action(self, *inItem):
        print('my shotAction3Action')

        if len(inItem) == 0:
            chosenVer = None
        else:
            chosenVer = inItem[0].text()

        print('chosenVer: ')
        print(chosenVer)


        def isExrFormat(inPath):
            # This function is to limit only activate for EXR format. Due to current ability that other format seems have color issue when create RV session by text pad hacking. Should tackle later.
            print('my checkExrOnly')
            allFiles = os.listdir(inPath)

            '''
            check1stFrame = allFiles[0].split('.')
            if check1stFrame[-1] == 'exr' or check1stFrame[-1] == 'EXR':
                exrFormat = True
            else:
                exrFormat = False
            '''

            for i in allFiles:
                if i.split('.')[-1] == 'exr' or i.split('.')[-1] == 'EXR':
                    print(i)
                    exrFormat = True
                    print(exrFormat)
                elif i.split('.')[-1] == 'png' or i.split('.')[-1] == 'PNG':
                    print(i)
                    exrFormat = True
                    print(exrFormat)

                elif i.split('.')[-1] == 'tmp' or i.split('.')[-1] == 'TMP':
                    print(i)
                    print('pass')
                    pass
                else:
                    print(i)
                    exrFormat = False
                    print(exrFormat)
                    break

            return exrFormat

        print(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output'))
        thePath = os.path.join(self.selProjScnShotTaskPath, 'comp', 'output')
        if self.listWidget_2.currentRow() > -1:
            try:
                folderList = os.listdir(thePath)
            except:
                QMessageBox.information(self, 'message', 'Standard "Comp" & "Output" folder not found.')

            print(folderList)

            if chosenVer == None:
                listSeq = []
                for i in folderList:
                    print('i : ')
                    print(i)
                    if (len(i) <= 5) and (i[0] == 'v') and i[1::].isnumeric():
                        print(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', i))
                        if os.path.isdir(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', i)):
                            listSeq.append(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', i))
                            latestVersion = i
                listSeq.sort()
                print(listSeq)
                print(latestVersion)
                LatestVerPath = listSeq[-1]
                verType = 'CompMaster'
            else:
                latestVersion = chosenVer
                LatestVerPath = os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', latestVersion)
                print('chosenVer !=, print(LatestVerPath) :')
                print(LatestVerPath)
                listSeq = [LatestVerPath]

                if (len(latestVersion) <= 5) and (latestVersion[0] == 'v') and latestVersion[1::].isnumeric():
                    verType = 'CompMaster'
                else:
                    verType = 'LayerMask'

                print(verType)

            if len(listSeq) > 0:


                SameRvVersionPath = (os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', latestVersion + '.rv'))
                haveSameRvVersion = os.path.isfile(SameRvVersionPath)

                if haveSameRvVersion:
                    subprocess.Popen([rvPath, SameRvVersionPath])

                else:
                    if verType == 'CompMaster':
                        if isExrFormat(LatestVerPath):
                            self.createRvFile(LatestVerPath, latestVersion)
                            subprocess.Popen([rvPath, SameRvVersionPath])

                        else:
                            QMessageBox.information(self, 'message', r'Make Sure all frame are .exr format.')
                    elif verType == 'LayerMask':
                        os.startfile(LatestVerPath)


            else:
                QMessageBox.information(self, 'message', r'No folder in ...\comp\output')
        else:
            QMessageBox.information(self, 'message', "no shot is selected.")

    def createRvFile(self, inLatestVerPath, inLatestVer):

        print('my createRvFile')
        print(inLatestVerPath)
        print(inLatestVer)

        def getMetaData():
            print('my getMetaData')

            import subprocess, os

            def getFrames(inPath):
                print('my getFrames')
                allFiles = os.listdir(inPath)
                print(inPath)
                onlyFiles = []
                print(allFiles)
                for i in allFiles:
                    if os.path.isfile(os.path.join(inPath, i)):
                        onlyFiles.append(i)
                onlyFiles.sort()

                return onlyFiles

            theFrameList = getFrames(inLatestVerPath)
            print('theFrameList : {}'.format(theFrameList))

            # to avoid first frame is .tmp which will fail to read meta data
            for frame in theFrameList:
                if frame.split('.')[-1] == 'tmp' or frame.split('.')[-1] == 'TMP':
                    theFrameList.remove(frame)

            print('theFrameList after del tmp check: {}'.format(theFrameList))

            FrameStartFullName = theFrameList[0].split('.')
            FrameEndFullName = theFrameList[-1].split('.')

            FrameFrontName = FrameStartFullName[0]
            FrameFirstFrameNo = FrameStartFullName[1]
            FrameEndFrameNo = FrameEndFullName[1]
            FrameExtension = FrameStartFullName[2]

            startFrameDigit = (len(FrameFirstFrameNo))
            startFrameDigitNoZero = (len(str(int(FrameFirstFrameNo))))
            endFrameDigit = (len(FrameEndFrameNo))
            endFrameDigitNoZero = (len(str(int(FrameEndFrameNo))))

            # Pattern 1 : name.0000001.exr to name.0010030.exr --> @@@@@@@
            # Pattern 2 : name.1.exr to name.0010030.exr --> @
            # Pattern 3 : name.998.exr to name.2001.exr -- > @@@
            # Pattern 4 : name.001001.exr to name.002001.exr --> @@@@@@
            # Pattern 5 : name.0998.exr to name.2001.exr --> #
            # Pattern 6 : name.1001.exr to name.2001.exr --> #

            if (startFrameDigit == endFrameDigit) and ((endFrameDigit - endFrameDigitNoZero) == 0):
                symbol = '#'
            else:
                symbol = '@'* startFrameDigit


            # carl.1001-1010@@@@@.exr
            rvStringName = (FrameFrontName + '.' + str(int(FrameFirstFrameNo)) + '-' + str(int(FrameEndFrameNo)) + symbol + '.' + FrameExtension)
            print('rvStringName : ' + rvStringName)


            #externalToolPath = r'N:\BigKeeper\py\externalTool'
            input_file = os.path.normpath((os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', inLatestVer, theFrameList[0])))
            print(input_file)



            exec_command = os.path.normpath(os.path.join(externalToolPath, r'exiftool.exe'))
            print(exec_command)
            #exec_command = r'N:\BigKeeper\py\externalTool\exiftool.exe'
            #input_file = r'N:\mnt\job\18012WOF\WorkingFile\WOF\scenes\hologramSeq\ac0343\components\comp\output\v0015\ac0343.1001.exr'
            arg1 = r'-all'
            arg2 = r'-ImageWidth'
            arg3 = r'-ImageHeight'
            arg4 = r'-Bigkframepersecond'
            arg0 = r'-s2' # s1--tag names instead of descriptions   s2--no extra spaces    s3--values only

            print('before run')
            process = subprocess.Popen([exec_command, input_file, arg1, arg0], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)
            print('after run')

            # store data in dict way
            infoDict = {}
            #print(process.stdout.read())
            for i in process.stdout:
                line = i.strip().split(':')     #splite Tag as line[0], value as line[1]. (line is <list> type)
                infoDict[line[0].strip()] = line[1].strip()     # line[0] as dict's key, line[1] as value.

            print('infoDict:')
            print(infoDict)

            metaData = []

            try:
                metaData.append(int(infoDict['ImageWidth']))
            except:
                metaData.append(320) #make a dramatic wrong, user will be alerted. Will develop to pop up dialog for user input.

            try:
                metaData.append(int(infoDict['ImageHeight']))
            except:
                metaData.append(240) #make a dramatic wrong, user will be alerted. Will develop to pop up dialog for user input.

            try:
                metaData.append(round(float(infoDict['Bigkframepersecond']), 3))
            except:
                metaData.append(3.000) # make a dramatic wrong, user will be alerted. Will develop to pop up dialog for user input.

            metaData.append(rvStringName)
            metaData.append(FrameFirstFrameNo)
            metaData.append(FrameEndFrameNo)

            return metaData

        def askFolderName():
            print('my askFolderName')
            try:
                defaultText = self.storedAnsweredFolder
            except:
                defaultText = ""
            answerFolder = QInputDialog.getText(self, 'Input Folder Name', 'To create instance-shortcut for comment folder,\nformat: <yyyymmdd>\n\nor\n\nPress cancel to skip.',QLineEdit.Normal, defaultText)
            print(answerFolder)

            return answerFolder

        def createShortCut(folderName, inShotName, iniRvVersion, inRvFullPathName):
            print(self.subDict[self.selProjPath])

            targetShortCutPath = os.path.normpath(os.path.join(self.subDict[self.selProjPath], 'comment', folderName))
            print(targetShortCutPath)
            if not os.path.isdir(targetShortCutPath):
                os.makedirs(targetShortCutPath)

            exec_command = os.path.normpath(os.path.join(externalToolPath, 'shortCut', 'Shortcut.exe'))
            #argument_command = ' ' + r'/f:"' + r'D:\toliet\Shortcut\myBNOpic8.lnk' + r'" ' +  r'/a:c ' + r'/t:"' + r'D:\toliet\Shortcut\IMG_1459_BNO_N_U.jpg' + '"'
            linkName = os.path.normpath(os.path.join(targetShortCutPath, str(inShotName + '_' + iniRvVersion))) + r'__shortcut' + r'.lnk'
            sourceName = os.path.normpath(inRvFullPathName)
            argument_command = ' ' + r'/f:"' + linkName + r'" ' +  r'/a:c ' + r'/t:"' + sourceName + '"'
            # sample: Shortcut.exe /f:"D:\toliet\Shortcut\myBNOpic2.lnk" /a:c /t:"D:\toliet\Shortcut\IMG_1459_BNO_N_U.jpg"
            #cmd = exec_command + " " + r'/f:"D:\toliet\Shortcut\myBNOpic6.lnk" /a:c /t:"D:\toliet\Shortcut\IMG_1459_BNO_N_U.jpg"'
            cmd = exec_command + argument_command
            print('exec_command :' + exec_command)
            print('cmd :' + cmd)

            #subprocess.Popen([exec_command, linkName, actionMode, sourceName])
            os.system(cmd)




        # rvTemplate = r'N:\mnt\job\19901BigPicture_TestProj\_bigkeeperPyData\rv.template'
        theFile = os.path.join(self.selProjScnShotTaskPath, 'comp', 'output')

        with open(rvTemplate) as f:
            data = f.readlines()

        print('***************************************')

        MetaData = getMetaData()
        inWidth = MetaData[0]
        inHeight = MetaData[1]
        inFps = MetaData[2]
        inRvStringName = MetaData[3]
        RvStringMovie = (str(inLatestVerPath + '/' + inRvStringName).replace("\\", "/"))
        inFrameFirstFrameNo = MetaData[4]
        inFrameEndFrameNo = MetaData[5]
        rvTimeLineStart = 1
        rvTimeLineEnd = int(inFrameEndFrameNo) - int(inFrameFirstFrameNo) + 1 + rvTimeLineStart

        lineForWidthHeight = [80, 286, 601]
        lineForFps = [19, 79, 223, 255, 287, 581, 600]
        lineForPathStringMovie = [574]
        lineForStringName = [370]
        lineForStartFrame = [280, 598]
        lineForEndFrame = [281]
        lineForEndFramePlus1 = [598]
        lineForRvTimeLineStartEnd = [17, 18, 279]

        print(inRvStringName[0:-4:1])
        print(RvStringMovie)

        #string movie = "N:/mnt/job/18006Chery/WorkingFile/Chery/scenes/turnTable/ttb0030/components/comp/output/v0015/ttb0030.1-10030@@@@@@@.tga"
        for line in lineForWidthHeight:
            data[line-1] = data[line-1].replace('__<bigkeeperPy_Width>__', str(inWidth))
            data[line-1] = data[line-1].replace('__<bigkeeperPy_Height>__', str(inHeight))

        for line in lineForFps:
            data[line-1] = data[line-1].replace('__<bigkeeperPy_fps>__', str(inFps))

        for line in lineForPathStringMovie:
            data[line-1] = data[line-1].replace('__<bigkeeperPy_stringMovie>__', str(RvStringMovie))

        for line in lineForStringName:
            data[line-1] = data[line-1].replace('__<bigkeeperPy_stringName>__', str(inRvStringName[0:-4:1]))

        for line in lineForStartFrame:
            data[line-1] = data[line-1].replace('__<frameNoStart>__', str(int(inFrameFirstFrameNo)))

        for line in lineForEndFrame:
            data[line-1] = data[line-1].replace('__<frameNoEnd>__', str(int(inFrameEndFrameNo)))

        for line in lineForEndFramePlus1:
            data[line-1] = data[line-1].replace('__<frameNoEndPlus1>__', str(int(inFrameEndFrameNo)+1))

        for line in lineForRvTimeLineStartEnd:
            data[line-1] = data[line-1].replace('__<rvTimelineStart>__', str(rvTimeLineStart))
            data[line-1] = data[line-1].replace('__<rvTimelineEnd>__', str(rvTimeLineEnd))

        writePath = str(os.path.join(self.selProjScnShotTaskPath, 'comp', 'output', inLatestVer + '.rv')).replace("\\", "/")
        #writePath = writePath.replace("\\", "/")
        print('writePath is :' + writePath)
        with open(writePath, 'w') as f:
            f.writelines(data)

        receivedAnswerFolder = askFolderName()
        if receivedAnswerFolder[1]:
            self.storedAnsweredFolder = receivedAnswerFolder[0]
            createShortCut(self.storedAnsweredFolder, self.selShot, inLatestVer, writePath)

    def findNodeLargestNumber(self, InPrefix, InNodeClassName):
        print('my findNodeLargestNumber')

        dedictatedPrefix = InPrefix
        nodeClassName = InNodeClassName


        # Gather all the nodes in the scene
        allNodes = nuke.allNodes()
        sameNodeNameList = []

        # sort out only (bigK + targetClassName)nodes
        for i in allNodes:
            mergePrefix = dedictatedPrefix + '_' + nodeClassName + '_'
            if i.name()[0:len(mergePrefix)] == mergePrefix:
                sameNodeNameList.append(i.name())

        print('sameNodeNameList :')
        print(sameNodeNameList)
        if len(sameNodeNameList) > 0:
            # find out the Largest number
            seperator = '_' + nodeClassName + '_'
            print('seperator')

            allNumbers = []
            for i in sameNodeNameList:
                splitName = i.split(seperator)
                print(seperator)
                print('splitName :')
                print(splitName)
                allNumbers.append(int(splitName[-1]))
            allNumbers.sort()
            print(allNumbers)
            LargestNumber = int(allNumbers[-1])
        else:
            LargestNumber = 0

        return LargestNumber


    def nukeBornBigKNode(self, InPrefix, InNodeClassName):
        print('my nnukeBornBigKNode')

        """dedictatedPrefix = 'bigK'
        nodeClassName = 'Grade'"""
        dedictatedPrefix = InPrefix
        nodeClassName = InNodeClassName

        print('nodeClassName :')
        print(nodeClassName)
        print('dedictatedPrefix :')
        print(dedictatedPrefix)

        targetNumber = self.findNodeLargestNumber(InPrefix = dedictatedPrefix, InNodeClassName = nodeClassName)
        print('targetNumber :')
        print(targetNumber)

        NewNodeName = dedictatedPrefix + '_' + nodeClassName + '_' + str(targetNumber + 1)

        print('NewNodeName :')
        print(NewNodeName)
        #newCreatedNode = nuke.nodes.nodeClassName(name=NewNodeName)
        #newCreatedNode.setInput(1, userSelNode)
        newCreatedNode = nuke.createNode(nodeClassName)
        newCreatedNode.knob('name').setValue(NewNodeName)

        return newCreatedNode

    def nukeBornGradeNode(self):
        print('my nukeBornGradeNode')

        #newCreatedNodeMetadata = self.nukeBornBigKNode('bigK', 'ModifyMetaData')
        newCreatedNodeMetadata = self.nukeBornMetadataNode()
        newCreatedNode = self.nukeBornBigKNode('bigK', 'Grade')
        newCreatedNode.setInput(0, newCreatedNodeMetadata)

        return newCreatedNode

    def nukeCheckKnobContentUnique(self, inClass, inKnob, inContent):
        print('my nukeCheckPathUnique')

        print('inContent is :')
        print(inContent)
        allNodes = nuke.allNodes(filter=inClass)
        nodeList = []
        duplicatedNodeList = []

        for i in allNodes:
            knobValue = os.path.normpath(i.knob(inKnob).getValue())
            nodeList.append(i)
            print(inContent)
            print(knobValue)
            if inContent in knobValue:
                duplicatedNodeList.append(i.name())

        print(nodeList)
        print(duplicatedNodeList)

        if len(duplicatedNodeList) > 0:
            isUnique = False

            dupMessage = inContent + '\n\nThe above path is already existed in :\n\n' + str(duplicatedNodeList)
            QMessageBox.information(self, 'message', dupMessage)
        else:
            isUnique = True

        return isUnique

    def nukeAskSuffix(self):
        bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
        print(bigKInfo.currentCompIniSuffix())




    def nukeBornWriteNode(self, inType, *args):
        print('my nukeBornWriteNode')

        answerName = answerSuffix = readyToCreate = None

        try:
            print(args)
            print(args[0])
        except:
            args=[None]
            print('no args, assigned {} instead.'.format(args[0]))

        try:
            orignalSelNode = nuke.selectedNode()
            print('original :::')
            print(orignalSelNode)
            print(type(orignalSelNode))
        except:
            orignalSelNode = None

        numOfSelNodes = len(nuke.selectedNodes())

        if numOfSelNodes > 1:
            QMessageBox.information(self, 'message', 'Please only select 1 node as anchor OR as input node.')

        elif numOfSelNodes < 1 :
            QMessageBox.information(self, 'message', 'No node is selected.\n\nPlease create a "DOT" node as an anchor.')

        else:
            if len(orignalSelNode.dependent()) > 1:
                errorMessage = 'The output of the selected node :\n     ' + str(orignalSelNode.name()) + "\nis linked to other node.\n\nTo avoid Node Graph chaos :\n1) Create a seperate DOT node as an Anchor.\n2) Select the Anchor to generate again.\n3) After the nodes are generated, re-connect manually, if needed."
                QMessageBox.information(self, 'message', errorMessage)
            else:
                bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
                if inType == 'CompMaster':
                    print(inType)

                    answerSuffix, readyToCreate = QInputDialog.getText(self, 'Suffix', 'Suffix : (empty if not needed.)', QLineEdit.Normal, bigKInfo.currentCompIniSuffix())
                    frameName = str(bigKInfo.currentShot()) + answerSuffix + '.%04d' + '.exr'
                    verFolder = 'v' + str(bigKInfo.currentThisWipVerNum()).zfill(4)
                    targetFilePath = os.path.normpath(os.path.join(str(bigKInfo.currentTaskPath()), 'output', verFolder, frameName))
                    checkPath      = os.path.normpath(os.path.join(str(bigKInfo.currentTaskPath()), 'output', verFolder))
                    #readyToCreate = True
                    backdropLabel = inType


                elif inType == 'CompMasterToV':
                    print(inType)

                    answerSuffix, readyToCreate = QInputDialog.getText(self, 'Suffix', 'Suffix : (empty if not needed.)', QLineEdit.Normal, bigKInfo.currentCompIniSuffix())
                    frameName = str(bigKInfo.currentShot()) + answerSuffix + '.%04d' + '.exr'
                    vDriveFolder = self.vDrivePathRead(os.path.join(bigKInfo.currentProjWorkPath(), 'bigPathsProject.ini'), 'BIGPATHS', 'vOutput')
                    outputVdriveFolder = os.path.join(vDriveFolder, bigKInfo.currentShot())

                    targetFilePath = os.path.normpath(os.path.join(outputVdriveFolder, frameName))
                    checkPath      = outputVdriveFolder
                    #readyToCreate = True
                    backdropLabel = inType

                elif inType == 'LayerMask':
                    print(inType)
                    answerName, readyToCreate = QInputDialog.getText(self, 'sub-name', 'Input a sub-name for sub-folderName and sub-framename', QLineEdit.Normal)
                    print(answerName)
                    if readyToCreate == True:
                        answerSuffix, readyToCreate = QInputDialog.getText(self, 'Suffix', 'Suffix : (empty if not needed.)', QLineEdit.Normal, bigKInfo.currentCompIniSuffix())

                    frameName = str(bigKInfo.currentShot()) + '_' + answerName + answerSuffix + '.%04d' + '.exr'
                    verFolder = 'v' + str(bigKInfo.currentThisWipVerNum()).zfill(4) + '_' + inType
                    targetFilePath = os.path.normpath(os.path.join(str(bigKInfo.currentTaskPath()), 'output', verFolder, answerName, frameName))
                    checkPath = os.path.normpath(os.path.join(str(bigKInfo.currentTaskPath()), 'output', verFolder, answerName))
                    backdropLabel = answerName + '_' + inType

                elif inType == 'PreRend':
                    # *** unknow bug, this elif section need to keep. If this section deleted, the 'Prerend' section will sytax error. To Be Fix.
                    print(inType)
                    answerName, readyToCreate = QInputDialog.getText(self, 'sub-name', 'Input a sub-name for sub-folderName and sub-framename', QLineEdit.Normal)
                    print(answerName)

                    frameName = str(bigKInfo.currentShot()) + '_' + answerName + '.%04d' + '.exr'
                    verFolder = 'v' + str(bigKInfo.currentThisWipVerNum()).zfill(4)
                    targetFilePath = os.path.normpath(os.path.join(str(bigKInfo.currentTaskPath()), 'prerend', verFolder, answerName, frameName))
                    checkPath = os.path.normpath(os.path.join(str(bigKInfo.currentTaskPath()), 'prerend', verFolder, answerName))
                    #readyToCreate = True
                    backdropLabel = answerName + '_' + inType
                    # *** unknow bug, this elif section need to keep. If this section deleted, the 'Prerend' section will sytax error. To Be Fix.

                elif inType == 'Prerend':
                    print(inType)
                    answerName = args[0]
                    readyToCreate = True

                    print('3 self.prerendKeyword is {}'.format(answerName))

                    answerSuffix, readyToCreate = QInputDialog.getText(self, 'Suffix', 'Suffix : (empty if not needed.)', QLineEdit.Normal, bigKInfo.currentCompIniSuffix())
                    frameName = str(bigKInfo.currentShot()) + '_' + answerName + answerSuffix + '.%04d' + '.exr'
                    verFolder = 'v' + str(bigKInfo.currentThisWipVerNum()).zfill(4)
                    targetFilePath = os.path.normpath(os.path.join(str(bigKInfo.currentTaskPath()), 'prerend', verFolder, answerName, frameName))
                    checkPath = os.path.normpath(os.path.join(str(bigKInfo.currentTaskPath()), 'prerend', verFolder, answerName))
                    backdropLabel = answerName + '_' + inType



                print('checkPath is : ' + checkPath)
                checkPath = str(checkPath + os.sep)
                print('checkPath is : ' + checkPath)
                isUnique = self.nukeCheckKnobContentUnique('Write', 'file', checkPath)
                if isUnique:

                    if readyToCreate :
                        #newCreatedNodeMetadata = self.nukeBornBigKNode('bigK', 'ModifyMetaData')
                        newCreatedNodeMetadata = self.nukeBornMetadataNode()
                        newCreatedNode = self.nukeBornBigKNode('bigK', 'Write')
                        newCreatedNode.setInput(0, newCreatedNodeMetadata)
                        newCreatedNode.knob('channels').setValue('rgba')

                        #targetFilePath = os.path.join(str(bigKInfo.currentTaskPath()), 'output', str(bigKInfo.currentThisWipVerNum(), (str(bigKInfo.currentShot()) + '.%04d' + '.exr')))
                        targetFilePath = targetFilePath.replace(os.sep, '/')
                        newCreatedNode.knob('file').setValue(targetFilePath)
                        newCreatedNode.knob('create_directories').setValue(True)
                        newCreatedNode.knob('metadata').setValue('all metadata')
                        newCreatedNode.knob('noprefix').setValue(True)
                    else:
                        pass

                    allNewNodes = [orignalSelNode, newCreatedNodeMetadata, newCreatedNode]
                    print(newCreatedNodeMetadata)
                    print('***')
                    print(newCreatedNode)
                    print('*************allNewNodes : ***************************')
                    print(allNewNodes)

                    for i in allNewNodes:
                        i.setSelected(True)

                    newBD = self.nukeBornBackdrop(allNewNodes, backdropLabel, inType)

                    print('original After:::')
                else:
                    print('Not Unique Path.')

                # setSelected to let user move the position of the created nodes
                for i in allNewNodes:
                    i.setSelected(True)
                newBD.setSelected(True)

                #orignalSelNode.setSelected(False)

                return newCreatedNode


    def nukeBornBackdrop(self, inNodes, inLabelText, inTypeForColor):
        print('my nukeBornBackdrop')



        #allNode = nuke.selectedNode()
        #labelText = 'write\nLayerMask'

        allNode = inNodes
        labelText = 'write' + '\n' + inLabelText


        if inTypeForColor == 'CompMaster':
            baseColor = 2419101951
        elif inTypeForColor == 'CompMasterToV':
            baseColor = 2319101951
        elif inTypeForColor == 'LayerMask':
            baseColor = 2068476415
        elif inTypeForColor == 'PreRend':
            baseColor = 2060476415
        elif inTypeForColor == 'Prerend':
            baseColor = 2060476415

        allNode = nuke.selectedNode()
        print('nodes :' + str(len(allNode)))


        margin = 100
        yLabelSpace = 25
        rightOffSetSpace = 20
        labelFontSize = 20

        xpMax = allNode.xpos()
        xpMin = allNode.xpos()
        ypMax = allNode.ypos()
        ypMin = allNode.ypos()

        for a in nuke.selectedNodes():
            if a.xpos() > xpMax:
                xpMax = a.xpos()
            if a.xpos() < xpMin:
                xpMin = a.xpos()
            if a.ypos() > ypMax:
                ypMax = a.ypos()
            if a.ypos() < ypMin:
                ypMin = a.ypos()

        bd = nuke.nodes.BackdropNode(bdwidth=(xpMax-xpMin)+margin , bdheight=(ypMax-ypMin)+ margin + yLabelSpace )
        bd.setXpos(int(xpMin-margin/2 + rightOffSetSpace * 1.8))
        bd.setYpos(int(ypMin-margin/2 - yLabelSpace))

        bd.knob('tile_color').setValue(baseColor)
        bd.knob('label').setValue(labelText)
        bd.knob('note_font_size').setValue(20)

        return bd



    def nukeBornMetadataNode(self):
        print('my nukeBornMetadataNode')

        newCreatedNodeMetadata = self.nukeBornBigKNode('bigK', 'ModifyMetaData')

        fpsFromProjectSetting = nuke.Root().knob('fps').value()
        filenameWhenSave = os.path.basename(nuke.root().name())

        #newdata = "{set FramesPerSecond 2323}"
        newdata = "{set bigkframepersecond " + str(fpsFromProjectSetting) + "}" + '\n' + "{set bigk_nukeScript_From " + str(filenameWhenSave) + "}"
        newCreatedNodeMetadata['metadata'].fromScript(newdata)

        return newCreatedNodeMetadata


    def nukeUpdateMetadataNodeFps(self):
        print('my nukeUpdateMetadataNodeFps')
        allNodes = nuke.allNodes(filter='ModifyMetaData')
        fpsFromProjectSetting = nuke.Root().knob('fps').value()
        filenameWhenSave = os.path.basename(nuke.root().name())

        for i in allNodes:
            if 'bigK_' in i.name():
                print(i.name())

                newdata = "{set bigkframepersecond " + str(fpsFromProjectSetting) + "}" + '\n' + "{set bigk_nukeScript_From " + str(filenameWhenSave) + "}"
                i['metadata'].fromScript(newdata)



    def nukeUpdateWriteNodeVer(self):
        print('my nukeUpdateWriteNodeVer')
        # This function is intentionally read and update the path data according to the current content, instead of using bigkeeperinfo toolkit. To avoid unwanted overwrite data.

        # check if it is in Nuke Assist
        nukeEnv = nuke.env
        isAssist = nukeEnv['assist']

        '''
        if isAssist:
            theMessage = 'Warning !!!\n\n' + 'Currently in < Nuke Assist >.\n\n' + 'Therefore <Write Nodes> are not updated to align output version number.\n'+ '- Do not render this nuke script verion.\n' + '- < Version Up > in Nuke or Nuke X, before submit render to align the write node version number.'
            QMessageBox.information(self, 'WARNING !!! ', theMessage)'''


        bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
        currentVerNumber = bigKInfo.currentThisWipVerNum()
        currentTaskPath = bigKInfo.currentTaskPath()
        currentShotname = bigKInfo.currentShot()
        dedictatedPrefix = 'bigK'
        nodeClassName = 'Write'


        # Gather all the nodes in the scene
        allNodes = nuke.allNodes()
        print(allNodes)
        print(len(allNodes))
        print(type(allNodes))
        sameNodeNameList = []

        # sort out only (bigK + targetClassName)nodes, filter by .name()
        allFilteredNodes = []

        for i in allNodes:

            '''
            # to sort out Disabled Write node. For Freeze the version update status.
            if i.Class() == 'Write' and i.knob('disable').getValue() == True:
                pass

            else:
                mergePrefix = dedictatedPrefix + '_' + nodeClassName + '_'
                if i.name()[0:len(mergePrefix)] == mergePrefix:
                    sameNodeNameList.append(i.name())
                    #create a list containing "node" instead of nodeName, for coding convinient
                    allFilteredNodes.append(nuke.toNode(i.name()))
            '''

            # Cancel the above procedure of sorting out Disable Write Node. After discuss with Apple and Lik.
            mergePrefix = dedictatedPrefix + '_' + nodeClassName + '_'
            if i.name()[0:len(mergePrefix)] == mergePrefix:
                sameNodeNameList.append(i.name())
                #create a list containing "node" instead of nodeName, for coding convinient
                allFilteredNodes.append(nuke.toNode(i.name()))

        print(allFilteredNodes)

        '''
        # To avoid, in case, previous version is copy and paste from window explorer.
        try:
            seperator = '/output/v'
        except:
            seperator = '\output\v'
        '''

        seperatorKeywords = ['output', 'prerend']

        for i in allFilteredNodes:

            print(f"i.knob('file').value() : {i.knob('file').value()}")
            originalContent = os.path.normpath(i.knob('file').value())


            print('originalContent :')
            print(originalContent)

            if r'\vDrive' in originalContent:
                seperator = r'\vDrive'
                print(f'vDrive Node Found. -- {seperator}')

                basename = os.path.basename(originalContent)
                print(f'basename : {basename}')
                basenameFull = basename.split('.')
                print(f'basenameFull : {basenameFull}')
                basenameFullShotName = basenameFull[0].split('_')
                print(f'basenameFullShotName : {basenameFullShotName}')

                splitContent = originalContent.split(seperator)
                print(f'splitContent : {splitContent}')

                splitContentEnd = splitContent[-1]
                print(f'splitContentEnd : {splitContentEnd}')
                splitContentEnd = splitContentEnd.replace(basenameFullShotName[0], currentShotname)
                print(f'splitContentEnd : {splitContentEnd}')

                vDriveFolder = self.vDrivePathRead(os.path.join(bigKInfo.currentProjWorkPath(), 'bigPathsProject.ini'), 'BIGPATHS', 'vOutput')
                print(f'vDriveFolder : {vDriveFolder}')

                updatedContent = str(os.path.normpath(vDriveFolder + splitContentEnd))
                updatedContent = updatedContent.replace(os.sep, '/')

            else:

                for keyword in seperatorKeywords:
                    print(r'\{}\v'.format(keyword))
                    if r'\{}\v'.format(keyword) in originalContent:
                        seperator = r'\{}\v'.format(keyword)
                        print(seperator)

                #To find out current frame name for both CompMaster(tsq0010) & LayerMask(tsq0010_shadow), store in basenameFullShotName[0]
                basename = os.path.basename(originalContent)
                print(f'basename : {basename}')
                basenameFull = basename.split('.')
                print(f'basenameFull : {basenameFull}')
                basenameFullShotName = basenameFull[0].split('_')
                print(f'basenameFullShotName : {basenameFullShotName}')

                splitContent = originalContent.split(seperator)
                print(f'splitContent : {splitContent}')
                splitContentFront = splitContent[0]
                splitVerNumber = splitContent[1][0:4]
                splitContentEnd = splitContent[1][4::]

                print('splitContentEnd is :')
                print(splitContentEnd)
                splitContentEnd = splitContentEnd.replace(basenameFullShotName[0], currentShotname)

                newVerNumber = currentVerNumber
                updatedContent = str(os.path.normpath(currentTaskPath + seperator + str(newVerNumber).zfill(4) + splitContentEnd))
                updatedContent = updatedContent.replace(os.sep, '/')

            print('updatedContent :')
            print(updatedContent)

            os.path.normpath
            i.knob('file').setValue(updatedContent)

    def cleanUpCompOutput(self, inScns):
        print('my cleanUpCompOutput')

        import datetime
        totalSortoutCompSizeGB = 0

        # ref : https://pythonspot.com/pyqt5-input-dialog/
        keepVers, VersOkPressed = QInputDialog.getInt(self, 'Input :', 'How many Latest VERSIONS to be kept and protected?', 10, 1, 100, 1)
        if VersOkPressed:
            print('keepVers inputed : %d' %keepVers)


            keepDays, DaysOkPressed = QInputDialog.getInt(self, 'Input :', 'How many Latest DAYS to be kept and protected?', 30, 0, 100, 1)
            if DaysOkPressed:
                print('keepDays inputed : %d' %keepDays)

                showAskPath = True
                for selectedScn in inScns:

                    timerStart = datetime.datetime.now()

                    # Calculate boundary data (currentTime - KeepDays)
                    currentTimeStamp = datetime.datetime.now().timestamp()
                    currentTimeStamp_YYYYmmddHHMMSS = datetime.datetime.fromtimestamp(currentTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
                    print(currentTimeStamp_YYYYmmddHHMMSS)
                    value_currentTimeStamp_YYYYmmddHHMMSS = datetime.datetime.strptime(currentTimeStamp_YYYYmmddHHMMSS , '%Y-%m-%d %H:%M:%S')
                    DayValue = datetime.timedelta(days=keepDays)
                    boundryDate = value_currentTimeStamp_YYYYmmddHHMMSS - DayValue
                    print('boundryDate is : ')
                    print(boundryDate)
                    saveNameCurrentTimeStamp = 'toBeDel_' + selectedScn.text() + '_' + datetime.datetime.fromtimestamp(currentTimeStamp).strftime('-D%Y-%m-%d_T%H%M%S')

                    if showAskPath:
                        saveFullPath = None
                        saveFullPath = self.askSaveFile(saveNameCurrentTimeStamp)
                        saveDirPath = os.path.dirname(saveFullPath)
                    else:
                        saveFullPath = os.path.join(saveDirPath, saveNameCurrentTimeStamp + '.txt')

                    if saveFullPath != None:

                        sourceCheckPath = os.path.join(self.selProjScnPath, selectedScn.text())
                        print('<><><><><>')
                        print(selectedScn.text())
                        print(sourceCheckPath)
                        print('<><><><><>')

                        toBeDelList, toBeKeepList = self.cleanUpSortOutDelVers(sourceCheckPath, keepVers, keepDays)

                        print('toBeDelList is :')
                        for i in toBeDelList:
                            print(i)

                        print('toBeKeepList is :')
                        for i in toBeKeepList:
                            print(i)

                        totalSize = 0

                        print()

                        msgBox = QMessageBox()
                        msgBox.setStandardButtons(QMessageBox.NoButton)
                        msgBox.show()

                        for i in toBeDelList:
                            print(i)
                            size = self.cleanUpCheckFolderSize(i)
                            print('Path : ' + i + '     Size in MB : ' + str(size/1024/1024))
                            totalSize += size
                            QApplication.processEvents()
                            #msgBox.setText(os.path.normpath(i))
                            msg = 'Path : ' + str(i) + '     Size in MB : ' + str(size/1024/1024)
                            msgBox.setText(msg)

                        print()
                        '''print('toBeDelList is :')
                        print(toBeDelList)
                        for i in toBeDelList:
                            print(i)
                        '''

                        print()
                        print('Keeping %d Latest Vers ---OR--- verions within %d Latest Days (%s)' %(keepVers, keepDays, str(boundryDate)))
                        print('totalSize is :')
                        print('totalSize in MB (to be deleted) : ' + str(totalSize/1024/1024))
                        print('totalSize in GB (to be deleted) : ' + str(totalSize/1024/1024/1024))
                        totalSortoutCompSizeGB  += totalSize/1024/1024/1024
                        timerEnd = datetime.datetime.now()
                        print(timerEnd - timerStart)

                        headerContentList = []
                        headerContentList.append(str('Keeping %d Latest Vers ---OR--- verions within %d Latest Days (%s)' %(keepVers, keepDays, str(boundryDate))))
                        headerContentList.append(str('totalSize in MB (to be deleted): ' + str(totalSize/1024/1024)))
                        headerContentList.append(str('totalSize in GB (to be deleted): ' + str(totalSize/1024/1024/1024)))

                        #writePath = os.path.normpath(r'D:\\')
                        self.cleanUpWriteToText(saveFullPath, headerContentList, toBeDelList, toBeKeepList)

                        showAskPath = False

                        totalSizeLogFilePath = os.path.join(saveDirPath, 'sizeLog.txt')
                        f = open(totalSizeLogFilePath, 'w')
                        f.write(str(totalSortoutCompSizeGB))
                        f.close()




        print('\n\n')
        print(f'****************************************')
        print(f'**  Total sortout size (GB): {totalSortoutCompSizeGB}')
        print(f'****************************************')
        print('\n\n')



    def checkVerFolderFormat(self, inName):
        print('my checkVerFolderFormat')

        valid = None
        if inName[0] == 'v':
            for i in range(1, 5):
                if inName[i].isnumeric():
                    #print(inName[i])
                    valid = True
                else:
                    valid = False
                    break

        if valid:
            return True
        else:
            return False


    def cleanUpSortOutDelVers(self, inPathRoot, inKeepVers, inKeepDays):
        print('my cleanUpSortOutDelVers')

        keepVers = inKeepVers
        keepDays = inKeepDays

        delVersPath = []
        keepVersPath = []

        msgBox = QMessageBox()
        msgBox.setStandardButtons(QMessageBox.NoButton)
        msgBox.show()

        print('**********')
        print(inPathRoot)
        print('**********')

        # for loop of each SHOT
        #for i in self.listShot:
        for i  in os.listdir(inPathRoot):
            thePath = os.path.join(inPathRoot, i)
            print(thePath)


            theCompOutputPath = os.path.join(thePath, 'components', 'comp', 'output')
            print(theCompOutputPath)

            if os.path.isdir(theCompOutputPath):
                tempDirs = os.listdir(theCompOutputPath)
                print('tempDirs is : {} {}'.format(len(tempDirs), tempDirs))

                folderOnlyList = []

                # for loop of each version in SHOT-Comp-Output
                for j in tempDirs:

                    if self.checkVerFolderFormat(j) and os.path.isdir(os.path.join(theCompOutputPath, j)):
                        folderOnlyList.append(j)

                    unKeepFolderList = []
                    keepFolderList = []
                    keptVerNumList = []
                    counter = 0

                    folderOnlyList.sort(reverse = True)

                    for j in folderOnlyList[::]:

                        # to identify "CompMaster" and "_LayerMask"
                        previousJ = folderOnlyList[folderOnlyList.index(j)-1]
                        print('j in folderOnlyList : {} in {}'.format(j, folderOnlyList))
                        print('previousJ : {}'.format(previousJ))
                        #print(f'j is {j}, index is {folderOnlyList.index(j)}, j-1 is {folderOnlyList[folderOnlyList.index(j)-1]}, j[0:5] is {j[0:5]}, previousJ is {previousJ[0:5]}')

                        if counter < keepVers:
                            if j[0:5] != previousJ[0:5]:
                                counter += 1
                                keptVerNumList.append(j[0:5])
                                keepFolderList.append(j)
                            else:
                                pass
                                keptVerNumList.append(j[0:5])
                                keepFolderList.append(j)
                        else:
                            if j[0:5] == previousJ[0:5] and j[0:5] in keptVerNumList:
                                continue
                            else:
                                unKeepFolderList.append(j)

                print('folderOnlyList   : {} {}'.format(len(folderOnlyList), folderOnlyList))
                print('keepFolderList   : {} {}'.format(len(keepFolderList), keepFolderList))
                print('unKeepFolderList : {} {}'.format(len(unKeepFolderList), unKeepFolderList))

                for l in keepFolderList:
                    keepVersPath.append(os.path.normpath(os.path.join(theCompOutputPath, l)))

                for k in unKeepFolderList:
                    if self.isEarlierThanKeepDays(os.path.join(theCompOutputPath, k), keepDays):
                        #print('Earlier.\n')
                        delVersPath.append(os.path.normpath(os.path.join(theCompOutputPath, k)))
                    else:
                        keepVersPath.append(os.path.normpath(os.path.join(theCompOutputPath, l)))

            QApplication.processEvents()
            msgBox.setText(theCompOutputPath)


        msgBox.close()
        return delVersPath, keepVersPath


    def isEarlierThanKeepDays(self, inPath, inKeepDays):
        import datetime

        # ref : https://thispointer.com/python-get-last-modification-date-time-of-a-file-os-stat-os-path-getmtime/
        #filePath = r'N:\mnt\job\19901BigPicture_TestProj\WorkingFile\BigPicture19_TestProj\scenes\bensonSeq\tsq9010\components\comp\output'
        #keepDays = 50

        filePath = inPath
        keepDays = inKeepDays

        #modTimeStamp = os.path.getmtime(filePath)
        #currentTimeStamp = datetime.datetime.now().timestamp()
        createTimeStamp = os.path.getctime(filePath)
        creation_YYYYmmddHHMMSS = datetime.datetime.fromtimestamp(createTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
        print(creation_YYYYmmddHHMMSS)
        value_creation_YYYYmmddHHMMSS = datetime.datetime.strptime(creation_YYYYmmddHHMMSS, '%Y-%m-%d %H:%M:%S')

        #currentTimeStamp_YYYYmmddHHMMSS = datetime.datetime.fromtimestamp(currentTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
        #value_currentTimeStamp_YYYYmmddHHMMSS = datetime.datetime.strptime(currentTimeStamp_YYYYmmddHHMMSS , '%Y-%m-%d %H:%M:%S')
        #print(currentTimeStamp_YYYYmmddHHMMSS)


        # found boundary date (currentTime - keepDays)
        currentTimeStamp = datetime.datetime.now().timestamp()
        currentTimeStamp_YYYYmmddHHMMSS = datetime.datetime.fromtimestamp(currentTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
        print(currentTimeStamp_YYYYmmddHHMMSS)
        value_currentTimeStamp_YYYYmmddHHMMSS = datetime.datetime.strptime(currentTimeStamp_YYYYmmddHHMMSS , '%Y-%m-%d %H:%M:%S')
        DayValue = datetime.timedelta(days=keepDays)
        boundryDate = value_currentTimeStamp_YYYYmmddHHMMSS - DayValue
        print('boundryDate is : ')
        print(boundryDate)

        # Same date count as NOT Earlier, tends to keep for safe.
        if (datetime.datetime.strptime(str(creation_YYYYmmddHHMMSS), '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(str(boundryDate), '%Y-%m-%d %H:%M:%S')).days < -1:
            return True
        else:
            return False


    def cleanUpCheckFolderSize(self, inPathRoot):
        print('my cleanUpCheckFolderSize')
        print(inPathRoot)
        sizeUnit = {'Bytes': 1, 'Kilobytes': float(1)/1024, 'Megabytes': float(1)/(1024*1024), 'Gigabytes': float(1)/(1024*1024*1024)}
        total_size = 0
        start_path = inPathRoot  # To get size of current directory
        checking = True
        filecounter = 0

        for path, dirs, files in os.walk(start_path):
            for f in files:
                filecounter += 1
                #print(filecounter)
            totalfiles = filecounter

        filecounter = 0

        for path, dirs, files in os.walk(start_path):
            for f in files:
                filecounter += 1
                ###print(start_path)
                fp = os.path.join(path, f)
                fileSize = os.path.getsize(fp)
                total_size += fileSize

                ###print('%d of %d   ---   %d' %(filecounter, totalfiles, (filecounter/totalfiles)*100.0) + '%')
                #print(start_path)
                ###print(str(fp))
                ###print('total_size in MB : %s' %str(total_size * float(sizeUnit['Megabytes'])))



        print("Directory size in bytes: " + str(total_size))
        print("Directory size in MB: " + str(total_size * float(sizeUnit['Megabytes'])))

        #msgBox.close()

        return total_size

    def cleanUpWriteToText(self, inPath, inHeader, inDelList, inKeepList):
        print('my cleanUpWriteToText')
        import datetime

        currentTimeStamp = datetime.datetime.now().timestamp()
        currentTimeStamp_YYYYmmddHHMMSS = datetime.datetime.fromtimestamp(currentTimeStamp).strftime('-D%Y-%m-%d_T%H%M%S')
        #filename = 'toBeDel' + currentTimeStamp_YYYYmmddHHMMSS + '.txt'
        #f = open(os.path.join(inPath, filename), 'w')
        f = open(inPath, 'w')
        for lines in inHeader:
            f.writelines('<bigK_header>...' + lines + '\n')
        for lines in inDelList:
            f.writelines('< del* >' + lines + '\n')
        for lines in inKeepList:
            f.writelines('< Keep >' + lines + '\n')
        f.close()
        #print('Text File written to <%s>' %os.path.join(inPath, filename))
        print('Text File written to <%s>' %inPath)

    def askOpenFile(self):
        print('my askOpenFile')

        QMessageBox.information(self, 'Clean Up Comp Output', 'Warning !!!\n\n\nYou are about to mass DELETE folders!!!\n\n\n')

        # ref : https://pythonspot.com/pyqt5-file-dialog/
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)

        if fileName:
            print(fileName)
            return fileName



    def askSaveFile(self, inName):

            # ref : https://pythonspot.com/pyqt5-file-dialog/
            options = QFileDialog.Options()
            #options |= QFileDialog.DontUseNativeDialog
            fileNamePrefix = inName
            fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()", fileNamePrefix,"All Files (*);;Text Files (*.txt)", options=options)
            if fileName:
                print(fileName)
                return fileName





    def cleanUpDelAction(self):
        print('my cleanUpDelAction')

        import shutil

        '''
        theFile = self.askOpenFile()
        print(theFile)
        print(type(theFile))
        '''
        answerFolder = QInputDialog.getText(self, 'Input Folder Path', 'Please input the folder path containing ALL toBeDel_xxxxxxx.txt\n\n\n\n***** this is DELETE action. *****\n\n\n',QLineEdit.Normal)
        print(answerFolder[0])
        print(type(answerFolder[0]))

        allFiles = os.listdir(answerFolder[0])
        counter = 0
        delConfirm = False
        delToken = False

        # create _done directory to store the .txt
        doneFolder = os.path.join(answerFolder[0], '_done')
        if not os.path.exists(doneFolder):
            os.mkdir(doneFolder)
            print(doneFolder ,  " --- Created ")

        while delToken == False:
            inputCheck = QInputDialog.getText(self, 'Double Confirmation', 'If you confirm to batch delete all files.\n\n input the following correctly:\n\n"Confirm to delete a lot of files."\n\n\n',QLineEdit.Normal)
            if inputCheck[0] == 'Confirm to delete a lot of files.':
                delConfirm = True
                delToken = True

        if delConfirm == True:
            for file in allFiles:

                theFile = os.path.join(answerFolder[0], file)
                print(theFile)

                if theFile.endswith('.txt'):
                    f = open(theFile, 'r')
                    linePaths = []
                    for line in f:
                        if not line.startswith('<bigK_header>') or not line.startswith('< KEEP >'):
                            if line.startswith('< del* >'):
                                counter += 1
                                targetPath = line.lstrip('< del* >').rstrip('\n')
                                linePaths.append(targetPath)
                                print(str(counter) + 'line :' + targetPath)
                                #ref : https://thispointer.com/python-how-to-delete-a-directory-recursively-using-shutil-rmtree/
                                shutil.rmtree(targetPath, ignore_errors=True)
                    f.close()

                    shutil.move(theFile, doneFolder)



        print('End of cleanUpDelAction.')


















    '''
    # ref: https://www.tutorialspoint.com/pyqt/pyqt_qinputdialog_widget.htm
    # ref: https://pythonspot.com/pyqt5-input-dialog/
    def ask(self):
        print('my ask')
        try:
            defaultText = self.answer[0]
        except:
            defaultText = ""
        self.answer = QInputDialog.getText(self, 'Input Folder Name', 'To create instance-shortcut for comment folder,\nformat: <yyyymmdd>\n\nor\n\nPress cancel to skip.',QLineEdit.Normal, defaultText)
        print(self.answer)

    def theAnswer(self):
        try:
            print('my theAnswer')
            print(self.answer)
            print(type(self.answer))
        except:
            print('No Value.')'''

sys.path.append(r'N:\bpPipeline\bigKeeperPy\py\pySide2UI\ui')
import childMenu as UiPyChild # path : N:\BigKeeper         WIP : N:\BigKeeper\py\pySide2UI\ui
sys.path.remove(r'N:\bpPipeline\bigKeeperPy\py\pySide2UI\ui')

# The QT Child window class
class ChildWindow(UiPyChild.Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None):
        super(ChildWindow, self).__init__(parent)
        self.setupUi(self)

# The QT window class for list out nukeWrongFormat
class subListView(UiList.Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None):
        super(subListView, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)

'''
class prerendKeywordListView(UiList.Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None):
        super(prerendKeywordListView, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        '''

class NewWIPDialogWindow(UiDialog.Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None):
        super(NewWIPDialogWindow, self).__init__(parent)
        self.setupUi(self)

class doneWindow(UiDone.Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None):
        super(doneWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)



class nukeTempWindow(UiNukeTemp.Ui_nukeReadNodeFrameInOut, QMainWindow):
    def __init__(self, parent = None):
        super(nukeTempWindow, self).__init__(parent)
        self.setupUi(self)
        #self.setWindowModality(Qt.ApplicationModal)


    def initializeNukeTempWindow(self):
        print('my initializeNukeTempWindow')
        self.pushButton_execute.clicked.connect(self.action)

    def LoadInOutFrame(self):
        print('my LoadInOutFrame')
        import bigKeeperInfoGlobal_published
        bigKInfo = bigKeeperInfoGlobal_published.bigKeepCLASS()
        self.lineEdit_NewFrameIn.setText(bigKInfo.currentShotFrameIn())
        self.lineEdit_NewFrameOut.setText(bigKInfo.currentShotFrameOut())


    def action(self):
        print('my action')

        if len(nuke.selectedNodes('Read')) < 1:
            QMessageBox.information(self, 'message', 'No "Read Node" is selected.')
            """if in_nuke:
                nuke.message('No "Read Node" is selected.')
            '''if in_maya:
                cmds.confirmDialog( title='Confirm', message='No "Read Node" is selected.', button=['OK'], defaultButton='OK')
            if in_houdini:
                hou.ui.displayMessage('No "Read Node" is selected.', buttons=('OK',), default_choice=0, close_choice=0)'''"""

        else:
            if self.lineEdit_NewFrameIn.text().isnumeric and self.lineEdit_NewFrameOut.text().isnumeric:
                FrameInInt = int(self.lineEdit_NewFrameIn.text())
                FrameOutInt = int(self.lineEdit_NewFrameOut.text())

                print(FrameInInt)
                print(FrameOutInt)

                counter = 0
                for n in nuke.selectedNodes('Read'):
                    n['first'].setValue(FrameInInt)
                    n['last'].setValue(FrameOutInt)
                    n['origfirst'].setValue(FrameInInt)
                    n['origlast'].setValue(FrameOutInt)
                    counter += 1

                if in_nuke:
                    msg = str(counter) + ' "Read Node" received.'
                    nuke.message(msg)

                self.close()

            else:

                if in_nuke:
                    nuke.message('Only accept Integer.')
                '''if in_maya:
                    cmds.confirmDialog( title='Confirm', message='Only accept Integer.', button=['OK'], defaultButton='OK')
                if in_houdini:
                    hou.ui.displayMessage('Only accept Integer.', buttons=('OK',), default_choice=0, close_choice=0)'''

class createShotNewTaskWindow(UiNewTask.Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None):
        super(createShotNewTaskWindow, self).__init__(parent)
        print('my createShotNewTaskWindow - __init__')
        self.setupUi(self)
        self.label.setText('New Task Name :')
        #self.setWindowModality(Qt.ApplicationModal)

class nukeAskKeywordWindow(UiPreset.Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None):
        super(nukeAskKeywordWindow, self).__init__(parent)
        print('my nukeAskKeywordWindow - __init__')
        #self.setWindowModality(Qt.ApplicationModal)
        self.setupUi(self)





def main():
    window = BigMainWindow()
    window.show()

    try:
        app.exec_()
    except:
        pass

if not in_houdini:
    if __name__ == "__main__":
        main()
else:
    main()






