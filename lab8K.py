import cv2, os
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw, ImageTk
from matplotlib import pyplot as plt
from tkinter import *
from PIL import *




def Face():

    # Для детектирования лиц используем каскады Хаара
    cascadePath = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath)


    # Для распознавания используем локальные бинарные шаблоны
    recognizer = cv2.face.LBPHFaceRecognizer_create()


    def get_images(path):
        # Ищем все фотографии и записываем их в image_paths
        image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.happy')]
        
        images = []
        labels = []

        for image_path in image_paths:
            # Переводим изображение в черно-белый формат и приводим его к формату массива
            gray = Image.open(image_path)
            gray.convert('L')
            image = np.array(gray, 'uint8')
            # Из каждого имени файла извлекаем номер человека, изображенного на фото
            subject_number = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
            
            # Определяем области где есть лица
            faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            # Если лицо нашлось добавляем его в список images, а соответствующий ему номер в список labels
            for (x, y, w, h) in faces:
                images.append(image[y: y + h, x: x + w])
                labels.append(subject_number)
                # В окне показываем изображение
                cv2.imshow("", image[y: y + h, x: x + w])
                cv2.waitKey(50)
        return images, labels

        
    # Путь к фотографиям
    path = 'yalefaces'
    # Получаем лица и соответствующие им номера
    images, labels = get_images(path)
    cv2.destroyAllWindows()

    # Обучаем программу распознавать лица
    recognizer.train(images, np.array(labels))


    # Создаем список фотографий для распознавания
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]

    for image_path in image_paths:
        # Ищем лица на фотографиях
        gray = Image.open(image_path).convert('L')
        image = np.array(gray, 'uint8')
        faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        
        for (x, y, w, h) in faces:
            # Если лица найдены, пытаемся распознать их
            # Функция  recognizer.predict в случае успешного распознавания возвращает номер и параметр confidence,
            # этот параметр указывает на уверенность алгоритма, что это именно тот человек, чем он меньше, тем больше уверенность
            number_predicted, conf = recognizer.predict(image[y: y + h, x: x + w])

            # Извлекаем настоящий номер человека на фото и сравниваем с тем, что выдал алгоритм
            number_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
            
            if number_actual == number_predicted:
                print ("{} is Correctly Recognized with confidence {}".format(number_actual, conf))
            else:
                print ("{} is Incorrect Recognized as {}".format(number_actual, number_predicted))
            cv2.imshow("Recognizing Face", image[y: y + h, x: x + w])
            cv2.waitKey(1000)

def Menu():
    window = Tk()

    
    window.title("Menu")

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('400x200+{}+{}'.format(w, h))
    window.configure(bg='#ffc887')

    btn = Button(window, text="Нахождение грустных людей", padx=10, pady=7, command =Face, bg='#ffe900')  
    btn.place(x = 100, y = 50, height= 60, width=200)

    btn1 = Button(window, text="Выход", padx=10, pady=7, command =exit, bg='#ffe900')  
    btn1.place(x = 300, y = 150, height= 30, width=80)
    


    window.mainloop()

Menu()