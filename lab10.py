# 1. вывести главное окно по центру
# 2. отключить от него resize
# 3. после главной кнопки появляется три новые кнопки ( через toplevel)
# фейерверк у главного окна по кнопке. еще кнопка которая отключает
# через 15, 30, 45 секунд с обратным отсчетом.
# через  это время фейерверк заканчивается, форма закрывается

from tkinter import*
root = Tk()
#form = Toplevel
width = 350
height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))
root.geometry(str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y))
root.title("lab10")
button = Button(root, height = 1, width = 7, text = "Старт", command = lambda: click_button(button))
root.resizable(False, False)
root.mainloop()
