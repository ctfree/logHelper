#!/usr/bin/python
import sys

try:
    import web
except ImportError:
    sys.path.append("/home/edrop/opt/python/lib/python2.4/site-packages")
    import web

from web import form

components = []


class component(object):
    def __init__(self):
        super(component, self).__init__()
        self.key = ''
        self.input = None
        self.data = ''

    def startFilter(self, line):
        if self.data == '' or self.data == None:
            return True
        try:
            if line.find(self.data) != -1:
                return True
        except TypeError:
            print self.key, self.data
        return False

    def endFilter(self, line):
        return True

    def layout(self):
        return form.Textbox(self.key, description=self.key)


class keyFilter(component):
    def __init__(self, key):
        super(keyFilter, self).__init__()
        self.key = key
        self.data = ''

    def layout(self):
        return form.Textbox(self.key, description=self.key)


class srcFilter(component):
    def __init__(self):
        super(srcFilter, self).__init__()
        self.key = 'src'
        self.data = ''

    def startFilter(self, line):
        if self.data == 'all':
            return True
        if line.find(self.data) != -1:
            return True
        return False

    def layout(self):
        return form.Radio('src', ['all', 'web', 'windows', 'android', 'iphone'])


class beforeTime(component):
    def __init__(self, module):
        super(beforeTime, self).__init__()
        self.key = 'beforeTime'
        self.data = ''
        self.starTime = 0
        self.endTime = 0
        self.type = 1
        self.module = module

    def startFilter(self, line):
        time = self.module.logTime.findTime(line)
        if time <= self.starTime:
            return True
        return False

    def endFilter(self, line):
        time = self.module.logTime.findTime(line)
        if time >= self.endTime:
            return True
        return False

    def layout(self):
        return None


class afterTime(component):
    def __init__(self, module):
        super(afterTime, self).__init__()
        self.key = 'afterTime'
        self.data = ''
        self.starTime = 0
        self.endTime = 0
        self.type = 1
        self.module = module

    def startFilter(self, line):
        time = self.module.logTime.findTime(line)
        if  self.starTime <= time <=self.endTime:
            return True
        return False

    def endFilter(self, line):
        time = self.module.logTime.findTime(line)
        if  self.starTime <= time <=self.endTime:
            return True
        return False

    def layout(self):
        return None


class Exception(component):
    def __init__(self):
        super(Time, self).__init__()
        self.key = 'src'
        self.data = ''

    def startFilter(self, line):
        if line.find(self.data) != -1:
            return False
        return True

    def layout(self):
        return form.Radio('src', ['all', 'web', 'windows', 'android', 'iphone'])