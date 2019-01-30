#Para esta libreria, intalar "sudo apt-get install python-tk"

from Tkinter import *
import tkMessageBox as box
import requests
import json

headers

def dialog1():
    username=entry1.get()
    password = entry2.get()
    if (username != '' and  password != ''):
		
		#response = requests.get('http://laboratorioredesneuronales.herokuapp.com/')
		#token = response.headers['Set-Cookie']
		params = {'name': username, 'password':password}
		url = 'http://laboratorioredesneuronales.herokuapp.com/login'
		response = requests.post(url, params=params)		

		if (response.status_code!=200):
			box.showinfo('info','Correo o Password Incorrectos')
		else:
			token = response.headers['token']
			headers = {'X-CSRF-TOKEN': token}			
		
    else:
        box.showinfo('info','Correo y Password Requeridos')


window = Tk()
window.title('Login laboratorio Redes Neuronales')

frame = Frame(window)

Label1 = Label(window,text = 'Correo ')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)



Label2 = Label(window,text = 'Password ')
Label2.pack(padx = 15,pady=6)

entry2 = Entry(window, bd=5,show='*')
entry2.pack(padx = 15,pady=7)




btn = Button(frame, text = 'Ingresar',command = dialog1)


btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()

