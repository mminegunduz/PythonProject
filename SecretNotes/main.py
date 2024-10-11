from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet




key= Fernet.generate_key()

fernet= Fernet(key)
def save_and_encrypt():
    title= entry1.get()
    message= entry2.get("1.0",END)
    secret= entry3.get()


    encMessage = fernet.encrypt(message.encode())
    #decMessage = fernet.decrypt(encMessage).decode()

    if len(title) == 0 or len(message)==0 or len(secret) ==0:
        messagebox.showerror(title="Error",message="Please enter all the boxes! ")
    else:
        #encryption
        try:

            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{encMessage.decode()}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{encMessage.decode()}")
        finally:
            entry1.delete(0,END)
            entry3.delete(0,END)
            entry2.delete("1.0",END)



def decrypt():
    encryptedMessage= entry2.get("1.0",END)
    secret= entry3.get()


    if len(encryptedMessage)==0 or len(secret) == 0:
        messagebox.showerror(title="Error!",message="Please enter two boxes!")
    else:
        decryptedMessage= fernet.decrypt(encryptedMessage.encode()).decode()
        entry2.delete("1.0",END)
        entry2.insert("1.0",decryptedMessage)






window= Tk()
window.title("Secret Notes")
window.minsize(width=500,height=600)
window.config(padx=20,pady=20)
window.geometry("200x200")





img=PhotoImage(file="C:\\Users\\DELL\\OneDrive\\Resimler\\secret.png")
Label(window,image=img).pack()


label1= Label(text="Enter your title",font=('Arial',15,"bold"))
label1.pack()

entry1= Entry(width=50)
entry1.pack()

label2= Label(text="Enter your secret text",font=('Arial',15,"bold"))
label2.pack()

entry2=Text(window,width=50,height=15)
entry2.pack()

label3=Label(text="Enter master key",font=('Arial',15,"bold"))
label3.pack()


entry3 = Entry(width=50)
entry3.pack()

button1= Button(text="Save & Encrypt",font=("Arial",10),command=save_and_encrypt)
button1.pack()

button2 = Button(text="Descript",font=("Arial",10),command=decrypt)
button2.pack()

window.mainloop()
