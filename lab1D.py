import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import Tk
from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style
from tkinter import messagebox
from PIL import *
from tkinter import ttk



if __name__ == '__main__':
    def nothing(*arg):
        pass

class Image(Frame):
    
    def settings(self):

        def show_message():
            
            self.value1 = int(entry.get())

            self.value2 = int(entry1.get())

            self.value3 = int(entry2.get())

            self.canny_()


        root = Tk()
        root.title("Настройки")
        root.geometry("280x280") 

        lbl = Label(root, text = "Canny min")
        lbl.pack(anchor=CENTER, padx=6, pady=6)
        
        entry = Entry(root)
        entry.pack(anchor=CENTER, padx=6, pady=6)

        lbl1 = Label(root, text = "Canny max")
        lbl1.pack(anchor=CENTER, padx=6, pady=6)

        entry1 = Entry(root)
        entry1.pack(anchor=CENTER, padx=6, pady=6)

        lbl2 = Label(root, text = "CellShading index")
        lbl2.pack(anchor=CENTER, padx=6, pady=6)

        entry2 = Entry(root)
        entry2.pack(anchor=CENTER, padx=6, pady=6)
        
        btn = Button(root, text="Click", command=show_message)
        btn.pack(anchor=CENTER, padx=6, pady=6)
        
        
        root.mainloop()

    def canny_(self):
        img = cv2.imread("Bleach.jpg", cv2.IMREAD_COLOR)
        img1 = cv2.imread("Bleach.jpg", cv2.IMREAD_COLOR)

        min, max, index = self.value1, self.value2, self.value3

        width = img.shape[0]
        height  = img.shape[1]

        canny_img = cv2.Canny(img, min, max)



        for k in range (3):
                for i in range(width):
                    for j in range(height):
                        
                        color = img1[i, j, k]
                            
                        if color<=50:
                            color = 0+index
                        elif color<=100:
                            color = 25+index
                        elif color<=150:
                            color = 180+index
                        elif color<=200:
                            color = 210+index
                        else:
                            color = 255
                        
                        img1[i, j, k] = color
                        img1[i,j] = img1[i,j] - canny_img[i,j]    

        cv2.startWindowThread()
        cv2.imshow("canny", canny_img)
        cv2.imshow("cellShading", img1)
        cv2.waitKey(0)


    def Video(self):
        
        messagebox.showinfo("Предупреждение", "Для закрытия окон видео, необходимо сначала закрыть окно настроек или дождаться конца видео")
    
        cap = cv2.VideoCapture('coffee.mp4')
        cv2.namedWindow( "settings" ) # создаем окно настроек
        cv2.resizeWindow("settings", 400, 250)

        percent = 20    
        cv2.createTrackbar('h1', 'settings', 50, 255, nothing)
        cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
        cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
        cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
        cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
        cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
        crange = [0,0,0, 0,0,0]

        

        if(cap.isOpened() == False):
            label = Label("", text = "Ошибка при чтении видеофайла")
            label.pack
        else:
            while cap.isOpened():
                ret, frame = cap.read()

                width = int(frame.shape[1] * percent / 100) 
                height = int(frame.shape[0] * percent / 100) 

                dim = (width, height)
                frame_re = cv2.resize(frame, dim)

                

                # считываем значения бегунков
                h1 = cv2.getTrackbarPos('h1', 'settings')
                #h1.style()
                s1 = cv2.getTrackbarPos('s1', 'settings')
                v1 = cv2.getTrackbarPos('v1', 'settings')
                h2 = cv2.getTrackbarPos('h2', 'settings')
                s2 = cv2.getTrackbarPos('s2', 'settings')
                v2 = cv2.getTrackbarPos('v2', 'settings')

                # формируем начальный и конечный цвет фильтра
                h_min = np.array((h1, s1, v1), np.uint8)
                h_max = np.array((h2, s2, v2), np.uint8)

                thresh = cv2.inRange(frame_re, h_min, h_max)

                cv2.imshow('result', thresh)
                cv2.imshow('Look', frame_re)



                if cv2.waitKey(40) == 27 & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

    def Web(self):
        
        messagebox.showinfo("Предупреждение", "Для закрытия окон видео, необходимо сначала закрыть окно настроек")
    
        cap = cv2.VideoCapture(0)
        cv2.namedWindow( "settings" ) # создаем окно настроек
        cv2.resizeWindow("settings", 400, 250)

        percent = 80   
        cv2.createTrackbar('h1', 'settings', 110, 255, nothing)
        cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
        cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
        cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
        cv2.createTrackbar('s2', 'settings', 190, 255, nothing)
        cv2.createTrackbar('v2', 'settings', 180, 255, nothing)
        crange = [0,0,0, 0,0,0]

        

        if(cap.isOpened() == False):
            label = Label("", text = "Ошибка при чтении видеофайла")
            label.pack
        else:
            while cap.isOpened():
                ret, frame = cap.read()

                width = int(frame.shape[1] * percent / 100) 
                height = int(frame.shape[0] * percent / 100) 

                dim = (width, height)
                frame_re = cv2.resize(frame, dim)

                

                # считываем значения бегунков
                h1 = cv2.getTrackbarPos('h1', 'settings')
                #h1.style()
                s1 = cv2.getTrackbarPos('s1', 'settings')
                v1 = cv2.getTrackbarPos('v1', 'settings')
                h2 = cv2.getTrackbarPos('h2', 'settings')
                s2 = cv2.getTrackbarPos('s2', 'settings')
                v2 = cv2.getTrackbarPos('v2', 'settings')

                # формируем начальный и конечный цвет фильтра
                h_min = np.array((h1, s1, v1), np.uint8)
                h_max = np.array((h2, s2, v2), np.uint8)

                thresh = cv2.inRange(frame_re, h_min, h_max)

                cv2.imshow('result', thresh)
                cv2.imshow('Look', frame_re)



                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()    





def Menu():
    window = Tk()
    window.title("Lab1")

    image = Image()

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('600x400+{}+{}'.format(w, h))
    window.config(background="#D2B48C")

    btn = Button(window, text="Обработка фото", command = image.settings, bg="#B0E0E6", font="Helvetica" )  
    
    btn.place(x=150, y = 130, width=300, height=50)

    btn1 = Button(window, text="Обработка видео", command = image.Video, bg="#B0E0E6", font="Helvetica")  
   
    btn1.place(x=150, y = 200, width=300, height=50)

    btn2 = Button(window, text="Вывод видео с веб-камеры",command = image.Web, bg="#B0E0E6", font="Helvetica")  
    
    btn2.place(x=150, y = 60, width=300, height=50)

    btn3 = Button(window, text="Выход", command = exit, bg="#B0E0E6", font="Helvetica")  
    
    btn3.place(x=225, y = 300, width=150, height=50)

    window.mainloop()

Menu()