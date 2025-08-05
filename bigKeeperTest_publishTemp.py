import os, pathlib

def isNumPadPattern(inString):
    print('\ndef >>>>> isNumPadPattern')
    # all number
    # all @
    # all #
    # %04D

    loopToken = True
    while loopToken == True:
        # all number
        if inString.isdigit():
            loopToken = False
            #print('all number')
            break
        else:

            #all "@"
            if inString.count('@') == len(inString):
                loopToken = False
                #print('all @')
                break
            else:

                #all "#"
                if inString.count('#') == len(inString):
                    loopToken = False
                    #print('all #')
                    break

                else:

                    # %04d, %xxxxd
                    if inString[0] == '%' and inString[-1] == 'd' and inString[1:-1:1].isdigit():
                        loopToken = False
                        inString[1:-1:1]
                        #print('%04d, %xxxxd')
                        break
                    else:
                        break


    loopToken = not loopToken

    return loopToken

def nameStemPattern(inString):
    print('\ndef >>>>> nameStemPattern')

    print('inString : {}'.format(inString))
    splitedString = inString.split('.')
    splitedString.reverse()
    outputStringList = []
    foundIsDigit = False
    for i in splitedString:
        #print('check : ' + i)
        #print(foundIsDigit)
        #print(isNumPadPattern(i))
        if foundIsDigit == False:
            if isNumPadPattern(i):
                foundIsDigit = True
            else:
                foundIsDigit = False
        elif foundIsDigit == True:

            #print( 'APPEND' )
            outputStringList.append(i)


        #print(outputStringList)

    outputStringList.reverse()
    outputString = ''

    for i in outputStringList:
        outputString = outputString + '.' + i

    #print('outputString[1::] >>> {}'.format( outputString[1::]))

    return outputString[1::]

def isVersionPattern(inString):
    print('\ndef >>>>> isVersionPattern')

    if inString.startswith('v') or inString.startswith('V'):
        print('inString : {} is startswith "v" or "V".'.format(inString))
        if inString[1::].isdigit:
            print('inString : {} is startswith "v" or "V" and the rest are isdigit. it is a version pattern.'.format(inString))
            returnValue = True
        else:
            print('inString : {} is startswith "v" or "V" and the rest are NOT isdigit. NOT version pattern.'.format(inString))
            returnValue = False
    else:
        print('inString : {} is not startswith "v" or "V". NOT version pattern'.format(inString))
        returnValue = False

    return returnValue

def versionPatternFrontOrEnd(inStringA, inStringB):
    print('\ndef >>>>> versionPatternFrontOrEnd')

    if inStringA.endswith(inStringB):
        return 'End'
    elif inStringA.startswith(inStringB):
        return 'Front'
    else:
        return 'NoMatch'


