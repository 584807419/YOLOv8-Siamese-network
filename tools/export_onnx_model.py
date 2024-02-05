from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('./best.pt', task='detect')
    model.export(format='onnx', imgsz=608, simplify=True)
