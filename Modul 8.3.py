import tkinter
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

def sett():
    global t
    rem=sd.askstring("Время напоминания",
                     "Введите время напоминания  формате ЧЧ:ММ")
    if rem:
        try:
            hour=int((rem.split(":")[0]))
            minute=int((rem.split(":")[1]))
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            t=dt.timestamp()
            print(t)
            label.config(text=f"Напоминание установлено на {hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Ошибка","Неверный формат времени")
        except Exception as e:
            print(e)


def check():
    global t
    if t:
        now=time.time()
        print(now)
        if now>=t:
            play_snd()
            tkinter.messagebox.showinfo(title="Напоминание", message="Сработал таймер")
            t=None
    window.after(10000, check)


def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("rem.mp3")
    pygame.mixer.music.play(-1)

def stop_snd():
    pygame.mixer.music.stop()
    tkinter.messagebox.showinfo(title="Таймер остановлен", message="Таймер остановлен")

window=Tk()
window.title("Напоминание со звуком")

label=Label(text="Установите напоминание", font=("Courier",20))
label.pack(pady=20)

button=Button(text="Установить", font=("Courier",20), command=sett)
button.pack(pady=20)
button_stop=Button(text="Остановить музыку", font=("Courier",15), command=stop_snd)
button_stop.pack(pady=20)

t=None
check()

window.mainloop()