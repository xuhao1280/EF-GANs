# encoding:utf-8
import csv,shutil
import pandas as pd
import numpy as np
import os


def mkdir(path):

    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("- - - new path - - - ")
    else:
        print("this foler exists")

        # shutil.rmtree(path)
        # os.makedirs(path)

# pandas.DataFrame用法
# data = pandas.DataFrame()
# 取某些列
# data=data[['column_a',...,'column_z']]
# 取某些行
# data=data[:10] //从头取10行
# 修改某个值
# data.loc[i,"AP"]=1

# 1.将表第一列名字加上文件夹名字
# pd.read_csv()绝对路径一定要用/,windows下也是如此,不加参数默认csv文件首行为标题行
# C:\\Users\\Administrator\\Desktop\\ganimage\\8VS_others\\train-set\\dcgan15
for iii in range(21):
    EMclass = str(iii)
    # root_address = "E:\\GAN\\21class=1vs20\\"+EMclass+"VS_others\\train-set\\"
    # root_address = "E:\\InceptionV3\\21class=1vs20\\" + EMclass + "VS_others\\train-set\\"
    # root_address = "E:\\Resnet\\21class=1vs20\\" + EMclass + "VS_others\\train-set\\"
    # root_address = "E:\\InceptionV3\\21class=1vs20\\" + EMclass + "VS_others\\validation-set\\"
    # root_address = "E:\\Resnet\\21class=1vs20\\" + EMclass + "VS_others\\validation-set\\"
    # root_address = "E:\\VGG16\\21class=1vs20\\" + EMclass + "VS_others\\validation-set\\"
    # root_address = "E:\\InceptionV3\\21class=1vs20\\" + EMclass + "VS_others\\validation-set\\epoch100\\"
    root_address = "E:\\Resnet\\21class=1vs20\\" + EMclass + "VS_others\\validation-set\\epoch100\\"
    leaf_address = ["dcgan15","dcgan35","dcgan55","dcgan75","dcgan95","wgan15","wgan35","wgan55","wgan75","wgan95","wgangp15","wgangp35","wgangp55","wgangp75","wgangp95","original"]
    # predict_data=pd.read_csv("C:/Users/Administrator/Desktop/" + "predict_all.csv",header=0)
    # print(predict_data.shape)
    for file in leaf_address:
        # excel = root_address + file + "/" + "VGG16_validation_pred.csv"
        # excel = root_address + file + "\\" + "Inception_validation_pred.csv"
        excel = root_address + file + "/" + "Resnet_validation_pred.csv"
        print(excel)
        data = pd.read_csv(excel)


        #1.取出A-E和F-I列数据，
        data = pd.read_csv(excel,usecols=[1,2,4,5,6,8])
        # print(data.head())
        #2.将A-E标签设为positive，F-I标签设为negative
        insert_column = {"label": ["positive"]*5}
        insert_column = pd.DataFrame(insert_column)
        data.insert(0, "label", insert_column)

        insert_column = {"label": ["negative"]*100}
        insert_column = pd.DataFrame(insert_column)
        data.insert(4, "label1", insert_column)
        # print(data)
        positive = data[["label","positive_name","positive_possbility","pred"]]
        negative = data[["label1","negative_name","positive_possbility1","pred1"]]
        # 3.将（F-I加标签）  接到  （A-E加标签） 下面
        negative.rename(
            columns={"label1": "label","negative_name":"positive_name","positive_possbility1":"positive_possbility","pred1":"pred"}, inplace=True)
        positive = positive[:5]
        # print(negative)

        positive=positive.append(negative, ignore_index=True)
        # print(positive)
        # 4.填一列为文件夹名字
        file_name =  {"file_name": [file]*105}
        file_name= pd.DataFrame(file_name)
        positive.insert(0, "file_name", file_name)
        # 5.根据"positive_possbility"从大到小排序
        positive = positive.sort_values(by='positive_possbility', ascending=False)
        # print(positive)
        # 6.添加一列为AP，判断label=="positive",则计算AP
        Precision = {"Precision": ["0"] * 105}
        Precision = pd.DataFrame(Precision)
        positive.insert(5, "Precision", Precision)
        # positive = pd.DataFrame(positive,columns = ["label","positive_name","positive_possbility","pred","AveragePrecision"])
        positive=positive.reset_index(drop =True)
        fenzi=0
        AveragePrecision=0
        # for i in range(210):
        for i in range(105):
            positive_pred = positive.ix[i, "pred"]
            label = positive.ix[i, "label"]

            if label == "positive":#positive_pred == "[0]" and
                fenzi=fenzi+1
                positive.loc[i,'Precision']=str(fenzi/(i+1))
                AveragePrecision=(AveragePrecision*(fenzi-1)+fenzi/(i+1))/fenzi

        print(AveragePrecision)
        # mkdir("E://InceptionV3/AP//epoch100//g"+str(iii+1).zfill(2)+"//")
        # print("E://InceptionV3/AP//epoch100//g"+str(iii+1).zfill(2)+"//")
        # positive.to_csv("E://InceptionV3/AP//epoch100//g"+str(iii+1).zfill(2)+"//"+str('{:.4f}'.format(AveragePrecision))+"_"+"validation_"+file+".csv")
        # print("E://InceptionV3/AP//epoch100//g" + str(iii + 1).zfill(2) + "//"+str('{:.4f}'.format(AveragePrecision))+"_"+"validation_"+file+".csv")
        mkdir("E://Resnet/AP//epoch100//g" + str(iii + 1).zfill(2) + "//")
        print("E://Resnet/AP//epoch100//g" + str(iii + 1).zfill(2) + "//")
        positive.to_csv("E://Resnet/AP//epoch100//g" + str(iii + 1).zfill(2) + "//" + str(
            '{:.4f}'.format(AveragePrecision)) + "_" + "validation_" + file + ".csv")
        print("E://Resnet/AP//epoch100//g" + str(iii + 1).zfill(2) + "//" + str(
            '{:.4f}'.format(AveragePrecision)) + "_" + "validation_" + file + ".csv")
        # os.system("pause")





