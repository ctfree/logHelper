#!/usr/bin/python
import time
import re


class logTime(object):
    def __init__(self, len, format, re1):
        super(logTime, self).__init__()
        self.len = len
        self.format = format
        self.re = re1

    def str2long(self, str):
        date = str[:-4]
        mis = str[-3:]
        return long(time.mktime(time.strptime(date, self.format))) * 1000 + int(mis)

    def findTime(self, line):
        times=self.re.findall(line)
        if len(times) == 0:
            return -1
        return self.str2long(times[0])


timeTxt1 = '13/12/06 12:09:10.119'
timeTxt2 = '2013-12-06 00:02:58.764'
format1 = '%y/%m/%d %H:%M:%S'
format2 = '%Y-%m-%d %H:%M:%S'
timeRe1 = re.compile(r'[\d]{2}/[\d]{2}/[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}.[\d]{3}')
timeRe2 = re.compile(r'[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}.[\d]{3}')
logTime1 = logTime(len(timeTxt1), format1, timeRe1)
logTime2 = logTime(len(timeTxt2), format2, timeRe2)

if __name__ == "__main__":
    print time.time()
    print time.localtime()
    print time.gmtime()
    print time.strftime(format1, time.localtime(time.time()))
    print logTime1.str2long(timeTxt1)
    print logTime2.str2long(timeTxt2)