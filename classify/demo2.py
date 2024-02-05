from ultralytics import YOLO

model = YOLO('../yolov8n.pt')
results = model([
    # 'bird.jpg',
    #              'cat.jpg',
                 'people.jpeg'
                 ], stream=True)

tuili_jieguo = []

for result in results:
    if len(result.boxes.cls) > 0:
        for i in range(len(result.boxes.cls)):
            leibie_id = int(result.boxes.cls[i].item())
            leibie = result.names[leibie_id]

            xiangsudu = result.boxes.conf[i].item()

            zuobiao = result.boxes.xyxy[i].tolist()
            tuili_jieguo.append({
                "类别": leibie,
                "相似度": xiangsudu,
                "坐标": zuobiao,
            })

if len(tuili_jieguo) > 0:
    for i in tuili_jieguo:
        print(i)
else:
    print("没有找到任何元素")
