import os
import cv2

path = "images/"

images = []

for i in os.listdir(path):
    name,ext = os.path.splitext(i)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+i
        print (file_name)
        images.append(file_name)
        
count=len(images)
frame = cv2.imread(images[0])
width,height,channel = frame.shape
size = (width,height)
print(size)

out = cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*"DIVX"),1,size)

for char in range(0,count-1):
    frame = cv2.imread(images[char])
    out.write(frame)
out.release()
print("Done")


