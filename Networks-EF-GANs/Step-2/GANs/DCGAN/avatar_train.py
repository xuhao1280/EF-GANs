# from avatarDcgan.avatar_model import AvatarModel
from dcganxuhao.avatar_model import AvatarModel
import tensorflow as tf
import time

if __name__ == '__main__':
    for i in range(21):
        start = time.clock()
        filename = "C:\\GAN\\log\\dcgan\\g" + str(i + 1).zfill(2) +"\\"+ "log.txt"
        with open(filename, 'w+') as file_object:
            file_object.write('Batch_size: 100 \nepoch_size:4000\n')

        dataname = "C:\\GAN\\augmentation\\g" + str(i + 1).zfill(2) + "\\"
        ganimage = "C:\\GAN\\ganimage\\dcgan\\g" + str(i + 1).zfill(2) + "\\"
        savemodel = "C:\\GAN\\savemodel\\dcgan\\g" + str(i + 1).zfill(2) + "\\"
        gannumber = 300
        tf.reset_default_graph()
        print(dataname,"\n",ganimage,"\n",savemodel)
        avatar = AvatarModel(dataname,savemodel,ganimage,gannumber,filename)
        avatar.train()
        tf.reset_default_graph()
        avatar.gen()
        print("gan:"+ganimage)

        end = time.clock()
        print('Running time: %s Minutes' % '{:.2f}'.format((end - start)/60))
        with open(filename, 'a+') as file_object:
            file_object.write('Running time: %s Minutes\n' % '{:.2f}'.format((end - start) / 60))

