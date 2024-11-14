from customtkinter import *
import random

root = CTk()

root.geometry('400 x 400 + 900 +150')

#def


def cpuMove():
    RandInt = random.random()
    if RandInt < 1 / 3:
        return 'paper'
    elif  RandInt < 2 / 3:
        return 'Rock'
    else:
        return 'Scissors'
    
def UserCpuGame(userMove):
    ComputerMove = cpuMove()
    LabelResult.place(relx=0.1, rely=0.4)

    if userMove == "scissors":

        if ComputerMove == 'paper':
            LabelResult.configure(fg_Color="light green",
                                  text=f' Computer picked :{ComputerMove}  and you picked:{userMove} \n \n you win')
            
        elif ComputerMove == 'Rock':
            LabelResult.configure(fg_color="red",
                                  text=f' Computer picked :{ComputerMove}  and you picked:{userMove} \n \n you lost')
        else:
            LabelResult.configure(fg_color="grey",
                                  text=f' Computer Picked:  {ComputerMove} \n and \n you picked: {userMove} \n tie')

    if userMove == "paper":

        if ComputerMove == "paper":
            LabelResult.configure(fg_color="grey",
                                  text=f' Computer Picked:  {ComputerMove} \n and \n you picked: {userMove} \n tie')
            
        elif ComputerMove == "Rock":
            LabelResult.configure(fg_color="light green",
                                  text=f' Computer picked: {ComputerMove} \n and \n you picked: {userMove} \n you win')
        else:
            LabelResult.configure(fg_color="red",
                                  text=f'Computer picked: {ComputerMove} \n and \n you picked: {userMove} \n you lost')
               
    if userMove == "Rock":

        if ComputerMove == "paper":
            LabelResult.configure(fg_color="red",
                                  text=f'computer picked: {ComputerMove} and  you picked :{userMove} \n \n you lost')
            
        elif ComputerMove == "Rock":
            LabelResult.configure(fg_color="grey",
                                  text=f'Computer Picked: {ComputerMove} and you picked:{userMove} \n tie')
        else:
            LabelResult.configure(fg_Glor="light green",
                                  text=f'computer picked: {ComputerMove} and you picked: {userMove} \n you win')




def RockChoice():
    UserCpuGame("Rock")

def Paperhoice():
    UserCpuGame("paper")   

def ScissorsChoice():
    UserCpuGame("scissors")




# btn

Rockbutton = CTkButton(root, text="Rock", width=50, command=RockChoice)
Rockbutton.place(relx=0.03, rely=0.2)

paperbutton = CTkButton(root, text="paper", width=50, command=Paperhoice)
paperbutton.place(relx=0.35, rely=0.2)

scissorsbutton = CTkButton(root, text="scissors", width=50, command=ScissorsChoice)
scissorsbutton.place(relx=0.67, rely=0.2)


#label

LabelResult = CTkLabel(root,
                       width=200,
                       text_color="black",
                       font=('titr', 14),
                       bg_color="transparent",
                       corner_radius=30
                       )

root.mainloop()