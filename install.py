# -*- coding: cp936 -*-
import os
import time

# ���б���д����Ҫ���ݵ��ļ����ͻ�Ŀ¼
source = [r'"/home/xiaonuo/somefile"']

# ���ݵ������Ŀ¼��
target_dir = '/home/xiaonuo/zipfile'

# ����Ϊzip�ļ����ļ�����: ������ʱ����.zip
target = target_dir + '����' + '.zip'

# ��winrar����������ѹ���ļ���ǰ����winrar��windowsXP��path��
zip_command = "zip -qr %s %s" % (target, ''.join(source) ) 


# ����������ݳ���������
if os.system(zip_command) == 0:
  print 'Successful backup to', target
else:
  print 'Backup FAILED!'