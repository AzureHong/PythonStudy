
# 不能实际运行的版本，仅用来学习逻辑和语法结构
# 实际应用中，可以使用zipfile或者tarfile内置的模块来创建他们的归档文档，这些都是标准库的一部分，随时供在PC中没有外部依赖的情况下使用这些功能

import os
import time
# 定义备份的文件与目录，并将其指定到列表中
source = ['/Users/swa/notes']

target_dir = '/Users/swa/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 将当前时间作为zip文件的名称，子目录为today
today = target_dir + os.sep +time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# 添加用户注释，用于辨别是否有评论，是否被修改
comment = input('Enter a commer --> ')
if len(comment) == 0:
    target = today + os.sep + now +'.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

zip_command = "zip -r {0} {1}".format(target,' '.join(source))

print('Zip command is:{}',zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to ',target)
else:
    print('Backup FATLED')




