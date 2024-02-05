import json
import os
import cv2

img_folder_path = r'D:\develop\lableme_study\image'  # 图片存放文件夹
folder_path = r"D:\develop\lableme_study\image\result_json"  # 标注数据的文件地址
txt_folder_path = r"D:\develop\lableme_study\image\labels_txt"  # 转换后的txt标签文件存放的文件夹

all_map= {"大图文字":0,"小图文字":1}
# 保存为相对坐标形式 :label x_center y_center w h
def relative_coordinate_txt(img_name, json_d, img_path):
    src_img = cv2.imread(img_path)
    h, w = src_img.shape[:2]
    txt_name = img_name.split(".")[0] + ".txt"
    txt_path = os.path.join(txt_folder_path, txt_name)
    print(txt_path)
    with open(txt_path, 'w') as f:
        for item in json_d["shapes"]:
            # print(item['points'])
            # print(item['label'])
            point = item['points']
            x_center = (point[0][0] + point[1][0]) / 2
            y_center = (point[0][1] + point[1][1]) / 2
            width = point[1][0] - point[0][0]
            hight = point[1][1] - point[0][1]
            # print(x_center)
            f.write(" {} ".format(all_map[item['label']]))
            f.write(" {} ".format(x_center / w))
            f.write(" {} ".format(y_center / h))
            f.write(" {} ".format(width / w))
            f.write(" {} ".format(hight / h))
            f.write(" \n")


# 保存为绝对坐标形式 :label x1 y1 x2 y2
def absolute_coordinate_txt(img_name, json_d, img_path):
    src_img = cv2.imread(img_path)
    h, w = src_img.shape[:2]
    txt_name = img_name.split(".")[0] + ".txt"
    txt_path = os.path.join(txt_folder_path, txt_name)
    print("txt_path:\t", txt_path)
    with open(txt_path, 'w') as f:
        for item in json_d["shapes"]:
            # print(item['points'])
            # print(item['label'])
            point = item['points']
            x1 = point[0][0]
            y1 = point[0][1]
            x2 = point[1][0]
            y2 = point[1][1]
            f.write(" {} ".format(item['label']))
            f.write(" {} ".format(x1))
            f.write(" {} ".format(y1))
            f.write(" {} ".format(x2))
            f.write(" {} ".format(y2))
            f.write(" \n")


i = 0
for jsonfile in os.listdir(folder_path):
    temp_path = os.path.join(folder_path, jsonfile)

    # i += 1
    # if i > 5:
    #     break
    # 如果是一个子目录就继续
    if os.path.isdir(temp_path):
        continue
    print("json_path:\t", temp_path)
    jsonfile_path = temp_path
    with open(jsonfile_path, "r", encoding='utf-8') as f:
        json_d = json.load(f)
        img_name = json_d['imagePath'].split("\\")[-1].split(".")[0] + ".png"
        img_path = os.path.join(img_folder_path, img_name)
        print("img_path:\t", img_path)
        relative_coordinate_txt(img_name, json_d, img_path)
        # absolute_coordinate_txt(img_name, json_d, img_path)