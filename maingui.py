from tkinter import *
from tkinter import messagebox
import lotteri

lotter = lotteri.Lotteri()

root = Tk()
root.title("Lotteri")

root.geometry("380x300")

label_antal = Label(root,
                    text="Antal lotter, max 3 st!")
label_antal.grid(row=0,
                 column=0,
                 sticky=W,
                 padx=5,
                 pady=5)

textbox_antal = Entry(root,
                      width=2)
textbox_antal.grid(row=0,
                   column=1,
                   sticky=W,
                   padx=5,
                   pady=5)
textbox_antal.focus_set()

def update_listBox(antal_lotter):
    listbox.delete(0,
                   END)
    listbox.insert(1,
                   "Grattis! Du har vunnit detta:")
    
    try:
        int_antal_lotter = int(antal_lotter)
        i=0

        if (int_antal_lotter <=3):
            while i < int_antal_lotter+1:
                vinst = lotter.get_vinst()
                listbox.insert((i+2),
                                vinst)
                i += i+1
        
        else:
            messagebox.showinfo("Du har valt för många lotter! MAX 3 ST")

    except ValueError:
        messagebox.showinfo("Endast siffror tillåtna!")

def clickSlumpaButton():
    antal_lott = textbox_antal.get()
    textbox_antal.delete(0,
                         END)
    textbox_antal.focus_set()

    update_listBox(antal_lott)

button_slumpa = Button(text="I'm feeling lucky",
                       command=clickSlumpaButton)
button_slumpa.grid(row=1,
                   column=0,
                   sticky=W,
                   padx=15,
                   pady=13)

listbox = Listbox(root, 
                  height=4,
                  width=30,
                  bg="white",
                  activestyle='dotbox',
                  font="Arial",
                  fg="crimson")

listbox.grid(row=2,
             column=0,
             padx=14,
             pady=15)

root.mainloop()