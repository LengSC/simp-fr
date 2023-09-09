# -*- coding: utf-8 -*-


import cv2
from logger import Logger


class Recognizer:
    def __init__(self, model_dir: str = None):
        self.logger = Logger()
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

        # self.recognizer = cv2.face.LBPHFaceRecognizer()

        # try:
        #     self.recognizer.read(model_dir)
        # except cv2.Error:
        #     self.logger.log('error', '识别模型读取失败！')

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def recognize(self) -> None:
        self.logger.log('info', '开始识别。')

        while True:
            img_raw = self.cap.read()[1]
            img_gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=5, minSize=(32, 32))

            for (x, y, w, h) in faces:
                cv2.rectangle(img_raw, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('Recognizing', img_raw)

            if cv2.waitKey(10) == 27:
                break

        self.logger.log('info', '结束识别。')


if __name__ == '__main__':
    r = Recognizer(None)
    r.recognize()
