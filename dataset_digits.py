import cv2
import os
import numpy as np

image = cv2.imread("input/digits.webp")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cnt = 1
number = 0
for i in range(0, image.shape[0], 20):
    for j in range(0, image.shape[1], 20):
        result=image[i:i+20, j:j+20]
        dir=f"output/digits{number}"
        os.makedirs(dir, exist_ok=True)
        cv2.imwrite(f"{dir}/{number}_{cnt}.jpg", result)
        cnt+=1
        if cnt>500:
            cnt=1
            number+=1
        


