from Tkinter import *
from ttk import *

app = Tk()
app.geometry('200x100')

labelTop = Label(app,
                    text="Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = Combobox(app, state="readonly",
                            values=[
                                "January",
                                "February",
                                "March",
                                "April"])

comboExample.grid(column=0, row=1)
# set the currently selected element to the third item in the list
comboExample.current(2)

# print the index of currently selected item
print comboExample.current()

# print the text of currently selected item
print comboExample.get()

app.mainloop()