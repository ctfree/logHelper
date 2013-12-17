#!/usr/bin/python
import time


class logTime(object):
    def __init__(self, len, format):
        super(logTime, self).__init__()
        self.len = len
        self.format = format

    def String2long(self, str):
        date = str[:-4]
        mis = str[-3:]
        return long(time.mktime(time.strptime(date, self.format))) * 1000 + int(mis)


timeTxt1 = '13/12/06 12:09:10.119'
timeTxt2 = '2013-12-06 00:02:58.764'
format1 = '%y/%m/%d %H:%M:%S'
format2 = '%Y-%m-%d %H:%M:%S'

logTime1 = logTime(len(timeTxt1), format1)
logTime2 = logTime(len(timeTxt2), format2)

if __name__ == "__main__":
    print time.time()
    print time.localtime()
    print time.gmtime()
    print time.strftime(format1, time.localtime(time.time()))
    print logTime1.String2long(timeTxt1)