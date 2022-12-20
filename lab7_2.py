# coding=utf-8
import cv2
import math
from tkinter import *
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

def Points():
    plt.rcParams["font.family"] = "SimHei"# Прямое изменение словаря конфигурации и установка шрифта по умолчанию
    img = cv2.imread("1000.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Позвоните Ши-Томаси, оператор обнаружения углов
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

    # Конвертировать данные с плавающей точкой в ​​int, иначе они не могут быть нарисованы
    corners = np.int0(corners)

    for i in corners:
        # Разберите каждый элемент и соберите его в кортеж
        x, y = i.ravel() # Превратите 1x1x2 в 1x2
        # Нарисуйте углы на графике, для лучшего отображения установите радиус на 2
        cv2.circle(img, (x, y), 2, (0, 255, 255), -1)
    cv2.imshow('img', img)
    cv2.waitKey(0)



   
def lucas():
    cap = cv2.VideoCapture("video1.mp4")
    #ShiTomasi Параметры обнаружения углов
    feature_params = dict(maxCorners=100,
                          qualityLevel=0.3,
                          minDistance=7,
                          blockSize=7)
    #lucas kanade Обязательные параметры для оптического потока
    # maxLevel - количество используемых слоев пирамиды изображений
    lk_params = dict(winSize=(15, 15),
                     maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    #Случайный цвет
    color = np.random.randint(0, 255, (100, 3))
    # 【1】 Считайте первый кадр и выполните определение угла, чтобы определить точку, которую нужно отслеживать.
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
    # Создаем маску изображения для рисования
    mask = np.zeros_like(old_frame)
    while True:
        ret, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # [2] Передать угловые точки изображения предыдущего кадра, изображения следующего кадра и изображения предыдущего кадра в функцию оптического потока
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
        # Функция вернет точку с номером статуса.
        # Если количество состояний равно 1, это означает, что эта точка находится в следующем кадре (угловая точка в предыдущем кадре).
        # Если количество состояний равно 0, это означает, что эта точка не найдена в следующем кадре изображения.
        # Затем мы передаем эти точки в качестве параметров функции и итеративно реализуем отслеживание.
        # [3] Сохраните найденные точки и начертите трек
        good_new = p1[st == 1]
        good_old = p0[st == 1]
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            a=math.floor(a)
            b=math.floor(b)
            c, d = old.ravel()
            c=math.floor(c)
            d=math.floor(d)
            mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
            frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
        img = cv2.add(frame, mask)
        cv2.imshow('frame', img)
        k = cv2.waitKey(30)  # & 0xff
        if k == 27:
            break
        # [4] Обновить характерные точки предыдущего кадра и предыдущего кадра
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)
    cv2.destroyAllWindows()
    cap.release()


def Menu():
    window = Tk()

    
    window.title("Menu")

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('600x200+{}+{}'.format(w, h))
    window.configure(bg='#ffc887')

    btn = Button(window, text="Нахождение точек", padx=10, pady=7, command =Points, bg='#ffe900')  
    btn.place(x = 50, y = 50, height= 60, width=200)

    btn2 = Button(window, text="Вывод оптического потока", padx=10, pady=7, command =lucas, bg='#ffe900')  
    btn2.place(x = 300, y = 50, height= 60, width=200)

    btn1 = Button(window, text="Выход", padx=10, pady=7, command =exit, bg='#ffe900')  
    btn1.place(x = 500, y = 150, height= 30, width=80)
    


    window.mainloop()

Menu()
