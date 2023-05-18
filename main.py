from tkinter import *

FONT = ('Times New Roman', 16)

# the interface
window = Tk()
window.minsize(height=500, width=700)
window.title('Password Manager')
window.config(padx=50, pady=50)



# background image
# canvas = Canvas(width=400, height=400)
# pic = PhotoImage(file='')
# canvas.create_image(200, 125, image=pic)
# canvas.grid(column=, row=)


# inputs
web_name = Label(text="Website : ", font=FONT)
web_name.grid(column=0, row=0)
input = Entry(width=50)
input.grid(column=1, row=0, columnspan=2)

user_name = Label(text='Username/E-mail : ', font=FONT)
user_name.grid(column=0, row=1)
user_input = Entry(width=50)
user_input.grid(column=1, row=1, columnspan=2)

password = Label(text='Password : ', font=FONT)
password.grid(column=0, row=2)
pass_input = Entry(width=27)
pass_input.grid(column=1, row=2)

gen_pass = Button(text='Generate password', font=('TineNewRoman', 10), command='')
gen_pass.config(padx=5)
gen_pass.grid(column=2, row=2)

add_tolist = Button(text='Add', font=('TineNewRoman', 10), width=37)
add_tolist.config(pady=2)
add_tolist.grid(column=1, row=3, columnspan=2)
window.mainloop()