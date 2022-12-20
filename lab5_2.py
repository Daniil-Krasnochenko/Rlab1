import cv2
import pytesseract
from tkinter import *


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def Text():
    img = cv2.imread("test.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(img, 100, 1000, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(binary, lang="eng", config="--oem 3 --psm 6")
    print(text)

    config = r'--oem 3 --psm 6'
    data = pytesseract.image_to_data(img, config=config)

    # Перебираем данные про текстовые надписи
    for i, el in enumerate(data.splitlines()):
        if i == 0:
            continue

        el = el.split()
        try:
            # Создаем подписи на картинке
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        except IndexError:
            continue
            #print("Операция была пропущена")

    cv2.imshow('output.png', img)
    cv2.waitKey(0)


def Face():

# создать новый объект камеру
    cap = cv2.VideoCapture(0)
    # инициализировать поиск лица (по умолчанию каскад Хаара)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    while True:
        # чтение изображения с камеры
        _, image = cap.read()
        # преобразование к оттенкам серого
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # обнаружение лиц на фотографии
        faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)
        # для каждого обнаруженного лица нарисовать синий квадрат
        for x, y, width, height in faces:
            cv2.rectangle(image, (x, y), (x + width, y + height), color=(0, 255, 255), thickness=2)
        cv2.imshow("image", image)
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

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

    btn = Button(window, text="Нахождение лица", padx=10, pady=7, command =Face, bg='#ffe900')  
    btn.place(x = 50, y = 50, height= 60, width=200)

    btn2 = Button(window, text="Нахождение текста", padx=10, pady=7, command =Text, bg='#ffe900')  
    btn2.place(x = 300, y = 50, height= 60, width=200)

    btn1 = Button(window, text="Выход", padx=10, pady=7, command =exit, bg='#ffe900')  
    btn1.place(x = 500, y = 150, height= 30, width=80)
    


    window.mainloop()

Menu()

