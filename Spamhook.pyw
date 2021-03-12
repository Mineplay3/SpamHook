from tkinter import * 
import json
import requests
import asyncio

root = Tk()
root.attributes('-topmost', True)
root.geometry('400x400')
root.resizable(False, False)

async def send():
    usernam = username.get()

    print(usernam)

    if usernam == None:
        usernam = "Spamhook"

    json = {
        'username': usernam,
        'content': message.get()
    }
    a = 0

    while a <= amount.get():
        root.update()  
        pog = requests.post("https://discord.com/api/v8/webhooks/819653001236971541/L9tsN3qft4sbb1NuVEoLFGMpsfDohpBstf03n31ohJGr-yJ_K7a2vQ2jYoQyBMQLHDMI?wait=false", json=json)
        root.update()
        a +=1
        status = Label(root, text=a)
        status.grid(row=3, column=0, columnspan=2)
        root.update()

        

def starter():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send())


root.title("SpamHook")
root.configure(background="#36393f")
webhook = Entry(root)
webhook.grid(row=1, column=1, columnspan=1)

message = Entry(root)
message.grid(row=1, column=2, columnspan=1)

username = Entry(root)
username.grid(row=1, column=3, columnspan=1)

amount = Scale(root, from_=1, to=300, orient=HORIZONTAL, background="#36393f", showvalue=1)
amount.grid(row=1, column=4, columnspan=1)

amount.set(1)

delay = Scale(root, from_=10, to=3000, orient=HORIZONTAL, background="#36393f", showvalue=1)
delay.grid(row=1, column=5, columnspan=1)
delay.set(10)

start = Button(root, text="Spam", command=starter, borderwidth=0, background="#36393f")
start.grid(row=1, column=2, columnspan=1)
img1 = PhotoImage(file="Images/spam.png")
start.config(image=img1)

close = Button(root, text="Close", command=root.destroy, borderwidth=0, background="#36393f")
close.grid(row=2, column=2, columnspan=1)

def clear():
    amount.set(1)
    delay.set(10)
    webhook.delete(0, 'end')
    message.delete(0, 'end')
    username.delete(0, 'end')

clear = Button(root, text="Clear", command=clear, background="#43b581")
clear.grid(row=3, column=2, columnspan=2)

root.mainloop()