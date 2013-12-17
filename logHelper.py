#!/usr/bin/python
import re

import module

LOG_KEYSTR = re.compile(r':[\d]*_[\d]*')


class logItem(object):
    def __init__(self):
        super(logItem, self).__init__()
        self.keyId = ''
        self.startTime = 0
        self.endTime = 0
        self.server = ''

    def __str__(self):
        info=''
        for element in self.__dict__:
            info= info +" "+element+":"+str(self.__getattribute__(element))
        return info



def parseKeyId(str1):
    return str1[str1.index(':') + 1:str1.index("_")]


def parseLogItem(log):
    logItem1 = logItem()
    lines = log.split('<br>')
    startLine = lines[0]
    for module1 in module.modules:
        if startLine.find(module1.taskStart) != -1:
            break
    logItem1.server = module1.name
    logItem1.startTime = module1.logTime.findTime(startLine)
    logItem1.keyId = parseKeyId(LOG_KEYSTR.findall(startLine)[0])
    endLine = ''
    for i in range(1, len(lines)):
        if lines[-i] == '':
            continue
        if lines[-i].find(module1.taskEnd) != -1:
            endLine = lines[-i]
            break
        if lines[-i].find(module1.errorEnd) != -1:
            endLine = lines[-i]
            break
        if lines[-i].find(module1.taskStart) != -1:
            break
    logItem1.endTime = module1.logTime.findTime(endLine)
    print logItem1
    return logItem1


class Content(object):
    def __init__(self):
        super(Content, self).__init__()
        self.datas = []

    def put(self, data):
        self.datas.insert(0, data)

    def insertFirst(self, newDatas):
        newDatas.extend(self.datas)
        self.datas = newDatas

    def toConsole(self):
        for data in self.datas:
            print data



def findInLastlog(name, key, module, components):
    key = ":" + key + "_"
    myfile = open(name, "r+")
    myfile.seek(0, 2)
    fileSize = myfile.tell()
    readSize = 10000 * 150
    flag = True
    content = Content()
    num = 0
    readNum = 1
    print key
    outFlag = False
    while num < 1:
        info = ''
        print myfile.tell()
        print 'readNum ' + str(readNum)
        seekSize = readSize * readNum
        if seekSize > fileSize:
            seekSize = fileSize
            readSize = fileSize % readSize
            outFlag = True
        myfile.seek(-seekSize, 2)
        readNum = readNum + 1
        datas = []
        lastLine = ''
        other= ''
        for line in myfile.readlines(readSize):
            if line.find(key) != -1:
                if line.find(module.taskStart) != -1:
                    if info != '':
                        flag = True
                        for component in components:
                            if component.endFilter(lastLine) == False:
                                flag = False
                                break
                        if flag:
                            num = num + 1
                            if other !='':
                                info = info +other
                            datas.append(info)
                            flag =False
                        info = ''
                    flag = True
                    for component in components:
                        if component.startFilter(line) == False:
                            flag = False
                            break
                    other = ''
                if flag:
                    if other !='':
                        info = info +other
                        other =''
                    info = info + line
                    lastLine = line
            else:
                if flag and module.logTime.findTime(line)==-1:
                    if line.strip() !='':
                        other = other+ line
                if line.find(module.taskStart) != -1:
                    flag =False
        other =''
        if info != '':
            #datas.append(info)
            info = ''
            lastLine = ''
        if len(datas) != 0:
            content.insertFirst(datas)
        if outFlag:
            break
    myfile.close()
    return content


if __name__ == '__main__':
    logItem = logItem()
    print logItem
    pass
    #cn = 1
    #if len(sys.argv) < 1:
    #    print 'arg num is not right'
    #    sys.exit(1)
    #    # name = sys.argv[1]
    #key = sys.argv[1]
    #logs = getLogs()
    #print logs[-1].name
    #filters = []
    #filters=sys.argv[1:]
    #content = findInLastlog(logs[-1].name, key, filters)
    #content.toConsole()
