# -*- coding: cp936 -*-
import os
import time

# 在列表中写明需要备份的文件名和或目录
source = [r'"/home/xiaonuo/somefile"']

# 备份到下面的目录中
target_dir = '/home/xiaonuo/zipfile'

# 备份为zip文件，文件名是: 年月日时分秒.zip
target = target_dir + '备份' + '.zip'

# 用winrar的命令行来压缩文件，前提是winrar在windowsXP的path中
zip_command = "zip -qr %s %s" % (target, ''.join(source) ) 


# 运行这个备份程序来备份
if os.system(zip_command) == 0:
  print 'Successful backup to', target
else:
  print 'Backup FAILED!'