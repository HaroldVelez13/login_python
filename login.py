#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Este codigo es para que nos acepte caracteres en español


#Para esta libreria, intalar "sudo apt-get install python-tk"
from Tkinter import *
import tkMessageBox as box
#esta libreria viene por defecto, en caso de que no instalar "sudo apt-get install requests"
import requests
import re

#Esta variable es para tener el udsuario registrado(logueado).
user_id = ''
#Esta variable tendra la direccion a donde haremos la peciciones
# http://laboratorioredesneuronales.herokuapp.com/api/
Api_url = 'http://laboratorioredesneuronales.herokuapp.com/api/'



def vista_login():
	#Tomamos los valores del formulario
    correo=entry1.get()
    password = entry2.get()

    #Validamos que los valores existan
    if (correo != '' and  password != ''):
    	#enviamos la solicitud al servidor
		params = {'email': correo, 'password':password}
		url = Api_url+'login_api'
		response = requests.post(url, params=params)		

		#SI no es aceptada
		if (response.status_code!=200):
			box.showwarning('Warning','Correo o Password Incorrectos')
		#si es correcto, tenemos nuestro user_id (La autenticacion de que somos nosotros)
		else:
			user_id = response.text			
	
	#Si los datos vienen vacios		box.showinfo('info','Muy bien, ya esta validado')
    else:
        box.showwarning('Warning','Correo y Password Requeridos')

#Iniciamos la interface del login
window = Tk()
window.title('Laboratorio Redes Neuronales')

frame = Frame(window)

Label1 = Label(window,text = 'Correo ')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)



Label2 = Label(window,text = 'Password ')
Label2.pack(padx = 15,pady=6)

entry2 = Entry(window, bd=5,show='*')
entry2.pack(padx = 15,pady=7)


btn = Button(frame, text = 'Ingresar',command = vista_login)


btn.pack(side = RIGHT , padx =5)
frame.pack(padx=150,pady = 19)
#color de fondo #93ABB9
#window.config(background='#93ABB9')

#iniciamos la interface
window.mainloop()

print user_id
print Api_url


#url = Api_url+'user/'+user_id+'/redes/agregar'
#files = {'imagen': open('img.jpg', 'rb')}
#requests.post(url, files=files)
