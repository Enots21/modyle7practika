import tkinter as tk  # importa tkinter
from tkinter import filedialog  # importa filedialog
from tkinter import messagebox as mb  # importa messagebox

info = (  # создаем переменную c информацией
    'Приложение сделано на Python 3.8.5\nВ этом приложении вы можете выбрать файл и ответить на вопросы.'
    '\n\nВыберите файл и нажмите ОК'
)

about = (  # создаем переменную c информацией
    'Разработано на Python 3.8.5\nРазработал автор Pepsi'
)


def check():  # функция massegebox
    mb.askyesno(title="Вопрос", message=str(info))


def checks():  # функция massegebox
    mb.askyesno(title="Вопрос", message=str(about))


def select_file():  # функция которая открывает файл и показывает его путь
    filename = filedialog.askopenfilename(initialdir='/', title="Файловая система",
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '.*')))  # выбор файла

    text['text'] = text['text'] + '\n' + filename# добавляем путь в текст


window = tk.Tk() # создаем окно

menubar = tk.Menu() # создаем меню

menubar.add_cascade(label="info", command=check) # добавляем кнопку info
menubar.add_cascade(label="about", command=checks) # добавляем кнопку about

SCREEN_WIDTH = window.winfo_screenwidth()  # ширина экрана
SCREEN_HEIGHT = window.winfo_screenheight()  # высота экрана

w_window = SCREEN_WIDTH // 2  # ширина окна по середине экрана
h_window = SCREEN_HEIGHT // 2  # высота окна по середине экрана

window.title("Проводник")
window.geometry(f'350x350+{w_window}+{h_window}')  # ширина и высота окна
window.resizable(False, False)  # разрешить изменение размера окна
text = tk.Label(window, text="Файл:", height=3, width=35, background="silver", anchor="w")  # клавиатура
text.grid(row=0, column=0)# position
button_select = tk.Button(window, text="Выбрать файл", height=3, width=13, background="silver",# кнопка
                          command=select_file)  # кнопка
button_select.grid(column=2, row=0)  # position

window.config(menu=menubar)# меню
window.mainloop()  # запуск окна
