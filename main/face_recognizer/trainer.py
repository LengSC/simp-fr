# -*- coding: utf-8 -*-


import cv2
from logger import Logger
import numpy as np


class Trainer:
    def __init__(self):
        self.logger = Logger()
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

        self.trainer = cv2.face.LBPHFaceRecognizer()

    def train(self) -> None:
        self.logger.log('info', '准备开始训练。')
        face_id = int(input('你的ID，寡人要整数：'))

        face_samples = list()
        cnt = 0

        self.logger.log('info', '开始采集人脸。')

        while cnt < 64:
            img_raw = self.cap.read()[1]
            img_gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=5, minSize=(32, 32))

            for (x, y, w, h) in faces:
                face_samples.append(img_gray[x: x + w, y: y + h])
                cv2.rectangle(img_raw, (x, y), (x + w, y + h), (0x3b, 0x2a, 0x19), 2)

            cnt += len(faces)

            cv2.imshow(f'Training, {cnt} of 64', img_raw)

            if cv2.waitKey(10) == 27:
                break

        self.logger.log('info', '人脸采集结束。')

        self.logger.log('info', '开始训练模型。')

        self.trainer.train(face_samples, np.array([face_id] * 64))

        self.logger.log('info', '模型训练结束。')


if __name__ == '__main__':
    t = Trainer()
    t.train()
