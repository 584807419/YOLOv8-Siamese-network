from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('./yolov8n.pt', task='detect')  # 加载预训练的 YOLOv8n 模型,自动判断是目标检测任务还是分类classify任务等
    model.train(data='./click.yaml', epochs=1000, cache=True, imgsz=608, batch=32,
                workers=10, device='0')  # 训练模型
