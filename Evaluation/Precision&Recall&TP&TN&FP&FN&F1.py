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


#
# b = np.array([[0,0,0]])
# c = np.insert(a, 0, values=b, axis=0)
index = np.array([["EMclass", "file", "TP", "TN", "FP", "FN", "Accuracy","Precision", "Recall","F1score", "interval_90_Accuracy","interval_95_Accuracy","interval_90_Precision","interval_95_Precision","interval_90_Recall","interval_95_Recall"]])

for iii in range(21):
    EMclass = str(iii)
    max = 0
    # root_address = "E:\\GAN\\21class=1vs20\\"+EMclass+"VS_others\\train-set\\"
    # root_address = "E:\\InceptionV3\\21class=1vs20\\" + EMclass + "VS_others\\train-set\\"
    # root_address = "E:\\Resnet\\21class=1vs20\\" + EMclass + "VS_others\\train-set\\"
    # root_address = "E:\\InceptionV3\\21class=1vs20\\" + EMclass + "VS_others\\validation-set\\"
    # root_address = "E:\\Resnet\\21class=1vs20\\" + EMclass + "VS_others\\validation-set\\"
    root_address = "E:\\VGG16\\21class=1vs20\\" + EMclass + "VS_others\\validation-set\\"

    leaf_address = ["original","dcgan15","dcgan35","dcgan55","dcgan75","dcgan95","wgan15","wgan35","wgan55","wgan75","wgan95","wgangp15","wgangp35","wgangp55","wgangp75","wgangp95"]
    # leaf_address = ["wgan15", "original"]
    # predict_data=pd.read_csv("C:/Users/Administrator/Desktop/" + "predict_all.csv",header=0)
    # print(predict_data.shape)
    for file in leaf_address:
        excel = root_address + file + "/" + "VGG16_validation_pred.csv"
        # excel = root_address + file + "\\" + "Inception_validation_pred.csv"
        # excel = root_address + file + "/" + "Resnet_validation_pred.csv"
        print(excel)
        data = pd.read_csv(excel)
        pic_number=105


        #1.取出A-E和F-I列数据，只取图片名字，positive possibility，预测类别
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
        # # 4.填一列为文件夹名字
        # file_name =  {"file_name": [file]*105}
        # file_name= pd.DataFrame(file_name)
        # positive.insert(0, "file_name", file_name)
        TP=0
        TN=0
        FP=0
        FN=0
        for i in range(105):
            positive_pred = positive.ix[i, "pred"]
            label = positive.ix[i, "label"]
            if label == "positive" and positive_pred == "[0]":
                TP=TP+1
            if label == "positive" and positive_pred == "[1]":
                FN=FN+1
            if label == "negative" and positive_pred == "[0]":
                FP=FP+1
            if label == "negative" and positive_pred == "[1]":
                TN= TN+1
        # print("TP:"+ str(TP))
        # print("TN:" + str(TN))
        # print("FP:" + str(FP))
        # print("FN:" + str(FN))
        Accuracy=(TP+TN)/105
        if TP !=0:
            Precision=TP/(TP+FP)
            Recall = TP / (TP + FN)
            F1score = 2 * Precision * Recall / (Precision + Recall)
        else:
            Precision =0
            Recall = 0
            F1score = 0

        interval_90_Accuracy = 1.64 * pow(  Accuracy*(1-Accuracy)/pic_number,0.5)
        interval_95_Accuracy = 1.96 * pow(Accuracy * (1 - Accuracy) / pic_number, 0.5)
        interval_90_Precision = 1.64 * pow(Precision * (1 - Precision) / pic_number, 0.5)
        interval_95_Precision = 1.96 * pow(Precision * (1 - Precision) / pic_number, 0.5)
        interval_90_Recall = 1.64 * pow(Recall * (1 - Recall) / pic_number, 0.5)
        interval_95_Recall = 1.96 * pow(Recall * (1 - Recall) / pic_number, 0.5)
        if file == "original":
            galaxy = np.array([[EMclass, file, str(TP), str(TN), str(FP), str(FN), str(Accuracy), str(Precision),
                                str(Recall), str(F1score), str(interval_90_Accuracy), str(interval_95_Accuracy),
                                str(interval_90_Precision), str(interval_95_Precision), str(interval_90_Recall),
                                str(interval_95_Recall)]])
            index = np.insert(index, -1, values=galaxy, axis=0)
        elif F1score > max:
            max= F1score
            galaxy = np.array([[EMclass, file, str(TP), str(TN), str(FP), str(FN), str(Accuracy), str(Precision),
                                str(Recall), str(F1score), str(interval_90_Accuracy), str(interval_95_Accuracy),
                                str(interval_90_Precision), str(interval_95_Precision), str(interval_90_Recall),
                                str(interval_95_Recall)]])
        # print("Accuracy:"+str(Accuracy))
        # print("Precision:"+str(Precision))
        # print("Recall:"+str(Recall))
        # print("F1score:"+str(F1score))
        # print("interval_90_Accuracy:"+str(interval_90_Accuracy))
        # print("interval_95_Accuracy:" + str(interval_95_Accuracy))
        # print("interval_90_Precision:" + str(interval_90_Precision))
        # print("interval_95_Precision:" + str(interval_95_Precision))
        # print("interval_90_Recall:"+str(interval_90_Recall))
        # print("iinterval_95_Recall:" + str(interval_95_Recall))
        # index= {"EMclass": EMclass,"file":file,"TP":TP,"TN":TN,"FP" :FP,"FN" :FN ,"Accuracy":Accuracy,"Precision":Precision,"Recall":Recall,"interval_90":interval_90,"interval_95":interval_95}

        ##############################################
        # galaxy = np.array([[EMclass,  file,str(TP),str(  TN),str(  FP),str( FN),  str(Accuracy),str( Precision),str(  Recall),str(F1score),str(interval_90_Accuracy),str(interval_95_Accuracy),str(interval_90_Precision),str(interval_95_Precision),str(interval_90_Recall),str(interval_95_Recall)]])
        # index = np.insert(index, -1, values=galaxy, axis=0)
        #################################################

        ################################################
    # galaxy = np.array([[EMclass, file, str(TP), str(TN), str(FP), str(FN), str(Accuracy), str(Precision),
    #                         str(Recall), str(F1score), str(interval_90_Accuracy), str(interval_95_Accuracy),
    #                         str(interval_90_Precision), str(interval_95_Precision), str(interval_90_Recall),
    #                         str(interval_95_Recall)]])
    index = np.insert(index, -1, values=galaxy, axis=0)
        ########################################################


        # insert_column = {"label": ["positive"] * 5}
        # index = pd.DataFrame(index)
