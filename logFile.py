#!/usr/bin/python
import os
import fnmatch


class log(object):
    def __init__(self, name, time):
        super(log, self).__init__()
        self.name = name
        self.time = long(time)


def getLogs(module):
    dataPath = module.path
    files = os.listdir(dataPath)

    def compare(x, y):
        stat_x = os.stat(dataPath + "/" + x)
        stat_y = os.stat(dataPath + "/" + y)
        if stat_x.st_mtime < stat_y.st_mtime:
            return -1
        elif stat_x.st_mtime > stat_y.st_mtime:
            return 1
        else:
            return 0

    files.sort(compare)
    logs = []
    for file in files:
        if fnmatch.fnmatch(file, module.fileMatch):
            fileName = os.path.join(dataPath, file)
            log1 = log(fileName, os.stat(fileName).st_mtime * 1000)
            logs.append(log1)
    return logs