def isLatestVersion(inNodeName, inVer, inVerBasename, inVerLongpath, inVerFullpath):
    print('\ndef >>>>> isLatestVersion')

    print('---\ninNodeName : {}\ninVer: {}\ninVerBasename : {}\ninVerLongpath : {}\ninVerFullpath : {}\n---'.format(inNodeName, inVer, inVerBasename, inVerLongpath, inVerFullpath))

    ''' Result example:
    ---
    inNodeName : Read1
    inVer: v0006
    inVerBasename : v0006
    inVerLongpath : N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\light\images\v0006
    inVerFullpath : N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\light\images\v0006\pearlA_rlyr\pearlA_rlyr.%04d.exr
                                                                                                                                          |---| Ver
                                                                                                                                          |---| verBaseName
                    |-------------------------------------------------------------------------------------------------------------------------| verLongpath
                    |----------------------------------------------------------------------------------------------------------------------------------------------------------| verFullPath
    ---


    ---
    inNodeName : Read2
    inVer: v0008
    inVerBasename : v0008_LayerMask
    inVerLongpath : N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\compB\output\v0008_LayerMask
    inVerFullpath : N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\compB\output\v0008_LayerMask\pearl\five0010_pearl.%04d.exr
                                                                                                                                          |---| Ver
                                                                                                                                          |-------------| verBaseName
                    |-----------------------------------------------------------------------------------------------------------------------------------| verLongpath
                    |----------------------------------------------------------------------------------------------------------------------------------------------------------| verFullPath
    ---




    '''
    inVerPathObjLong = pathlib.Path(inVerLongpath)
    print('inVerPathObjLong.parent : {}'.format(inVerPathObjLong.parent))

    inVerLongpath_tail = inVerFullpath[len(str(inVerLongpath))::]
    print('inVerLongpath_tail : {}'.format(inVerLongpath_tail))

    inVerFullpath_name = os.path.basename(inVerFullpath)
    print('inVerFullpath_name : {}'.format(inVerFullpath_name))

    inVerFullpath_stem = os.path.basename(inVerFullpath).split('.')[0]
    print('inVerFullpath_stem : {}'.format(inVerFullpath_stem))




    # use parent path to find all versions
    listFolders = os.listdir(inVerPathObjLong.parent)
    listFolders.sort()
    print(listFolders)



    # check path match without Basename
    #       find out index number of inVerBasename from the listFrolder
    inVerBasenameIndex = listFolders.index(inVerBasename)
    print('inVerBasenameIndex : {}'.format(inVerBasenameIndex))

    inVerBasenameNoVersion = inVerBasename.removesuffix(inVer)
    if inVerBasenameNoVersion != inVerBasename:
        versionIsSuffix = True
    else:
        inVerBasenameNoVersion = inVerBasename.removeprefix(inVer)
        versionIsSuffix = False
    print('inVerBasenameNoVersion : {}'.format(inVerBasenameNoVersion))
    print()

    latestVerPathPattern = None

    # Reverse the List to start backward from the highest version
    listFolders.sort(reverse = True)
    for i in listFolders:
        print('\ni :' + i)
        #compareBaseName = listFolders[i + (inVerBasenameIndex + 1)]
        compareBaseName = i
        latestVerBaseName = None








        print('check if-condition 1 of 5')
        '''
        check the < number of Digit > of the VerBasename:
                                v#### == v####
                          V####_layer == v####_layer
        five0010_lightPearl_wip_v#### == five0010_lightPearl_wip_v####
        '''
        print('if len(compareBaseName) == len(inVerBasename):')
        print(f'len({compareBaseName}) vs len({inVerBasename})')
        if len(compareBaseName) == len(inVerBasename):
            print(len(inVer))
            print(inVerBasenameNoVersion)

            print('versionPatternFrontOrEnd:')
            print(versionPatternFrontOrEnd(inVerBasename, inVer))

            if versionPatternFrontOrEnd(inVerBasename, inVer) == 'End':
                compareBaseNameSplit_noVersion = compareBaseName.removesuffix(compareBaseName[len(inVer) * -1::])
            elif versionPatternFrontOrEnd(inVerBasename, inVer) == 'Front':
                compareBaseNameSplit_noVersion = compareBaseName.removeprefix(compareBaseName[0:len(inVer):])

            '''
            #for ending with v####
            if compareBaseName.endswith(compareBaseName[len(inVer) * -1::]):
                compareBaseNameSplit_noInVer = compareBaseName.rstrip(compareBaseName[len(inVer) * -1::])

            #for starting with v####
            elif compareBaseName.startswith(compareBaseName[len(inVer) * -1::]):
                compareBaseNameSplit_noInVer = compareBaseName.lstrip(compareBaseName[len(inVer) * -1::])
            '''


            '''
            #for ending with v####
            if compareBaseName.endswith(inVerBasenameNoVersion):
                compareBaseNameSplit_noInVer = compareBaseName.rstrip(compareBaseName[len(inVer) * -1::])

            #for starting with v####
            elif compareBaseName.startswith(inVerBasenameNoVersion):
                compareBaseNameSplit_noInVer = compareBaseName.lstrip(compareBaseName[len(inVer) * -1::])
            '''






            print('check if-condition 2 of 5')
            '''
            check basename without Version :
                                  <Empty> == <Empty> (eg. v####)
                                   _layer == _layer
                 five0010_lightPearl_wip_ == five0010_lightPearl_wip_

            '''
            print('compareBaseNameSplit_noVersion :{}'.format(compareBaseNameSplit_noVersion))
            print('inVerBasenameNoVersion :{}'.format(inVerBasenameNoVersion))
            if compareBaseNameSplit_noVersion == inVerBasenameNoVersion:

                print(compareBaseName)
                print('lstrip /rstrip with : ' + compareBaseNameSplit_noVersion )
                if versionPatternFrontOrEnd(inVerBasename, inVer) == 'End':
                    print('line 262')
                    print(compareBaseName)
                    print(compareBaseNameSplit_noVersion)
                    print(compareBaseName.lstrip(compareBaseNameSplit_noVersion))
                    compareBaseNameSplit_AfterInVer = compareBaseName.removeprefix(compareBaseNameSplit_noVersion)
                elif versionPatternFrontOrEnd(inVerBasename, inVer) == 'Front':
                    print('line 268')
                    print(compareBaseName)
                    print(compareBaseNameSplit_noVersion)
                    print(compareBaseName.rstrip(compareBaseNameSplit_noVersion))
                    compareBaseNameSplit_AfterInVer = compareBaseName.removesuffix(compareBaseNameSplit_noVersion)
                print('compareBaseNameSplit_AfterInVer : {}'.format(compareBaseNameSplit_AfterInVer))
                print('line274')








                print('check if-condition 3 of 5')
                '''
                check version pattern starts with "v" or "V"
                                v???? == v????
                                V???? == V????

                '''
                if compareBaseNameSplit_AfterInVer.startswith('v') or compareBaseNameSplit_AfterInVer.startswith('V'):
                    #print('have v or V.')








                    print('check if-condition 4 of 5')
                    '''
                    check version pattern starts with "v" or "V"
                                    ?#### == ?####
                    '''
                    if compareBaseNameSplit_AfterInVer[1::].isdigit():
                        #print('format match.')
                    # To compare if the folder contain the same image sequence
                        #print(inVerLongpath_tail.rstrip(inVerFullpath_name))
                        #print(inVerLongpath_tail.rstrip(inVerFullpath_name)[1:-1])
                        inVerPathPattern      =os.path.normpath( os.path.join(inVerPathObjLong.parent, inVerBasename,   inVerLongpath_tail.rstrip(inVerFullpath_name)[1:-1]) )
                        compareVerPathPattern =os.path.normpath( os.path.join(inVerPathObjLong.parent, compareBaseName, inVerLongpath_tail.rstrip(inVerFullpath_name)[1:-1]) )
                        print('\ninVerBasename         : {}'.format(inVerBasename))
                        print('inVerPathPattern      : {}'.format(inVerPathPattern))
                        print('compareBaseName       : {}'.format(compareBaseName))
                        print('compareVerPathPattern : {}\n'.format(compareVerPathPattern))





                        # check the compare Paths
                        listFiles = os.listdir(compareVerPathPattern)
                        #print(listFiles)


                        for listedfile in listFiles:

                            #print('nameStemPattern : {}'.format(nameStemPattern(listedfile)))

                            '''
                            print('{} vs {}'.format(listedfile, inVerFullpath_stem + '.'))
                            if listedfile.startswith(inVerFullpath_stem + '.'):
                                print('                         : {}'.format(inVerFullpath_stem))
                                print('Matched pattern filename : {}'.format(listedfile))
                                break
                                '''

                            #print('{} vs {}'.format(nameStemPattern(listedfile) + '.',     inVerFullpath_stem + '.'))
                            #if (nameStemPattern(listedfile) + '.') == (inVerFullpath_stem + '.'):
                            #print('{} vs {}'.format(nameStemPattern(listedfile) + '.',     nameStemPattern(inVerFullpath_name) + '.'))








                            print('check if-condition 5 of 5')
                            if (nameStemPattern(listedfile) + '.') == (nameStemPattern(inVerFullpath_name) + '.'):
                                #print('                         : {}'.format(nameStemPattern(listedfile) + '.'))
                                #print('Matched pattern filename : {}'.format(listedfile))

                                latestVerPathPattern = compareVerPathPattern
                                latestVerBaseName = compareBaseName

                                print('<><>'*80 + '\n' + latestVerPathPattern +'\n' + '<><>'*80)
                                print('latestVerBaseName FOUND :' + latestVerBaseName)
                                break
                            else:
                                #print('No Match pattern filename : x x x')

                                pass


                        if latestVerBaseName != None:
                            #print('269 break')
                            break
                    else:
                        print('Failed after check if-condition 4 of 5')
                else:
                    print('Failed after check if-condition 3 of 5')
            else:
                print('Failed after check if-condition 2 of 5')
        else:
            print('Failed after check if-condition 1 of 5')


    print('Latest WIP folder :')
    print(latestVerPathPattern)
    print(latestVerBaseName)
    return latestVerPathPattern, str(latestVerBaseName)


#'''
print('\nSample for Read1\n')
isLatestVersion('Read1',
                'v0006',
                'v0006',
                r'N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\light\images\v0006',
                r'N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\light\images\v0006\pearlA_rlyr\pearlA_rlyr.%04d.exr'
                )
#'''


#'''
print('\nSample for Read18\n')
isLatestVersion('Read18',
                'v0006',
                'five0010_lightPearl_wip_v0006',
                r'N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\lightPearl\images\five0010_lightPearl_wip_v0006',
                r'N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\lightPearl\images\five0010_lightPearl_wip_v0006\pearlA_rlyr\pearlA_rlyr.%04d.exr'
                )
#'''


#'''
print('\nSample for Read2\n')
isLatestVersion('Read2',
                'v0008',
                'v0008_LayerMask',
                r'N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\compB\output\v0008_LayerMask',
                r'N:\mnt\job\24068PantenePokemon\WorkingFile\PantenePokemon\scenes\zzzToliet\bensonPipelineTest\components\compB\output\v0008_LayerMask\pearl\five0010_pearl.%04d.exr'
                )

#'''