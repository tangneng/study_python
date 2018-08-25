#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 9:12
# @Author  : StalloneYang
# @File    : file2folder.py
# @desc: 把相同文件类型的文件移动到一个文件夹中

import shutil
import os

path = 'E:\\N迈外迪'
files = os.listdir(path)
print(files)
for f in files:
    if '.' in f:
        folder_name = os.path.join(path + "/" + f.split('.')[-1])  # 文件的后缀，并把后缀做为文件夹名
        file = os.path.join(path + "/" + f)  # 文件的全路径
        if os.path.isfile(file):
            try:
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                    shutil.move(file, folder_name)
                else:
                    shutil.move(file, folder_name)
                print("将'{}'成功移动到路径'{}'中".format(f, folder_name))
            except shutil.Error:
                print("文件已经存在,'{}'移动失败".format(f))
            except Exception as e:
                print( 'move_file ERROR: ',e)
        else:
            print("文件移动完成！")
