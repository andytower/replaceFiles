#!/usr/bin/env python
import os
import shutil
import sys

def normalizeString(sString):
    if sString[0:1] == '"':
        sString = sString[1:len(sString)-1]
    return sString

def main():
    if len(sys.argv) == 4:
        sPath = sys.argv[1]
        sourceString = sys.argv[2]
        distString = sys.argv[3]
    elif len(sys.argv) == 3:
        sPath = os.getcwd()
        sourceString = sys.argv[1]
        distString = sys.argv[2]
    else:
        print('Incorrect command line argument',len(sys.argv))
        return
    files = os.listdir(sPath)
    nCount = 0
    for fileName in files:
        if not os.path.exists(os.path.join(sPath,'bak')):
            os.makedirs(os.path.join(sPath,'bak'))
        if os.path.isfile(os.path.join(sPath,fileName)):
            shutil.copyfile(os.path.join(sPath,fileName),os.path.join(os.path.join(sPath,'bak'),fileName+'.bak'))
            descriptorFile = open(os.path.join(sPath,fileName),'r')
            fileText = descriptorFile.read();
            descriptorFile.close();
            descriptorFile = open(os.path.join(sPath,fileName),'w')
            descriptorFile.write(fileText.replace(sourceString,distString))
            descriptorFile.close()
            nCount=nCount+1
    print('Processing files - ',nCount)

 
if __name__ == '__main__':
    main()
