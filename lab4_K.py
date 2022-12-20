import sys
import numpy as np
import cv2 as cv
from tkinter import *


def Oval():
    hsv_min = np.array((0, 77, 17), np.uint8)
    hsv_max = np.array((208, 255, 255), np.uint8)

    fn = 'donut.png'
    img = cv.imread(fn)

    hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV )
    thresh = cv.inRange( hsv, hsv_min, hsv_max )
    contours0, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours0:
        if len(cnt)>4:
            ellipse = cv.fitEllipse(cnt)
            cv.ellipse(img,ellipse,(0,255,255),2)

    cv.imshow('contours', img)

    cv.waitKey()
    cv.destroyAllWindows()

def Squad():
    
    hsv_min = np.array((0, 54, 5), np.uint8)
    hsv_max = np.array((187, 255, 253), np.uint8)

    fn = 'kart2.jpg' # имя файла, который будем анализировать
    img = cv.imread(fn)

    hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
        box = np.int0(box) # округление координат
        cv.drawContours(img,[box],0,(0,255,255),2) # рисуем прямоугольник

    cv.imshow('contours', img) # вывод обработанного кадра в окно

    cv.waitKey()
    cv.destroyAllWindows()



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

    btn = Button(window, text="Нахождение окружностей", padx=10, pady=7, command =Oval, bg='#ffe900')  
    btn.place(x = 50, y = 50, height= 60, width=200)

    btn2 = Button(window, text="Нахождение прямоугольных форм", padx=10, pady=7, command =Squad, bg='#ffe900')  
    btn2.place(x = 300, y = 50, height= 60, width=230)

    btn1 = Button(window, text="Выход", padx=10, pady=7, command =exit, bg='#ffe900')  
    btn1.place(x = 500, y = 150, height= 30, width=80)
    


    window.mainloop()

Menu()

