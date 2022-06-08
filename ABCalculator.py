# A/B калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
      root.destroy()

def popup_window():
      window = tk.Toplevel()
      window.geometry("280x300")
      window.title("A/B калькулятор")
 
     # Добавление кнопки закрытия программы
      btnClosePopup = tk.Button(window, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command = window.destroy)
      btnClosePopup.place(x = 160, y = 250, width = 90, height = 30)
     
# Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

# Добавление метки заголовка
lblTitle = tk.Label(text = "A/B калькулятор", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x = 55, y = 20)

# Добавление метки заголовка контрольной группы
lblTitle1 = tk.Label(text = "Контрольная группа", font = ('Helvetica', 12, 'bold'), fg = '#0066ff')
lblTitle1.place(x = 25, y = 55)

# Добавление полей ввода контрольной группы
lblVisitors1 = tk.Label(text = "Посетители:", font = ('Helvetica', 10, 'bold'))
lblVisitors1.place(x = 25, y = 85)

entVisitors1 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entVisitors1.place(x = 115, y = 85, width = 90, height = 20)

lblConversions1 = tk.Label(text = "Конверсии:", font = ('Helvetica', 10, 'bold'))
lblConversions1.place(x = 25, y = 115)

entConversions1 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entConversions1.place(x = 115, y = 115, width = 90, height = 20)

# Добавление метки заголовка тестовой группы
lblTitle2 = tk.Label(text = "Тестовая группа", font = ('Helvetica', 12, 'bold'), fg = '#0066ff')
lblTitle2.place(x = 25, y = 145)

# Добавление полей ввода тестовой группы
lblVisitors2 = tk.Label(text = "Посетители:", font = ('Helvetica', 10, 'bold'))
lblVisitors2.place(x = 25, y = 175)

entVisitors2 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entVisitors2.place(x = 115, y = 175, width = 90, height = 20)

lblConversions2 = tk.Label(text = "Конверсии:", font = ('Helvetica', 10, 'bold'))
lblConversions2.place(x = 25, y = 205)

entConversions2 = tk.Entry(font = ('Helvetica', 10, 'bold'))
entConversions2.place(x = 115, y = 205, width = 90, height = 20)

# Добавление кнопки Рассчитать
btnProcess = tk.Button(root, text = "Рассчитать", font = ('Helvetica', 10, 'bold'), command = popup_window)
btnProcess.place(x = 25, y = 250, width = 90, height = 30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x = 160, y = 250, width = 90, height = 30)

# Запуск цикла mainloop
root.mainloop()
