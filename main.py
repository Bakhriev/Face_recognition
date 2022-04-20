import sys
from datetime import datetime
import os
import time
import pickle

import pyttsx3 as pytt
import face_recognition
import asyncio
import cv2

pathname = datetime.now().strftime('%Y-%m-%d')
date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
full_pathname = f'skrin/{pathname}'

if not os.path.exists(full_pathname):  # <- Если нет директории, создадим её
    os.mkdir(full_pathname)


async def output(sleep, text):  # Создаём отдельный поток для цикла while
    await asyncio.sleep(sleep)
    print(text)


async def look():
    await output(000.1, 'Пауза')  # Притормаживаем наш шустрый цикл. (:
    # text = f"Время запуска : {time.strftime('%X')}"
    # tts = pytt.init()
    # tts.say(text)
    # tts.runAndWait()
    print(f"Started: {time.strftime('%X')}")  # Принтуем время старта
    # cam = cv2.VideoCapture('rtsp://admin:123456789q@192.168.72.70:554/cam/realmonitor?channel=1&subtype=0')
    cam = cv2.VideoCapture(0)  # Включаем камеру
    count_for_foto = 0
    #   Находим файл xml
    cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
    face_detector = cv2.CascadeClassifier(cascPathface)
    data = pickle.loads(open('face_enc', "rb").read())
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray
                                               , scaleFactor=1.1
                                               , minNeighbors=5
                                               , minSize=(60, 60)
                                               , flags=cv2.CASCADE_SCALE_IMAGE)
        # Преобразовать входной кадр из BGR в RGB
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Накладываем лица для лица во входном кадре
        encodings = face_recognition.face_encodings(rgb)
        names = []
        # Цикл накладывания лиц
        for encoding in encodings:
            # Сравниваем кодировки с кодировками в data['encodings']
            # Совпадения содержат массив с буливыми значениями True для наложения
            # и False для остальных соответственно
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            # Устанавливаем name = в -> unknown если ни одна кодировка не совпадает
            name = "No name"
            # проверка на совпадения
            if True in matches:
                # Находим позиции в True и сохраняем
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                # Цикл по совпавшим индексам и ведение счёта для
                # Каждого распознанного лица
                for i in matchedIdxs:
                    # Проверяем имена в соответствующих индексов которые мы нашли
                    name = data["names"][i]
                    # Увеличиваем кол - во для имени которое нашли
                    counts[name] = counts.get(name, 0) + 1
                # Устанавливаем имя с наибольшим кол - вом
                name = max(counts, key=counts.get)
                # Обновляем список имён в листе
            names.append(name)
            names.append(f"{time.strftime('%X')}")
            # Принтуем для проверки
            print(names)
            #   Голосовое приветствие
            if name == 'No name':
                text = "Лицо не распознано, пользователь неизвестен!!!"
                tts = pytt.init()
                tts.say(text)
                tts.runAndWait()
            else:
                text = 'Доброго утра ' + name + ' И, хорошего дня!'
                tts = pytt.init()
                time.sleep(000.1)
                tts.say(text)
                tts.runAndWait()

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count_for_foto += 1
            # Сохраняем лицо
            cv2.imwrite(f'{full_pathname}/user.' + str(name) + str(count_for_foto) +'.jpg', gray)
        # cv2.imshow('image', img) # Вывод изображения
        k = cv2.waitKey(100) & 0xff  # 'ESC'
        if name == 27:
            break
        elif count_for_foto >= 1:
            continue

    # cam.release()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    # asyncio.run(main())
    while True:
        asyncio.run(look())
        sys.exit(cv2.destroyAllWindows())
