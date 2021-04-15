from tkinter import *
from tkinter import Button

mult = 1
num_toshow = 0
N = 0
# початкове значення
after_id = 0


# збільшення на 1 кожну секунду
def tick():
    global num_toshow, after_id, mult
    if num_toshow > N:
        root.after_cancel(after_id)
        btn1.grid(row=1, columnspan=2, sticky="ew")
        btn2.grid_forget()
    else:
        after_id = root.after(1000, tick)
        label1.configure(text=str(num_toshow))
        num_toshow += 2
        label2.configure(text=str(mult))
        mult *= num_toshow


# запуск підрахунку
def start_sw():
    get_N()
    btn1.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky="ew")
    tick()


# зупинити підрахунок
def stop_sw():
    btn2.grid_forget()
    btn3.grid(row=1, columnspan=2, sticky="ew")
    btn4.grid(row=2, columnspan=2, sticky="ew")
    root.after_cancel(after_id)


# продовжити підрахунок
def continue_sw():
    btn3.grid_forget()
    btn4.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky="ew")
    tick()


# обнулити підрахунок
def reset_sw():
    global num_toshow, mult
    num_toshow = 0
    mult = 1
    label1.configure(text="0")
    label2.configure(text="0")
    btn3.grid_forget()
    btn4.grid_forget()
    btn1.grid(row=1, columnspan=2, sticky="ew")

def get_N(): 
    global N
    try:
        a = int(entry_a.get())
        N = a
        print(N)
    except ValueError as e:
        print(e)

# створення порожнього вікна
root = Tk()
root.geometry('1000x600')
# назва вікна
root.title("Лабораторна робота 4 Нижник О.О. КН-3-2")
label1: Label = Label(root, width=10, font=("Ubuntu", 50), text='0')
label1.grid(row=0, columnspan=2)
label2: Label = Label(root, width=10, font=("Ubuntu", 50), text='0')
label2.grid(row=5, columnspan=3)
label_w: Label = Label(root, font=("Ubuntu", 30), text='Введіть кінцеве значення:')
label_w.place(x=0, y=300)

entry_a = Entry(root, font=("Ubuntu", 30))
entry_a.place(x=500, y=300)

# створення кнопок стану підрахунку
btn1 = Button(root, text="Пуск", font=("Ubuntu", 30) )
btn1.bind('<Button-1>', lambda event: start_sw())
btn2 = Button(root, text="Стоп", font=("Ubuntu", 30), command=stop_sw)
btn3 = Button(root, text="Продовжити", font=("Ubuntu", 30))
btn3.bind('<Button-1>', lambda event: continue_sw())
btn4: Button = Button(root, text="Скинути", font=("Ubuntu", 30), command=reset_sw)

# відображення кнопки на формі
btn1.grid(row=1, columnspan=2, sticky="ew")

# відобразити вікно
root.mainloop()
