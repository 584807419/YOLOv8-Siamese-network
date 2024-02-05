from ultralytics import YOLO

model = YOLO('./yolov8n.pt')
# 接受所有格式 - classify / dir / Path / URL / video / PIL / ndarray。0用于网络摄像头
# YOLOv8预测模式可以为各种任务生成预测，在使用流模式时返回结果对象列表或结果对象的内存高效生成器。通过在预测器的调用方法中传递stream=True来启用流模式。stream=True的流媒体模式应用于长视频或大型预测源，否则结果将在内存中累积并最终导致内存不足错误。
results = model.predict(source='https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/54/10/542081054/542081054-1-208.mp4?e=ig8euxZM2rNcNbhMhzdVhwdlhzKzhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1707069615&gen=playurlv2&os=ctosbv&oi=2584261250&trid=bbc0d0eccf99482a9c0e8ca26c0818e0T&mid=0&platform=html5&upsig=b41b27482494307572dea4835ead25d6&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&bw=343952&orderid=0,3&buvid=&build=0&mobi_app=&f=T_0_0&logo=80000000', show=True,device=0)
results = model.predict(source='1.mp4', show=True,device=0)# 展示预测结果
results = model.predict(source='cat.jpg', show=True)
results = model.predict(source='bird.jpg', show=True)
results = model.predict(source='bird.jpg', show=True)
#
# # from PIL
# im1 = Image.open("bus.jpg")
# results = model.predict(source=im1, save=True)  # 保存绘制的图像
#
# # from ndarray
# im2 = cv2.imread("bus.jpg")
# results = model.predict(source=im2, save=True, save_txt=True)  # 将预测保存为标签
#
# # from list of PIL/ndarray
# results = model.predict(source=[im1, im2])
