import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw, ImageTk
from matplotlib import pyplot as plt
from tkinter import *
from tkinter.ttk import Entry
from tkinter import messagebox
from tkinter import filedialog
from PIL import *
from tkinter import ttk 
import win32api



class Image_:

    def Size(h):
        img = cv2.imread("kart2.jpg")

        height, width =  img.shape[:2]
        height = int(height*h)
        width = int(width*h)

        img = cv2.resize(img, (height, width), cv2.INTER_LINEAR)

        cv2.imshow("res", img)
        cv2.waitKey()


    def Gucci_flip_flap(money):

        image = cv2.imread("kart2.jpg")

        flip_image = cv2.flip(image,money)

        stack = np.hstack((image, flip_image))

        cv2.imshow("Flip image", stack)
        cv2.waitKey(0)


    def Proection(self):
        
        # Прочитайте исходное изображение.
        im_src = cv2.imread('100.png')
        # Четыре точки соответствия на обложке книги в исходном изображении
        pts_src = np.array([[0, 1], [403, 2], [405, 596], [2, 596]])
        # Прочитайте изображение для трансформации
        im_dst = cv2.imread('1000.png')
        # Четыре точки соответствия на обложке книги в изображении трансформации
        pts_dst = np.array([[183, 18], [376, 83], [426, 227], [152, 155]])
        # Рассчитайте гомографию
        h, status = cv2.findHomography(pts_src, pts_dst)
        
        # Трансформируем исходное изображение, используя полученную гомографию
        im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
        img1 = cv2.addWeighted(im_dst,0.8,im_out,0.6, 0)
        


        # Покажите картинки
        cv2.imshow("Destination Image", im_dst)
        cv2.imshow("Warped Source Image", img1)
        cv2.waitKey(0)

    def Shifting(x, y):

        img = cv2.imread("kart2.jpg")
        h, w = img.shape[:2]
        translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
        dst = cv2.warpAffine(img, translation_matrix, (w, h))
        cv2.imshow('Сдвиг', dst)
        cv2.waitKey(0)

    def Rotate(self):

        img = cv2.imread("kart2.jpg")

        srcTri = np.array( [[0, 0], [img.shape[1] - 1, 0], [0, img.shape[0] - 1]] ).astype(np.float32)
        dstTri = np.array( [[0, img.shape[1]*0.33], [img.shape[1]*0.85, img.shape[0]*0.25], [img.shape[1]*0.15, img.shape[0]*0.7]] ).astype(np.float32)
        warp_mat = cv2.getAffineTransform(srcTri, dstTri)
        warp_dst = cv2.warpAffine(img, warp_mat, (img.shape[1], img.shape[0]))

        
        center = (warp_dst.shape[1]//2, warp_dst.shape[0]//2)
        angle = -50
        scale = 0.6
        rot_mat = cv2.getRotationMatrix2D( center, angle, scale )
        warp_rotate_dst = cv2.warpAffine(warp_dst, rot_mat, (warp_dst.shape[1], warp_dst.shape[0]))

        stack = np.hstack((img, warp_dst, warp_rotate_dst))
        cv2.imshow("res", stack)

        cv2.waitKey()

    def Point(self):
        img = cv2.imread("kart2.jpg")

        cv2.imshow("res", img)
        cv2.findHomography


    def Rel_rotate( x, y, angle1):
        
        img = cv2.imread("kart2.jpg")

        center = (x, y)
        angle = angle1
        scale = 0.6
        rot_mat = cv2.getRotationMatrix2D( center, angle, scale )
        warp_rotate_dst = cv2.warpAffine(img, rot_mat, (img.shape[1], img.shape[0]), cv2.INTER_LINEAR)

        imstack = np.hstack((img, warp_rotate_dst))

        cv2.imshow("res", imstack)
        cv2.waitKey()


def menu_s():
    win2 = Toplevel()
    win2.title("Настройки")

    win2.geometry("300x100")


    def change():

        im = Image_
        height = float(en1.get())

        im.Size(height)



    lbl = Label(win2, text = "Введите коэффициент масштабирования: ")
    lbl.pack()

    en1 = Entry(win2)
    en1.pack()


    b1 = Button(win2, text= "Click", command = change)
    b1.pack()

def menu_r():
    win1 = Toplevel()
    win1.title("Настройки")

    win1.geometry("200x200")


    def change():

        im = Image_
        x = int(en1.get())
        y = int(en2.get())
        angle = int(en3.get())

        im.Rel_rotate(x, y, angle)



    lbl = Label(win1, text = "Введите координаты центра: ")
    lbl.pack()

    lbl1 = Label(win1, text = "X: ")
    lbl1.pack()

    en1 = Entry(win1)
    en1.pack()

    lbl2 = Label(win1, text = "Y: ")
    lbl2.pack()

    en2 = Entry(win1)
    en2.pack()

    lbl3 = Label(win1, text = "Angle: ")
    lbl3.pack()

    en3 = Entry(win1)
    en3.pack()

    b1 = Button(win1, text= "Click", command = change)
    b1.pack()

def menu_sh():
    win1 = Toplevel()
    win1.title("Настройки")

    win1.geometry("200x200")


    def change():

        im = Image_
        x = int(en1.get())
        y = int(en2.get())

        im.Shifting(x, y)



    lbl = Label(win1, text = "Введите координаты центра: ")
    lbl.pack()

    lbl1 = Label(win1, text = "X: ")
    lbl1.pack()

    en1 = Entry(win1)
    en1.pack()

    lbl2 = Label(win1, text = "Y: ")
    lbl2.pack()

    en2 = Entry(win1)
    en2.pack()

    b1 = Button(win1, text= "Click", command = change)
    b1.pack()

def menu_f():
    win2 = Toplevel()
    win2.title("Настройки")

    win2.geometry("300x150")


    def change():

        im = Image_
        h = int(en1.get())

        im.Gucci_flip_flap(h)



    lbl = Label(win2, text = "Введите одно из значений ниже: ")
    lbl.pack()
    lbl = Label(win2, text = "0 - отражение по вертикали ")
    lbl.pack()
    lbl = Label(win2, text = "1 - отражение по горизонтали")
    lbl.pack()
    lbl = Label(win2, text = "-1 - по вертикали и по горизонтали")
    lbl.pack()


    en1 = Entry(win2)
    en1.pack()


    b1 = Button(win2, text= "Click", command = change)
    b1.pack()


def Menu():
    window = Tk()

    img = Image_()
    
    window.title("Menu")

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('600x600+{}+{}'.format(w, h))
   


    
    window.config(background="#D2B48C")

    btn = Button(window, text="Поворот", command =menu_r , bg="#B0E0E6", font="Helvetica" )  
    
    btn.place(x=70, y = 40, width=200, height=50)

    btn1 = Button(window, text="Масштабирование", command = menu_s, bg="#B0E0E6", font="Helvetica")  
    
    btn1.place(x=350, y = 240, width=200, height=50)

    btn2 = Button(window, text="Проекция на плоскость" ,command = img.Proection, bg="#B0E0E6", font="Helvetica")  
    
    btn2.place(x=70, y = 240, width=250, height=50)

    btn3 = Button(window, text="Сдвиг", command = menu_sh, bg="#B0E0E6", font="Helvetica")  
   
    btn3.place(x=350, y = 40, width=200, height=50)

    btn4 = Button(window, text="Отражение", command = menu_f, bg="#B0E0E6", font="Helvetica" )  
    
    btn4.place(x=100, y = 140, width=400, height=50)

#    btn5 = Button(window, text="Изменение плоскости" ,command = img.Rotate, bg="##B0E0E6", font="Helvetica")  
    
 #   btn5.place(x=100, y = 340, width=400, height=50)












    btn6 = Button(window, text="Выход", command = exit, bg="#B0E0E6", font="Helvetica")  
    
    btn6.place(x=450, y = 540, width=100, height=35)


    
    
    #btn6 = Button(window, text="Отражение", padx=5, pady=5, command =menu_f , bg='#eec6ea')  
    #btn6.pack(anchor="center", padx=20, pady=10)

    #btn4 = Button(window, text="Выход", padx=5, pady=5, command = exit, bg='#eec6ea')  
    #btn4.pack(anchor="center", padx=20, pady=10)

    window.mainloop()

Menu()