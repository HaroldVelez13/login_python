#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Este codigo es para que nos acepte caracteres en español

#Para esta libreria, intalar "sudo apt-get install python-tk"
from Tkinter import *
import tkMessageBox as box
#esta libreria viene por defecto, en caso de que no instalar "sudo apt-get install requests"
import requests

#---------------********************************---------------

#Esta variable tendra la direccion a donde haremos la peciciones
Api_url = 'http://laboratorioredesneuronales.herokuapp.com/api/'



def vista_login():
	#Tomamos los valores del formulario
    correo=entry1.get()
    password = entry2.get()

    #Con global podemos instanciar la variable y modificarla en esta funcion
    global Api_url

    #Validamos que los valores existan
    if (correo != '' and  password != ''):
    	#enviamos la solicitud al servidor
		params = {'email': correo, 'password':password}
		url = Api_url+'login_api'
		response = requests.post(url, params=params)
		#SI no es aceptada
		if (response.status_code!=200):
			box.showwarning('Warning','Correo o Contraseña Incorrectos')
		#si es correcto, tenemos nuestro user_id (La autenticacion de que somos nosotros)
		else:
			user_id = response.text	
			Api_url = Api_url+'user/'+user_id+'/'
			box.showinfo('info','Muy bien, ya esta validado, cierra la ventana y sigamos!')	
	#Si los datos vienen vacios		
    else:
        box.showwarning('Warning','Correo y Contraseña Requeridos')

#Iniciamos la interface del login
window = Tk()
window.title(' Laboratorio Redes Neuronales ')
frame = Frame(window)
Label1 = Label(window,text = ' Correo ')
Label1.pack(padx=15,pady= 5)
entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)
Label2 = Label(window,text = ' Contraseña ')
Label2.pack(padx = 15,pady=6)
entry2 = Entry(window, bd=5,show='*')
entry2.pack(padx = 15,pady=7)
btn = Button(frame, text = 'Ingresar',command = vista_login)
btn.pack(side = RIGHT , padx =5)
frame.pack(padx=130,pady = 19)
#color de fondo #93ABB9
#window.config(background='#93ABB9')
#iniciamos la interface
window.mainloop()

print Api_url
#---------------********************************---------------

#Desde aca en adelante viene la logica para enviar las imagenes
#Este es un ejemplo de como se debe hacer
#files = {'imagen': open('img.jpg', 'rb')}
#requests.post(Api_url, files=files)
