import torch
import glob
import json
import random
import os
from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import subprocess




subprocess.call("test.py --trained_model=./craft_mlt_25k.pth --cuda False --test_folder=./image", shell=True)

test_file = glob.glob('./image/*.jpg')
print(test_file[0][:-4])


for i in range(len(test_file)):
    tmp_string = test_file[i].replace('image', 'image_result')
    box_list = pd.read_table(tmp_string[:-4] + '_res.txt', sep=',', header = None)
    box_df = pd.DataFrame(box_list)
    tmp_img = Image.open(test_file[i])
    for j in range(len(box_df)):
        tmp_list = list(box_df.loc[j,:])
        if(tmp_list[1] > tmp_list[3] + 5): #직사각형 형태만 crop, 마름모 제외
            continue
        else:
            tmp_crop = tmp_img.crop((tmp_list[0], tmp_list[1], tmp_list[4], tmp_list[5])).convert("RGB")
            tmp_crop.save("./image_localized/" + str(j) + ".jpg") #################### 여기만 save로 수정 후 이후 recognition 모델에서 test 해주면 됨



#subprocess.call("demo.py --Transformation None --FeatureExtraction VGG --SequenceModeling BiLSTM --Prediction CTC --image_folder image_localized/ --saved_model korean_g2.pth", shell=True)


subprocess.call("tesseract.py", shell=True)
#출력문 분석하기, 출력문 txt파일로 저장하기

subprocess.call("extraction.py", shell=True)

with open('result.txt', 'w', encoding = 'utf-8') as f:
    f.write('')


datas = os.listdir('image')
for data in datas:
    os.remove('image/' + data)
datas = os.listdir('image_result')
for data in datas:
    os.remove('image_result/' + data)
datas = os.listdir('image_localized')
for data in datas:
    os.remove('image_localized/' + data)


