from tkinter import *

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
    main_window.title('View all Books')
    main_window.geometry('375x370')
    icon=PhotoImage(file="pass_icon.png")
    main_window.iconphoto(False,icon)

    len_lbl=Label(main_window,text="Enter Length of Password : ")
    num_lbl=Label(main_window,text="Enter Number of Passwords : ")
    len_e=Entry(main_window)
    num_e=Entry(main_window)
    
    len_lbl.place(x=25,y=40)
    num_lbl.place(x=25,y=90)
    len_e.place(x=200,y=40)
    num_e.place(x=200,y=90)

create_btn=Button(password_window,text="Create",font="Helvetica 10 bold",padx=10,background='black',foreground='white',command=next_window)
btn_window=home_canvas.create_window(150,315,anchor="nw",window=create_btn)

password_window.mainloop()