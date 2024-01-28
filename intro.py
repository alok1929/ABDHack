### STEPS FOLLOWED:###
# Clone repo:https://github.com/nicknochnack/RealTimeObjectDetection
# Collect images -code
# Setup labelling
# Label images
# Update labelmap
# Train
# Update checkpoint
# Detect

import cv2
import os
import time
import uuid

IMAGE_PATH = 'image/'

labels = ['current', 'pause', 'play']
number_imgs = 15

for label in labels:
    os.mkdir('image//'+label)
    cap = cv2.VideoCapture(0)
    time.sleep(5)
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(
            IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
