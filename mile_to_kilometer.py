from tkinter import *
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20 , pady = 20 )
def result_func():
    data = float(miles_input.get())
    num = data * 1.609
    kilometer_result_label.config(text = f"{num}")
miles_input = Entry(width=7)
miles_input.grid(column = 1, row = 0)
miles_label = Label(text = "miles")
miles_label.grid(column = 2, row = 0)
is_equal_label = Label(text = "is equal to")
is_equal_label.grid(column = 0, row = 1)
kilometer_result_label = Label(text = "0")
kilometer_result_label.grid(column = 1, row = 1)
kilometer_label = Label(text = "km")
kilometer_label.grid(column = 2, row = 1)
calculate_button = Button(text = "calculate" , command = result_func)
calculate_button.grid(column = 1, row = 2)















window.mainloop()