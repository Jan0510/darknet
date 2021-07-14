#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from os import listdir, getcwd
from os.path import join, abspath

train_txt_name = 'traffic_train.txt'
val_txt_name = 'traffic_val.txt'


if __name__ == '__main__':
    source_folder='../../JPEGImages'  #地址是所有图片的保存地点
    dest='./' + train_txt_name  #保存train.txt的地址,对于train.txt(在ImageSets/Main/下)
    dest2='./' + val_txt_name  #保存val.txt的地址，对于val.txt(在ImageSets/Main/下)
    file_list=os.listdir(source_folder)       #赋值图片所在文件夹的文件列表
    source_folder1 = os.path.abspath(source_folder)
    train_file=open(dest,'a')                 #打开文件
    val_file=open(dest2,'a')                  #打开文件
    for file_obj in file_list:                #访问文件列表中的每一个文件
        file_path=os.path.join(source_folder1,file_obj)
        #file_path保存每一个文件的完整路径
        file_name,file_extend=os.path.splitext(file_obj)
        #file_name 保存文件的名字，file_extend保存文件扩展名
        file_num=int(file_name)  
        if(file_num<620):                     #保留620个文件用于训练
            train_file.write(file_path+'\n')  #用于训练前620个的图片路径保存在train.txt里面
            val_file.write(file_path+'\n')    #其余的文件保存在val.txt里面
	    print(file_path)
    train_file.close()#关闭文件
val_file.close()
