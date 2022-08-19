from tkinter import *
#from tkmacosx import Button

#WINDOW
window = Tk()
window.title("Kilometer/Miles Converter")
window.minsize(250, 100)
window.config()


#LABELS

texto2 = Label(text="")
texto2.grid(column=2, row=1)

texto = Label(text="   is equal to ")
texto.grid(column=0, row=1)

texto4 = Label(text="")
texto4.grid(column=2,row=0)


def converter_miles():
    value = float(number.get())
    value = round(value * 0.62, 2)

    texto3 = Label(text=f"{value}")
    texto3.grid(column=1, row=1)
    texto4.config(text="Km")
    texto2.config(text="Miles")

def converter_km():
    value = float(number.get())
    value = round(value * 1.6, 2)

    texto3 = Label(text=f"{value}")
    texto3.grid(column=1, row=1)
    texto4.config(text="Miles")
    texto2.config(text="Kilometers")



#ENTRIES
number = Entry(width=8)
number.grid(column=1,row=0)

#BUTTONS

#BUTTON 1
calculate_button_miles = Button(text="Kilometers", command=converter_miles, width=7)
calculate_button_miles.grid(column=1,row=2)

#BUTTON 2
calculate_button_km = Button(text="Miles", command=converter_km, width=7)
calculate_button_km.grid(column=1,row=3)



window.mainloop()