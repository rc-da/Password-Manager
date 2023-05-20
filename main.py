from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ('Times New Roman', 16)

# the interface
window = Tk()
window.minsize(height=400, width=600)
window.title('Password Manager')
window.config(padx=50, pady=50)

# saving the datas to the file
def add_to_file():
    website = web_input.get()
    user_mail = user_input.get()
    passwords = pass_input.get()

    if len(website)!=0 and len(user_mail)!=0 and len(passwords)!=0:
        to_save = messagebox.askyesno(title='You sure!', message=f'Do u want to save these details ?\n Website : {website}\n Mail : {user_mail}\n Password : {passwords}')
        
        if to_save:
            with open('pass.txt', 'a') as file:
                file.write(f'\n{website} | {user_mail} | {passwords}')
            web_input.delete(0, END)
            user_input.delete(0, END)
            pass_input.delete(0, END)

    else:
        messagebox.showerror(title='Error', message='Some details are empty!')

# to generate passwords
def to_gen_pass():  
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    pass_letter = [random.choice(letters) for i in range (5)]
    pass_symb = [random.choice(symbols) for i in range (2)]
    pass_no = [random.choice(numbers) for i in range (3)]
    pass_list = pass_letter + pass_symb + pass_no
    random.shuffle(pass_list)
    gen_password = "".join(pass_list)

    pass_input.delete(0, END)
    pass_input.insert(END, gen_password)
    # this code copied the generated password to clipboard
    pyperclip.copy(gen_password)


# background image
canvas = Canvas(width=200, height=200)
pic = PhotoImage(file='lock-logo.png')
canvas.create_image(102, 102,image=pic)
canvas.grid(column=1, row=0)


# inputs
web_name = Label(text="Website : ", font=FONT)
web_name.grid(column=0, row=1)
web_input = Entry(width=50)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

user_name = Label(text='Username/E-mail : ', font=FONT)
user_name.grid(column=0, row=2)
user_input = Entry(width=50)
user_input.grid(column=1, row=2, columnspan=2)

password = Label(text='Password : ', font=FONT)
password.grid(column=0, row=3)
pass_input = Entry(width=27)
pass_input.grid(column=1, row=3)

gen_pass = Button(text='Generate password', font=('TineNewRoman', 10), command=to_gen_pass)
gen_pass.config(padx=5)
gen_pass.grid(column=2, row=3)

add_tolist = Button(text='Add', font=('TineNewRoman', 10), width=37, command=add_to_file)
add_tolist.config(pady=2)
add_tolist.grid(column=1, row=4, columnspan=2)
window.mainloop()