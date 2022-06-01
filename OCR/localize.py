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
            tmp_crop.save("./bbjpg/" + str(j) + ".jpg") #################### 여기만 save로 수정 후 이후 recognition 모델에서 test 해주면 됨



