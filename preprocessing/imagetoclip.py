# -*- coding:utf8 -*-

import os
import shutil


def moveimage(filepath, imagesperclip):
    isloop = True
    for root, dirs, files in os.walk(filepath):
        if isloop:
            dirs = sorted(dirs)
            for dir in dirs:
                dir = root + '/' + dir
                print(dir)
                images = os.listdir(dir)
                count = 1
                print(len(images))
                images = sorted(images)
                for image in images:
                    if (count - 1) % imagesperclip == 0:
                        newdir = str(dir) + '/' + 'clip%03d' % ((count - 1) / imagesperclip + 1)
                        if not os.path.exists(newdir):
                            os.makedirs(newdir)
                    imagename = str(dir) + '/' + str(image)
                    shutil.move(imagename, newdir)
                    count = count + 1
        else:
            break
        isloop = False

moveimage('/home/caoyong/jiangyingying/videodata/imagealign_secondbatch',imagesperclip=24)