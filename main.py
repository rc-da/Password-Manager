from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ('Times New Roman', 16)

# the interface
window = Tk()
window.minsize(height=400, width=550)
window.title('Password Manager')
window.config(padx=50, pady=50)

# saving the datas to the file
def add_to_file():
    website = web_input.get().lower()
    user_mail = mail_input.get()
    passwords = pass_input.get()
    pass_data = {website:{'email' : user_mail,'password' : passwords}}
    if len(website)!=0 and len(user_mail)!=0 and len(passwords)!=0:
        to_save = messagebox.askyesno(title='You sure!', message=f'Do u want to save these details ?\n Website : {website}\n Mail : {user_mail}\n Password : {passwords}')
        
        if to_save:
            try:
                with open('pass.json', 'r') as file:
                    data = json.load(file)
                    data.update(pass_data)

                with open('pass.json', 'w') as file:
                    json.dump(data, file, indent=4)

            except:
                with open('pass.json', 'w') as file:
                    json.dump(pass_data, file, indent=4)
            finally:
                web_input.delete(0, END)
                mail_input.delete(0, END)
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

# to search password
def search_passw():
    website = web_input.get().lower()
    try:
        with open('pass.json', 'r') as file:
            p_data = json.load(file)
            messagebox.showinfo(title=website, message='E-mail : '+p_data[website]['email']+'\nPassword : '+p_data[website]['password'])
    except:
        messagebox.showerror(message='There is no such website saved !')
# background image
canvas = Canvas(width=200, height=200)
pic = PhotoImage(file='lock-logo.png')
canvas.create_image(102, 102,image=pic)
canvas.grid(column=1, row=0)


# inputs
web_name = Label(text="Website : ", font=FONT)
web_name.grid(column=0, row=1)
web_input = Entry(width=30)
web_input.grid(column=1, row=1)
web_input.focus()

pass_search = Button(text='Search', command=search_passw)
pass_search.grid(column=2, row=1)
pass_search.config(padx=38)

mail_id = Label(text='E-mail : ', font=FONT)
mail_id.grid(column=0, row=2)
mail_input = Entry(width=30)
mail_input.grid(column=1, row=2)

password = Label(text='Password : ', font=FONT)
password.grid(column=0, row=3)
pass_input = Entry(width=30)
pass_input.grid(column=1, row=3)

gen_pass = Button(text='Generate password', font=('TineNewRoman', 10), command=to_gen_pass)
gen_pass.config(padx=3)
gen_pass.grid(column=2, row=3)

add_tolist = Button(text='Add', font=('TineNewRoman', 10), width=37, command=add_to_file)
add_tolist.config(pady=2, padx=10)
add_tolist.grid(column=1, row=4, columnspan=2)
window.mainloop()