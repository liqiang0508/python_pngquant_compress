#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import shutil
import fileUtils
# 压缩资源目录和生成目录
RES = "Res"
OUT = "Out"

#使用方法：第一个参数为压缩比 1-100 forexample: compress.py 20-60
print ("Start compress...........................................................................")
# print "sys.argv---",len(sys.argv)
# print(sys.argv[0]) # 打印sys.argv的第1个参数
main = "pngquant.exe"
if len(sys.argv)==1:
        quality = "20-50"#没有参数默认压缩比
else:
        quality = sys.argv[1]#压缩质量1-100


  # 看存在out文件夹不 如果不存在就新建文件夹，存在就删除重新创建空文件夹
if not os.path.exists(OUT):
    os.makedirs(OUT)
else:
    shutil.rmtree(OUT)
    os.makedirs(OUT)



fileUtils.copyFileTree(RES,OUT)#复制文件到输出目录
for dirpath,dirnames,filenames in os.walk(OUT):#压缩目录下的所有文件
            for file in filenames:
                    if file.endswith("png"):
                        print ("compressing......",os.path.join(dirpath, file))
                        cmd = main + " -f --ext .png --quality "+quality+" "+os.path.join(dirpath, file)
                        os.popen(cmd)
                    # %PNGQUANT% -f --ext .png --quality 90-95 "%%i"

print ("End compress................................................................................")

os.system("pause")