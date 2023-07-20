from tkinter import Tk,Label,Entry,Button,Listbox,N,S,E,W,END,StringVar,Frame,messagebox
import tkinter as tk
from random import randint

window = tk.Tk()
window.title(f'Guess Number Game')

window.configure(bg='light blue')
window.geometry('550x430')
window.resizable(width=False,height=False)

#global variable num_list
num_list = []


def start():
    #the global keyword is used to change the value of a global variable from empty list to a list of three numbers
    global num_list
    num_list = [randint(0,9),randint(0,9),randint(0,9)]
    first_ent.delete(0,tk.END)
    second_ent.delete(0,tk.END)
    third_ent.delete(0,tk.END)
    list_box.delete(0,tk.END)


def chek_num():
    list_box.delete(0,tk.END)
    txt_1 = first_text.get()
    txt_2 = second_text.get()
    txt_3 = third_text.get()
    lbl_1a = 'First Number: {} is correct'.format(txt_1)
    lbl_1b = 'First Number: {} is not correct'.format(txt_1)
    lbl_2a = 'Second Number: {} is correct'.format(txt_2)
    lbl_2b = 'Second Number: {} is not correct'.format(txt_2)
    lbl_3a = 'Third Number: {} is correct'.format(txt_3)
    lbl_3b = 'Third Number: {} is not correct'.format(txt_3)

   #if number fields are not empty
    if txt_1 !='' and txt_2 !='' and txt_3 !='':
        #if num_list is empty
        if num_list == []:
            messagebox.showerror(title='Error',message='You must click the start button to begin')
        else:
            if int(txt_1) == int(num_list[0]) and int(txt_2) == int(num_list[1]) and int(txt_3) == int(num_list[2]):
                list_box.insert(0,f'Congrats!!!')
                list_box.insert(tk.END,f'The numbers are :{num_list}')

            elif int(txt_1) == int(num_list[0]) and int(txt_2) != int(num_list[1]) and int(txt_3) != int(num_list[2]):
                list_box.insert(0,f'{lbl_1a}')
                list_box.insert(tk.END,f'{lbl_2b}')
                list_box.insert(tk.END,f'{lbl_3b}')
            elif int(txt_1) != int(num_list[0]) and int(txt_2) == int(num_list[1]) and int(txt_3) != int(num_list[2]):
                list_box.insert(0,f'{lbl_1b}')
                list_box.insert(tk.END,f'{lbl_2a}')
                list_box.insert(tk.END,f'{lbl_3b}')
            elif int(txt_1) != int(num_list[0]) and int(txt_2) != int(num_list[1]) and int(txt_3) == int(num_list[2]):
                list_box.insert(0,f'{lbl_1b}')
                list_box.insert(tk.END,f'{lbl_2b}')
                list_box.insert(tk.END,f'{lbl_3a}')
            elif int(txt_1) == int(num_list[0]) and int(txt_2) == int(num_list[1]) and int(txt_3) != int(num_list[2]):
                list_box.insert(0,f'{lbl_1a}')
                list_box.insert(tk.END,f'{lbl_2a}')
                list_box.insert(tk.END,f'{lbl_3b}')
            elif int(txt_1) == int(num_list[0]) and int(txt_2) != int(num_list[1]) and int(txt_3) == int(num_list[2]):
                list_box.insert(0,f'{lbl_1a}')
                list_box.insert(tk.END,f'{lbl_2b}')
                list_box.insert(tk.END,f'{lbl_3a}')
            elif int(txt_1) != int(num_list[0]) and int(txt_2) == int(num_list[1]) and int(txt_3) == int(num_list[2]):
                list_box.insert(0,f'{lbl_1b}')
                list_box.insert(tk.END,f'{lbl_2a}')
                list_box.insert(tk.END,f'{lbl_3a}')
            else:
                list_box.insert(0,f'{lbl_1b}')
                list_box.insert(tk.END,f'{lbl_2b}')
                list_box.insert(tk.END,f'{lbl_3b}')

   #if number fields are empty
    elif txt_1=='' or txt_2=='' or txt_3=='':
        messagebox.showerror(title='Error',message='Number fields can not be empty')

