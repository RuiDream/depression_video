# -*- coding: utf-8 -*-
from subprocess import call
import os
from tqdm import tqdm

# 读取原始视频，对视频进行分帧
# 视频的绝对路径和图片存储的目标路径以及读取标签进行存储
def extract_frames(src_path, target_path,label_path):
    new_path = target_path
    #打开label写入的txt路径和名称
    #writelabel=open('/home/caoyong/jiangyingying/videodata/secondbatchdata/label.txt','w+')
    #先遍历video下面的每个文件夹，再遍历每个文件夹下的mp4和txt文件
    dirs=os.listdir(src_path)
    dirs=sorted(dirs)
    labels = []
    for dir in dirs:
        dir=os.path.join(src_path,dir)
        if os.path.isdir(dir):
            files=os.listdir(dir)
            files=sorted(files)
            for file in files:
                filename = os.path.join(dir, file)
                if os.path.splitext(file)[1]=='.mp4':
                    cur_new_path = new_path + file.split('_')[0] + '/'
                    if not os.path.exists(cur_new_path):
                        os.mkdir(cur_new_path)
                    dest = cur_new_path + '%05d.jpg'
                    print(filename)
                    print(dest)
                    #在这里我手动去官网下载了ffmpeg，然后进行了环境变量的配置。
                    #在正常的windows 控制台是可以直接通过ffmpeg进行调用的。
                    #进行踩坑后发现在pycharm中需要将ffmpeg的路径填写完整才能进行调用。
                    # 这里的4为5fps，帧率可修改
                    call(["E:\DailySoftware\Ffmpeg\\ffmpeg-20190625-bb11584-win64-static\\bin\\ffmpeg", "-i", filename, "-r", "4", dest],shell = True)
                if os.path.splitext(file)[1]=='.txt':
                    #print(str(file))
                    lines=open(filename,'rb')
                    lines=list(lines)
                    score=int(lines[3])
                    if score<=4:
                        label=0
                    elif 5<=score<=9:
                        label=1
                    elif 10<=score<=14:
                        label=2
                    else:
                        label=3
                    tempLabel = str(file.split('_')[0]) + ":" + str(label) +"\n"
                    print(tempLabel)
                    labels.append(tempLabel)
    writeLabels(label_path,labels)

#将读取到的标签存入fileDir
def writeLabels(fileDir,label):
    file = open(fileDir,"w")
    with file as f:
        for i in range(len(label)):
            f.writelines(label[i])
    f.close()


extract_frames(src_path='T:\BaiduNetdiskDownload\DepressionDataset\\totalSet\Original_Video\\',
               target_path='T:\BaiduNetdiskDownload\DepressionDataset\\totalSet\Frame_Video\\',
               label_path="T:\BaiduNetdiskDownload\DepressionDataset\\totalSet\Labels\labels.txt")