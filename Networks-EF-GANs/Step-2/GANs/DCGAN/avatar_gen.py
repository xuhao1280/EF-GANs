# from avatarDcgan.avatar_model import AvatarModel
import tensorflow as tf
from dcganxuhao.avatar_model import AvatarModel
if __name__ == '__main__':
    for i in range(2):
        tf.reset_default_graph()
        dataname="E:\\augmentation\\g"+str(i+1).zfill(2)+"\\"
        genimage="E:\\genimage\\dcgan\\g"+str(i+1).zfill(2)+"\\"
        savemodel="E:\\savemodel\\g"+str(i+1).zfill(2)+"\\"
        print(dataname,"\n",genimage,"\n",savemodel)
        avatar = AvatarModel(dataname,savemodel,genimage)
        avatar.gen()
    # avatar = AvatarModel()
    # avatar.gen()
