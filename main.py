from customtkinter import *
import random

root = CTk()

root.geometry('400 x 400 + 900 +150')

#def

def Rock():
    pass

def scissors():
    pass

def paper():
    pass


# btn

Rockbutton = CTkButton(root, text="Rock", width=50, command=Rock)
Rockbutton.place(relx=0.03, rely=0.2)

paperbutton = CTkButton(root, text="paper", width=50, command=paper)
paperbutton.place(relx=0.35, rely=0.2)

scissorsbutton = CTkButton(root, text="scissors", width=50, command=scissors)
scissorsbutton.place(relx=0.67, rely=0.2)


root.mainloop()