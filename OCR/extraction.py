import os
import json
from collections import OrderedDict


eng_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

info_dic = {'name':'', 'std_id':'', 'birth':'', 'department':'', 'college':'', 'is_ajou':'no'}

with open("result.txt", 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    ajou_flag=0  ###### flag for AJOU
    for line in lines:
        line = line[:len(line)-1]
        if line.upper() == 'AJOU':
            ajou_flag = 1
        elif line[:3] == '아주대':
            ajou_flag = 1
            
        name_flag = 0
        if line.isalpha() and len(line)==3:  # 한글, 3글자 == 이름
            for char in eng_char:
                for i in range(3):
                    if line[i] == char or line[i] == char.upper():
                        name_flag = 1
            if name_flag == 0:
                info_dic['name'] = line

        if line.isdigit() and len(line)==9:  #숫자, 9글자 == 학번
            info_dic['std_id'] = line

        slash_flag = 0
        if len(line)==10:                        #숫자, 슬래쉬2번, 10글자 == 생년월일
            if line.replace('/', '').isdigit():
                for char in line:
                    if char=='/':
                        slash_flag = slash_flag + 1
            if slash_flag==2:
                info_dic['birth'] = line
                
        if line[-2:]=='학과':              #끝 2글자가 학과 ==학과
            info_dic['department'] = line
        if line[-2:]=='대학':              #끝 2글자가 대학==소속대학
            info_dic['college'] = line

if ajou_flag == 0:
    info_dic = {'name':'', 'std_id':'', 'birth':'', 'department':'', 'college':'', 'is_ajou':'no'}
else:
    info_dic['is_ajou'] = 'yes'
with open('info.txt', 'w', encoding = 'utf-8') as f:
    for key in info_dic.keys():
        f.write(key + ' ' + info_dic[key] + '\n')


file_data = OrderedDict()
if ajou_flag == 0:
    file_data["name"] = ""
    file_data["std_id"] = ""
    file_data["birth"] = ""
    file_data["department"] = ""
    file_data["college"] = ""
    file_data["is_ajou"] = info_dic['is_ajou']
else:
    file_data["name"] = info_dic['name']
    file_data["std_id"] = info_dic['std_id']
    file_data["birth"] = info_dic['birth']
    file_data["department"] = info_dic['department']
    file_data["college"] = info_dic['college']
    file_data["is_ajou"] = info_dic['is_ajou']




with open('info.json', 'w', encoding = "utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")






