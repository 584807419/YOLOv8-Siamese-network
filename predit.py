from ultralytics import YOLO


def y8_detect_xy(result):
    cls_dict = result.names
    cls_all = result.boxes.cls.tolist()
    print(f"识别结果目标类{len(cls_all)}个：{cls_all}")
    xyxy_all = result.boxes.xyxy.tolist()
    for i in range(len(cls_all)):
        label_name = cls_dict[int(cls_all[i])]
        box_xyxy = xyxy_all[i]
        box_mid_xyxy = [(box_xyxy[0] + box_xyxy[2]) / 2, (box_xyxy[1] + box_xyxy[3]) / 2]
        print(label_name)
        print(box_mid_xyxy)


if __name__ == '__main__':
    model = YOLO('./best.onnx', task='detect')  # 加载预训练的 YOLOv8n 模型,自动判断是目标检测任务还是分类classify任务等
    results = model.predict(source='./微信截图_20240204232320.png', show=True, save=True, imgsz=608,
                            device=0)
    # model.predict(source='./微信截图_20240204232307.png', show=True, save=True, imgsz=608,device=0)
    # model.predict(source='./微信截图_20240204232251.png', show=True, save=True, imgsz=608,device=0)
    # model.predict(source='./微信截图_20240204232251.png', show=True, save=True, imgsz=608,device=0)
    for result in results:
        y8_detect_xy(result)
    # model.val() # 在验证集模型上评估模型性能