index = pd.DataFrame(index)
index.to_csv("E://index0905_F1.csv")
print("done")

        # 5. 算出TP,TN,FP,FN
        # 5.根据"positive_possbility"从大到小排序
       #  positive = positive.sort_values(by='positive_possbility', ascending=False)
       #  # print(positive)
       #  # 6.添加一列为AP，判断label=="positive",则计算AP
       #  Precision = {"Precision": ["0"] * 105}
       #  Precision = pd.DataFrame(Precision)
       #  positive.insert(5, "Precision", Precision)
       #  # positive = pd.DataFrame(positive,columns = ["label","positive_name","positive_possbility","pred","AveragePrecision"])
       #  positive=positive.reset_index(drop =True)
       #  fenzi=0
       #  AveragePrecision=0
       #  # for i in range(210):
       #  for i in range(105):
       #      if
       #      positive_pred = positive.ix[i, "pred"]
       #      label = positive.ix[i, "label"]
       #
       #      if label == "positive":#positive_pred == "[0]" and
       #          fenzi=fenzi+1
       #          positive.loc[i,'Precision']=str(fenzi/(i+1))
       #          AveragePrecision=(AveragePrecision*(fenzi-1)+fenzi/(i+1))/fenzi
       #
       #  print(AveragePrecision)
       # mkdir("E://Resnet/AP//epoch100//g" + str(iii + 1).zfill(2) + "//")
       #  print("E://Resnet/AP//epoch100//g" + str(iii + 1).zfill(2) + "//")
       #  positive.to_csv("E://Resnet/AP//epoch100//g" + str(iii + 1).zfill(2) + "//" + str(
       #      '{:.4f}'.format(AveragePrecision)) + "_" + "validation_" + file + ".csv")
       #  print("E://Resnet/AP//epoch100//g" + str(iii + 1).zfill(2) + "//" + str(
       #      '{:.4f}'.format(AveragePrecision)) + "_" + "validation_" + file + ".csv")
       #  # os.system("pause")
