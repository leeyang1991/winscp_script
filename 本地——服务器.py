# coding=gbk

import time
import subprocess
import os
import codecs

this_root = os.getcwd()+'\\'
last_name = this_root.split('\\')[-2]
print(last_name)
# exit()
###########config##############
user = 'ly_sync'
passwd = 'asdfasdf'
ftp = '10.8.0.3'
port = '8080'
local_dir = this_root
remote_dir = '/'
sleep_time = 10
###########config##############


mkdir_script = 'open ftp://%s:%s@%s:%s/'%(user,passwd,ftp,port)+'\n'\
                'mkdir '+remote_dir+last_name+'\n'\
                'exit'

# print(mkdir_script)
# exit()


# synchronize both "C:\local_dir\" /remote_dir/
# option batch off



script = 'open ftp://%s:%s@%s:%s/\n' \
        'option batch continue \n'\
         'synchronize remote -delete %s %s\n' \
        'option batch off  \n'\
         'exit'%(user,passwd,ftp,port,local_dir,remote_dir+last_name)

f = codecs.open(this_root+'script.com','w','utf-8')
f.write(script)
f.close()
# outputFp = codecs.open(outputFilename, 'w');
# outputFp.write(testStrUtf8)
# codecs.open('test.txt','r','utf-8')
f = codecs.open(this_root+'mkdir_script.com','w','utf-8')
f.write(mkdir_script)
f.close()
# exit()
cmd_mkdir = r'"C:\Program Files (x86)\WinSCP\winscp" /script='+this_root+'mkdir_script.com'
subprocess.call(cmd_mkdir,shell=True)


cmd = r'"C:\Program Files (x86)\WinSCP\winscp" /script='+this_root+'script.com'

while 1:
    subprocess.call(cmd,shell=True)
    time.sleep(sleep_time)
