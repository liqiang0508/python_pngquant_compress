#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件操作类
import os  
import time # 引入time模块
import shutil



#复制src目录下面所有的文件到 dst目录下面 
def copyFileTree(src,dst ): 
	if os.path.exists(dst):
		print(dst+"  delete**** ")
		shutil.rmtree(dst)
	else:
		pass
			

	shutil.copytree(src, dst)
	print("copy tree %s -> %s"%( src,dst))
	# return


 # 复制文件
def copyFile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        # print "copy file %s -> %s"%( srcfile,dstfile)

# 创建文件夹
def makeDir(dir):
	if os.path.exists(dir):
		print("dir exists=="+dir)
		return
	os.makedirs(dir)



# 递归删除文件夹
def removeDir(dir):
	if os.path.exists(dir):

		shutil.rmtree(dir)
	else:
		print("no dir==="+dir)

# 删除文件
def deleteFile(filepath):
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		print("no file==" +filepath)