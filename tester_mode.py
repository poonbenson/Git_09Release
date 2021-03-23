

def main():

    try:
        del release_mode
    except NameError:
        pass
    finally:
        print('current dir(): after')
        print(dir())

    print('===== tester mode =====')
    import sys

    targetRemovePath = "N:\\bpPipeline\\bigKeeperPy\\repo_09Release"
    targetAppendPath = "N:\\bpPipeline\\bigKeeperPy\\repo_03Tester"
    noOfTargetRemovePath = sys.path.count(targetRemovePath)
    if noOfTargetRemovePath > 0:
        for i in range(0, noOfTargetRemovePath):
            sys.path.remove(targetRemovePath)

    targetRemovePath = "N:\\bpPipeline\\bigKeeperPy\\repo_01Developer"
    targetAppendPath = "N:\\bpPipeline\\bigKeeperPy\\repo_03Tester"
    noOfTargetRemovePath = sys.path.count(targetRemovePath)
    if noOfTargetRemovePath > 0:
        for i in range(0, noOfTargetRemovePath):
            sys.path.remove(targetRemovePath)


    targeRemoveModule = 'release_mode'
    targeImportModule = 'tester_mode'
    try:
        del sys.modules[targeRemoveModule]
        del sys.modules['bigKeeperTest_publish']
    except:
        pass

    targeRemoveModule = 'developer_mode'
    targeImportModule = 'tester_mode'
    try:
        del sys.modules[targeRemoveModule]
        del sys.modules['bigKeeperTest_publish']
    except:
        pass

    sys.path.append(targetAppendPath)
    #import bigKeeperTest_publish
    #from devbigKeeperTest_publish import BigMainWindow
    from bigKeeperTest_publish import BigMainWindow

    sys.path.remove(targetAppendPath)
    #BigMainWindow.show_window()
    BigMainWindow.show_window()

if __name__ == '__main__':
    main()