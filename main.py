import time
from datetime import datetime
import asyncio
import cv2
import os

pathname = datetime.now().strftime('%Y-%m-%d')
filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
full_pathname = f'skrin/{pathname}'

if not os.path.exists(full_pathname):
    os.mkdir(full_pathname)


async def output(sleep, text):
    await asyncio.sleep(sleep)
    print(text)


async def look():
    print(f"Started: {time.strftime('%X')}")
    await output(000.1, 'СТАРТ')
    # await asyncio.sleep(0.5)
    cam = cv2.VideoCapture(0)
    count = 0
    while True:
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            # Сохраняем лицо
            cv2.imwrite(f'{full_pathname}/user.' + str(count) + '.' + str(filename) + '.jpg', gray)
        cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff  # 'ESC'
        if k == 27:
            break
        elif count >= 1:
            continue
    # cam.release()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    while True:
        asyncio.run(look())
        cv2.destroyAllWindows()