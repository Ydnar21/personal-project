import PySimpleGUI as sg
from tkinter import simpledialog
username= ""
password= ""


def login_window():
    window = sg.Window(title= "Investment Portfolio", layout=[
        [sg.Text("This is your Investment Porfolio Picker")],
        [sg.Text("Enter Username", size =(15,1)),sg.InputText(key='username')],
        [sg.Text("Enter Password", size = (15,1)),sg.InputText(key='password',password_char = '*')],
        [sg.Button("Login")],
        [sg.Button("Login", visible= False, bind_return_key=True)]], margins=(300,300)).read()
    while True:
        event, values = window
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        else:
            username = values['username']
            password = values['password']

            if username == "Randy":
                if password == "cool":
                    print("Login successfull")
                    #Do something that logs in. Make a new page get directed to something else but just need something
                else:
                    login_window()
            
            else:
                login_window()

            # check it out
            #username = values['username']
            #password = values['password']
            #this should be a log in feature to an account 
            break
    sg.Exit()

def login():
    pass
def main():
    login_window()







if __name__ =='__main__':
    main()