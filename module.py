#!/usr/bin/python
import logTime

rootPath = '/home/edrop/edrop-trunk-singleton/'

modules = []
moduleDict = {}
moduleRelation = [
    ['mas', 'metaserver']
]


def findRelationModules(name):
    ret = []
    for names in moduleRelation:
        if names.count(name) != 0:
            for name in names:
                print name
                ret.append(moduleDict[name])
    return ret


class module(object):
    def __init__(self):
        super(module, self).__init__()
        self.name = ''
        self.path = ''
        self.fileMatch = ''
        self.taskStart = ''
        self.taskEnd = ''
        self.errorEnd = 'Send Error Response'
        self.logTime = logTime.logTime1


class test(module):
    def __init__(self):
        super(test, self).__init__()
        self.name = 'test'
        self.taskStart = 'MetaServerDispatcher( 72)'
        self.fileMatch = 'metaserver-edrop*.log*'
        self.path = 'E:/test'


class metaserver(module):
    def __init__(self):
        super(metaserver, self).__init__()
        self.name = 'metaserver'
        self.taskStart = 'MetaServerDispatcher( 72)'
        self.taskEnd = 'task.Task(202)'
        self.errorEnd = 'Send Error Response'
        self.fileMatch = 'metaserver-edrop*.log*'
        self.path = rootPath + 'happ/metaserver/logs'
        self.logTime = logTime.logTime2


class mas(module):
    def __init__(self):
        super(mas, self).__init__()
        self.name = 'mas'
        self.taskStart = 'ExecuteThread( 53)'
        self.taskEnd = 'Task(142)'
        self.errorEnd='Send error response'
        self.fileMatch = 'mas-edrop*.log*'
        self.path = rootPath + 'happ/mas/logs'
