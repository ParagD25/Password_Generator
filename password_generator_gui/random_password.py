from tkinter import *
import random
import string

password_window=Tk()
password_window.title('Random Password Generator')
password_window.geometry('375x370')

icon=PhotoImage(file="pass_icon.png")
password_window.iconphoto(False,icon)

bg_img=PhotoImage(file="home.png")
home_canvas=Canvas(password_window,width=370,height=375) 
home_canvas.pack(fill="both",expand=True)
home_canvas.create_image(0,0,image=bg_img,anchor="nw")

def next_window():
    main_window=Toplevel()
    main_window.title('Generate Password')
    main_window.geometry('375x370')
    icon=PhotoImage(file="pass_icon.png")
    main_window.iconphoto(False,icon)
    main_window.config(background='white')

    def generate_password():
        upper=string.ascii_uppercase
        lower=string.ascii_lowercase
        special=string.punctuation
        digit=string.digits
        password=[]
        password.extend(list(upper))
        password.extend(list(lower))
        password.extend(list(special))
        password.extend(list(digit))

        pass_len = len_e.get()
        pass_num= num_e.get()
        all_password=[]

        try:
            pass_len=int(pass_len)
            pass_num=int(pass_num)
            for val in range(pass_num):
                random.shuffle(password)
                mypass=(('').join(password[:pass_len]))
                all_password.append(mypass)
            
            pass_list.delete(0,END)
            num=1
            for data in all_password:
                if len(all_password)==1:
                    pass_list.insert(END,f'Password --> {data}')
                else:
                    pass_list.insert(END,f'Password {num} --> {data}')
                    num+=1

                
        except:
            pass_list.delete(0,END)
            pass_list.insert(END,'Enter Numeric Value only')

    len_lbl=Label(main_window,text="Enter Length of Password : ",background='white',font='Helvetica 9 bold')
    num_lbl=Label(main_window,text="Enter Number of Password : ",background='white',font='Helvetica 9 bold')
    len_var=StringVar()
    len_e=Entry(main_window,bd=3,relief='groove',textvariable=len_var)
    num_var=StringVar()
    num_e=Entry(main_window,bd=3,relief='groove',textvariable=num_var)
    btn_create=Button(main_window,text='Create Password',bg='black',fg='white',activeforeground="#23F32D",activebackground='black',width=15,font='Helvetica 8',command=generate_password)
    pass_list=Listbox(main_window,bd=3,relief='groove',font='Helvetica 12 bold',height=5,width=34)
    btn_close=Button(main_window,text='Close',bg='black',fg='white',activeforeground="#FF0E0E",activebackground='black',width=15,font='Helvetica 8',command=main_window.destroy)

    len_lbl.place(x=25,y=40)
    num_lbl.place(x=25,y=90)
    len_e.place(x=200,y=40)
    num_e.place(x=200,y=90)
    btn_create.place(x=135,y=145)
    pass_list.place(x=30,y=185)
    btn_close.place(x=135,y=325)

create_btn=Button(password_window,text="Create",font="Helvetica 10 bold",padx=10,background='black',foreground='white',activebackground='black',activeforeground='#0EBDFF',command=next_window)
btn_window=home_canvas.create_window(150,315,anchor="nw",window=create_btn)

password_window.mainloop()