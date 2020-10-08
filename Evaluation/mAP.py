# E:/GAN/AP//g"+str(iii+1).zfill(2)+"//"
# 求出g01-g21的mAP
# 把所有.csv文件的前6个字符转为数字，取平均即为mAP

import csv
import pandas as pd
import numpy as np
import os

#输入文件夹路径，返回文件夹内所有文件名
def files_name(dirpath):
    for root, dirs, files in os.walk(dirpath):
        return files
for iii in range(21):
    EMclass = str(iii)
    csv_path = "E:/GAN/AP//g"+str(iii+1).zfill(2)+"//"
    print(csv_path)
    csv_name = files_name(csv_path)
    mAP = 0
    for name in csv_name:
        # print(name[0:6])

        # 1.求mAP (name[0:6]就是AP)
        mAP = mAP + float(name[0:6])

    l = len(csv_name)
   #2.求和整除文件数量
    mAP = mAP/l
    print(mAP)
    mAP = "{}".format('{:.4f}'.format(mAP))
    filename = csv_path+"mAP_"+ mAP+".txt"
    with open(filename, 'a+') as file_object:
        file_object.write("mAP:"+mAP)