def clear():
    first_ent.delete(0,tk.END)
    second_ent.delete(0,tk.END)
    third_ent.delete(0,tk.END)
    list_box.delete(0,tk.END)

def quit():
    if messagebox.askokcancel(title='Quit',message='Do you want to quit'):
        window.destroy()

def show():
    if num_list == []:
        messagebox.showerror(title='error',message='You must click the start button to begin')
    else:
        messagebox.showinfo(title='Message',message='The Numbers are:'+ str(num_list))


title_head = Label(master=window,text=f'Guess Number Game from 0 to 9',font='Helvetical 15 bold',fg='red')
title_head.grid(row=0,column=1,sticky=W,padx=10,pady=5)

title_text = 'Click the start button only once to generate three unknown numbers,\n then guess the three numbers and click check number button to see result.\n To see the numbers after several attempts, click show numbers button'

title_lbl = Label(master=window,text=f'{title_text}',font='Helvetical 10 bold',fg='red')
title_lbl.grid(row=2,column=1,sticky=W,padx=2,pady=10)

start_btn = Button(master=window,text='Start',font='Helvetical 10 bold',bg='light blue',fg='red',command=start)
start_btn.grid(row=4,column=1,padx=5,pady=5,sticky='W')

frm_1 = Frame(master=window, relief=tk.GROOVE,borderwidth=5)
frm_1.grid(row=6,column=1,sticky=W,padx=10)

first_lbl = Label(master=frm_1,text='First Number',font='Helvetical 10 bold',fg='red')
first_lbl.grid(row=0,column=1,sticky=W,padx=10,pady=5)
first_text = StringVar()
first_ent = Entry(master=frm_1,textvariable=first_text)
first_ent.grid(row=0,column=2,sticky=W,padx=10,pady=5)

second_lbl = Label(master=frm_1,text='Second Number',font='Helvetical 10 bold',fg='red')
second_lbl.grid(row=2,column=1,sticky=W,padx=10,pady=5)
second_text = StringVar()
second_ent = Entry(master=frm_1,textvariable=second_text)
second_ent.grid(row=2,column=2,sticky=W,padx=10,pady=5)

third_lbl = Label(master=frm_1,text='Third Number',font='Helvetical 10 bold',fg='red')
third_lbl.grid(row=4,column=1,sticky=W,padx=10,pady=5)
third_text = StringVar()
third_ent = Entry(master=frm_1,textvariable=third_text)
third_ent.grid(row=4,column=2,sticky=W,padx=10,pady=5)

list_box = Listbox(master=window,font='Helvetical 10 bold',bg='orange',fg='blue',width=30,height=10)
list_box.grid(row=6,column=1,sticky=W,padx=300)

frm_2 = Frame(master=window, relief=tk.FLAT,borderwidth=5)
frm_2.grid(row=9,column=1,sticky=W,padx=10,pady=10)

btn_1 = Button(master=frm_2,text='Check Number',font='Helvetical 10 bold',bg='light blue',fg='red',command=chek_num)
btn_1.grid(row=0,column=1,padx=5,pady=5)

btn_2 = Button(master=frm_2,text='Clear',font='Helvetical 10 bold',bg='light blue',fg='red',command=clear)
btn_2.grid(row=0,column=2,padx=5,pady=5)

btn_3 = Button(master=frm_2,text='Quit',font='Helvetical 10 bold',bg='light blue',fg='red',command=quit)
btn_3.grid(row=0,column=3,padx=5,pady=5)

btn_4 = Button(master=frm_2,text='Show Numbers',font='Helvetical 10 bold',bg='light blue',fg='red',command=show)
btn_4.grid(row=0,column=4,padx=5,pady=5)

fourth_lbl = Label(master=window,text='Built by Peter Modo',font='Helvetical 10 bold',fg='blue')
fourth_lbl.grid(row=11,column=1,sticky=W,padx=10,pady=5)

window.mainloop()
