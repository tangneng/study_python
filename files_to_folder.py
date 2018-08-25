#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 9:12
# @Author  : superyang713
# @File    : file_folder.py
# @desc: 把相同文件类型的文件移动到一个文件夹中

import os
import shutil


def main():
    dest_folder =  'E:\\N迈外迪'
    sort_files(dest_folder)


def sort_files(dest_folder):
    """
    parameters:
        dest_folder: 要整理的文件夹的绝对地址。
    return:
        首先按照文件的后缀建立文件夹。然后将文件放入对应的文件夹内。
        特例：
            只有后缀或没有后缀的文件将会不予处理。
    """
    files = [f for f in os.listdir(dest_folder)
             if os.path.isfile(os.path.join(dest_folder, f))]
    for f in files:
        new_folder = os.path.join(dest_folder, os.path.splitext(f)[-1][1:])
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        try:
            shutil.move(os.path.join(dest_folder, f), new_folder)
        except shutil.Error:
            if f.startswith('.'):
                print('{} is a dot file.'.format(f))
            else:
                print('{} does not have file extension.'.format(f))


if __name__ == '__main__':
    main()
    
    
    
   
