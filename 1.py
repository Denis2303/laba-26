import tkinter as tk

def add_digit(digit):
    a = calc.get()
    if digit == 'С':
        calc.delete(0,tk.END)
        return
    elif a == "Лишний оператор" or a == "Ошибка: деление на 0":
        calc.delete(0,tk.END)
    elif len(a) > 0:
        if a[-1] in '+-/*^' and str(digit) in "+-/*^":
            a = a[:-1]
            a += digit
            calc.delete(0,tk.END)
            calc.insert(0, a)
            return
    calc.insert(tk.END, str(digit))


def ravn():
    a = calc.get()
    calc.delete(0,tk.END)
    i = 0
    if a.count("/0") > a.count("/0."):
            calc.delete(0, tk.END)
            calc.insert(0,"Ошибка: Деление на 0")
            return
    elif a[-1] in '-+/*^':
        calc.insert(0,"Лишний оператор")
    else:
        while "^" in a:
            if a[i] == '^':
                b = a[:i]+'**'+a[i+1:]
                a = b
            i+=1
        q = eval(a)
        if q % 1 == 0:
            calc.insert(0, int(q))
        else:
            calc.insert(0,q)

def new_button(digit):
    digit = str(digit)
    return tk.Button(text = digit, bd = 5, font = ('Arial', 30) , command = lambda : add_digit(digit))

def new_buttonС(digit):
    digit = str(digit)
    return tk.Button(text = "С", bd = 5,fg = 'red', font = ('Arial', 30) , command = lambda : add_digit(digit))

win = tk.Tk()
win.title("Калькулятор") #смена имени
win.config(bg='#00b5f7') #фон
win.geometry("480x530+800+250")
win.resizable(False, False) #изменение размера

calc = tk.Entry(win, justify = tk.RIGHT, font = ("Arial", 30), width = 15, bd = 5)
calc.grid(row = 0, column = 0,columnspan = 6, stick ='we', padx=5)

new_button( '+').grid(row = 1, column = 0, stick = "wens", padx = 5, pady = 5)
new_button( '-').grid(row = 1, column = 1, stick = "wens", padx = 5, pady = 5)
new_button( '*').grid(row = 1, column = 2, stick = "wens", padx = 5, pady = 5)
new_button( '1').grid(row = 2, column = 0, stick = "wens", padx = 5, pady = 5)
new_button( '2').grid(row = 2, column = 1, stick = "wens", padx = 5, pady = 5)
new_button( '3').grid(row = 2, column = 2, stick = "wens", padx = 5, pady = 5)
new_button( '4').grid(row = 3, column = 0, stick = "wens", padx = 5, pady = 5)
new_button( '5').grid(row = 3, column = 1, stick = "wens", padx = 5, pady = 5)
new_button( '6').grid(row = 3, column = 2, stick = "wens", padx = 5, pady = 5)
new_button( '7').grid(row = 4, column = 0, stick = "wens", padx = 5, pady = 5)
tk.Button(text = '=', bd = 5, font = ('Arial', 30), command = lambda : ravn()).grid(row = 4, column = 3, stick = "wens", padx = 5, pady = 5)
new_button('^').grid(row = 2, column = 3, stick = "wens", padx = 5, pady = 5)
new_button('.').grid(row = 3, column = 3, stick = "wens", padx = 5, pady = 5)
new_button('8').grid(row = 4, column = 1, stick = "wens", padx = 5, pady = 5)
new_button("9").grid(row = 4, column = 2, stick = 'wens', padx = 5, pady = 5)
new_button('/').grid(row = 1, column = 3, stick = 'wens', padx = 5, pady = 5)
new_button('(').grid(row = 5, column = 0, stick = 'wens', padx = 5, pady = 5)
new_button(')').grid(row = 5, column = 1, stick = 'wens', padx = 5, pady = 5)
new_button('0').grid(row = 5, column = 2, stick = 'wens', padx = 5, pady = 5)
new_buttonС('С').grid(row = 5, column = 3, stick = 'wens', padx = 5, pady = 5)

win.grid_columnconfigure(0, minsize=120)
win.grid_columnconfigure(1, minsize=120)
win.grid_columnconfigure(2, minsize=120)
win.grid_columnconfigure(3, minsize=120)
win.grid_columnconfigure(3, minsize=120)
win.grid_rowconfigure(1,minsize = 80)
win.grid_rowconfigure(2,minsize = 80)
win.grid_rowconfigure(3,minsize = 80)
win.grid_rowconfigure(4,minsize = 80)
win.grid_rowconfigure(5,minsize = 80)

win.mainloop()