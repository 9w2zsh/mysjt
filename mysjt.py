from tkinter import *
import requests
import json

root = Tk()
root.title('MySejahtera Appointment')
#root.icontbitmap('ico/py.ico')
root.geometry('650x250')

def show_appt():
    ic = ic_input.get()
    tel = tel_input.get()
    print(ic,tel)
    try:
        api_url = "https://api.vaksincovid.gov.my/semakstatus/westfunction?"
        appt_req = requests.get(api_url+"name="+ic+"-bsep-"+tel)
        appt = json.loads(appt_req.content)
    except Exception as e:
        appt = "Error loading data..."
        
ic_label = Label(root,text='I/C: ')
ic_label.grid(row=0,column=0,sticky=W)
tel_label = Label(root,text='Tel number: ')
tel_label.grid(row=0,column=1,sticky=W)

ic_input = Entry(root)
ic_input.grid(row=0,column=1,sticky=W)
tel_input = Entry(root)
tel_input.grid(row=1,column=1,sticky=W)

btn_quit = Button(root, text='Quit', command=root.quit).grid(row=3,column=0,sticky=W)
btn_show = Button(root, text='Show', command=show_appt).grid(row=3,column=1,sticky=W)


mainloop()
