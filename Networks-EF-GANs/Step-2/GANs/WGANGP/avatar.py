import os
import scipy.misc
import numpy as np
import random
# import cv2 as cv
from glob import glob
import matplotlib.pyplot as plt

class Avatar:

    def __init__(self,dataname):
        # self.data_name = 'H:/augmentation/g09' #输入图片pathC:\Users\Administrator\Desktop\background
        self.data_name = dataname
        # self.data_name = 'H:/augmentation/g09'
        self.source_shape = (96, 96, 3)
        self.resize_shape = (96, 96, 3)
        self.crop = True
        self.img_shape = self.source_shape if not self.crop else self.resize_shape
        self.img_list = self._get_img_list()
        self.batch_size = 100
        self.batch_shape = (self.batch_size, ) + self.img_shape
        self.chunk_size = len(self.img_list) // self.batch_size

        # 噪音图片size
        self.noise_img_size = 100
        # 卷积转置输出通道数量
        self.gf_size = 64
        # 卷积输出通道数量
        self.df_size = 64
        # 训练循环次数
        self.epoch_size = 4000
        # 学习率
        self.learning_rate = 0.0002
        # 优化指数衰减率
        self.beta1 = 0.5
        # 生成图片数量
        self.sample_size = self.batch_size

    def _get_img_list(self):
        path = os.path.join(os.getcwd(), self.data_name, '*.jpg')
        return glob(path)

    def _get_img(self, name):
        assert name in self.img_list
        img = scipy.misc.imread(name).astype(np.float32)
        if img.shape != self.source_shape:
            img=scipy.misc.imresize(img, self.source_shape)
            # plt.imshow(img.astype(np.uint8))
            # plt.show()
            #
            # img=scipy.misc.toimage(cv.resize(img,self.source_shape))
            # img.resize(self.source_shape)
        assert img.shape == self.source_shape,'尺寸有问题'
        # if img.shape != self.source_shape:
        #     img.resize(self.source_shape)

        return self._resize(img) if self.crop else img

    def _resize(self, img):
        h, w = img.shape[:2]
        resize_h, resize_w = self.resize_shape[:2]
        crop_h, crop_w = self.source_shape[:2]
        j = int(round((h - crop_h) / 2.))
        i = int(round((w - crop_w) / 2.))
        cropped_image = scipy.misc.imresize(img[j:j + crop_h, i:i + crop_w], [resize_h, resize_w])
        return np.array(cropped_image) / 127.5 - 1.

    @staticmethod
    def save_img(image, path):
        scipy.misc.imsave(path, image)
        return True

    def batches(self):
        start = 0
        end = self.batch_size
        for _ in range(self.chunk_size):
            name_list = self.img_list[start:end]
            random.shuffle(name_list)
            imgs = [self._get_img(name) for name in name_list]
            batches = np.zeros(self.batch_shape)
            batches[::] = imgs
            yield batches
            start += self.batch_size
            end += self.batch_size

if __name__ == '__main__':
    avatar = Avatar()
    batch = avatar.batches()
    b = next(batch)
    for num in range(len(b)):
        avatar.save_img(b[num], './GAN-Image/'+os.sep+str(num)+'.jpg')
# import os
# import scipy.misc
# import numpy as np
# from glob import glob
#
#
# class Avatar:
#
#     def __init__(self):
#         self.data_name = 'H:/save7/' #输入图片path
#         # self.source_shape = (96, 96, 3)
#         # self.resize_shape = (48, 48, 3)
#         self.source_shape = (96, 96, 3)
#         self.resize_shape = (96, 96, 3)
#         self.crop = True
#         self.img_shape = self.source_shape if not self.crop else self.resize_shape
#         self.img_list = self._get_img_list()
#         self.batch_size = 32
#         self.batch_shape = (self.batch_size, ) + self.img_shape
#         self.chunk_size = len(self.img_list) // self.batch_size
#
#         # 噪音图片size
#         self.noise_img_size = 200
#         # 卷积转置输出通道数量
#         self.gf_size = 64
#         # 卷积输出通道数量
#         self.df_size = 64
#         # 训练循环次数
#         self.epoch_size = 100
#         # 学习率
#         self.learning_rate = 0.0002
#         # 优化指数衰减率
#         self.beta1 = 0.5
#         # 生成图片数量
#         self.sample_size = 32
#
#     def _get_img_list(self):
#         path = os.path.join(os.getcwd(), self.data_name, '*.png')
#         return glob(path)
#
#     def _get_img(self, name):
#         assert name in self.img_list,'图片不存在'
#         img = scipy.misc.imread(name).astype(np.float32)
#         if img.shape != self.source_shape:
#             img.resize(self.source_shape)
#         if name[8:9] == "01":
#             type = 1
#         elif name[8:9] == "02":
#             type = 2
#         elif name[8:9] == "03":
#             type = 3
#         elif name[8:9] == "04":
#             type = 4
#         elif name[8:9] == "05":
#             type = 5
#         elif name[8:9] == "06":
#             type = 6
#         elif name[8:9] == "07":
#             type = 7
#         elif name[8:9] == "08":
#             type = 8
#         elif name[8:9] == "09":
#             type = 9
#         elif name[8:9] == "10":
#             type = 10
#         elif name[8:9] == "11":
#             type = 11
#         elif name[8:9] == "12":
#             type = 12
#         elif name[8:9] == "13":
#             type = 13
#         elif name[8:9] == "14":
#             type = 14
#         elif name[8:9] == "15":
#             type = 15
#         elif name[8:9] == "16":
#             type = 16
#         elif name[8:9] == "17":
#             type = 17
#         elif name[8:9] == "18":
#             type = 18
#         elif name[8:9] == "19":
#             type = 19
#         elif name[8:9] == "20":
#             type = 20
#         elif name[8:9] == "21":
#             type = 21
#
#         assert img.shape == self.source_shape,'尺寸有问题'
#         # if img.shape != self.source_shape:
#         #     img.resize(self.source_shape)
#
#         return self._resize(img) if self.crop else img ,type
#
#     def _resize(self, img):
#         h, w = img.shape[:2]
#         resize_h, resize_w = self.resize_shape[:2]
#         crop_h, crop_w = self.source_shape[:2]
#         j = int(round((h - crop_h) / 2.))
#         i = int(round((w - crop_w) / 2.))
#         cropped_image = scipy.misc.imresize(img[j:j + crop_h, i:i + crop_w], [resize_h, resize_w])
#         return np.array(cropped_image) / 127.5 - 1.
#
#     @staticmethod
#     def save_img(image, path):
#         scipy.misc.imsave(path, image)
#         return True
#
#     def batches(self):
#         start = 0
#         end = self.batch_size
#         for _ in range(self.chunk_size):
#             name_list = self.img_list[start:end]
#             imgs,type = [self._get_img(name) for name in name_list]
#             batches = np.zeros(self.batch_shape)
#             batches[::] = imgs
#             yield batches
#             start += self.batch_size
#             end += self.batch_size
#
# if __name__ == '__main__':
#     avatar = Avatar()
#     batch = avatar.batches()
#     b = next(batch)
#     for num in range(len(b)):
#         avatar.save_img(b[num], '5'+os.sep+str(num)+'.jpg')
