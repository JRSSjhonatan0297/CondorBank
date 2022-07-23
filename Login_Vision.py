#--------------------------------------Importamos librerias--------------------------------------------

from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
from PIL import Image, ImageTk




#------------------------ Crearemos una funcion que se encargara de registrar el usuario ---------------------

def registrar_usuario():
    usuario_info = usuario.get() #Obetnemos la informacion alamcenada en usuario
    contra_info = contra.get() #Obtenemos la informacion almacenada en contra
    nombreusuario_info=nombre_completo.get();
    fech_nacimiento_info = fech_nacimiento.get();

    archivo = open(usuario_info, "w") #Abriremos la informacion en modo escritura
    archivo.write(usuario_info + "\n")   #escribimos la info
    archivo.write(contra_info+ "\n")
    archivo.write(nombreusuario_info+ "\n")
    archivo.write(fech_nacimiento_info+ "\n")
    archivo.write('0')
    archivo.close()

    #Limpiaremos los text variable
    usuario_entrada.delete(0, END)
    contra_entrada.delete(0, END)
    #Ahora le diremos al usuario que su registro ha sido exitoso
    Label(pantalla1, text = "Registro Convencional Exitoso", fg = "green", font = ("Calibri",11)).pack()
    

#--------------------------- Funcion para almacenar el registro  --------------------------------------
    
def registro_():
    #Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)               #Elegimos la camara con la que vamos a hacer la deteccion
    while(True):
        ret,frame = cap.read()              #Leemos el video
        cv2.imshow('Registro ',frame)         #Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:            #Cuando oprimamos "Escape" rompe el video
            break
    usuario_img = usuario.get()
    cv2.imwrite(usuario_img+".jpg",frame)       #Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()                               #Cerramos
    cv2.destroyAllWindows()

    usuario_entrada.delete(0, END)   #Limpiamos los text variables
    contra_entrada.delete(0, END)
    Label(pantalla1, text = "Registro  Exitoso", fg = "green", font = ("Calibri",11)).pack()

    #----------------- Detectamos el rostro y exportamos los pixeles --------------------------
    
    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1,ancho, alto = lista_resultados[i]['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC) #Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img+".jpg",cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img+".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)   
    
def registro_facial():
    #Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)               #Elegimos la camara con la que vamos a hacer la deteccion
    while(True):
        ret,frame = cap.read()              #Leemos el video
        cv2.imshow('Registro Facial',frame)         #Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:            #Cuando oprimamos "Escape" rompe el video
            break
    usuario_img = usuario.get()
    cv2.imwrite(usuario_img+".jpg",frame)       #Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()                               #Cerramos
    cv2.destroyAllWindows()

    usuario_entrada.delete(0, END)   #Limpiamos los text variables
    contra_entrada.delete(0, END)
    Label(pantalla1, text = "Registro Facial Exitoso", fg = "green", font = ("Calibri",11)).pack()

    #----------------- Detectamos el rostro y exportamos los pixeles --------------------------
    
    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1,ancho, alto = lista_resultados[i]['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC) #Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img+".jpg",cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img+".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)   
    
#------------------------Crearemos una funcion para asignar al boton registro --------------------------------
def registro():
    global usuario
    global nombre_completo
    global contra  #Globalizamos las variables para usarlas en otras funciones
    global usuario_entrada
    global contra_entrada
    global fech_nacimiento
    global pantalla1
    pantalla1 = Toplevel(pantalla) #Esta pantalla es de un nivel superior a la principal
    pantalla1.title("Registro")
    pantalla1.geometry("300x350")  #Asignamos el tamaño de la ventana
    pantalla1.iconbitmap('uno.ico')
    #--------- Empezaremos a crear las entradas ----------------------------------------
    
    usuario = StringVar()
    contra = StringVar()
    nombre_completo = StringVar()
    fech_nacimiento = StringVar()
    
    Label(pantalla1, text = "Registro facial: debe de asignar un usuario:").pack()
    #Label(pantalla1, text = "").pack()  #Dejamos un poco de espacio
    Label(pantalla1, text = "Registro tradicional: debe asignar usuario y contraseña:").pack()
    Label(pantalla1, text = "").pack()  #Dejamos un poco de espacio

    Label(pantalla1, text = "Nombre completo * ").pack()  #Mostramos en la pantalla 1 el usuario
    nombre_entrada = Entry(pantalla1, textvariable = nombre_completo) #Creamos un text variable para que el usuario ingrese la info
    nombre_entrada.pack()

    Label(pantalla1, text = "Fecha de nacimiento * ").pack()  #Mostramos en la pantalla 1 la fecha de nacimiento  del usuario
    fecha_entrada = Entry(pantalla1, textvariable = fech_nacimiento) #Creamos un text variable para que el usuario ingrese la info
    fecha_entrada.pack()
    
    Label(pantalla1, text = "Usuario * ").pack()  #Mostramos en la pantalla 1 el nombre completo de usuario (nombre+apellidos)
    usuario_entrada = Entry(pantalla1, textvariable = usuario) #Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()
    Label(pantalla1, text = "Contraseña * ").pack()  #Mostramos en la pantalla 1 la contraseña
    contra_entrada = Entry(pantalla1, textvariable = contra) #Creamos un text variable para que el usuario ingrese la contra
    contra_entrada.pack()
    Label(pantalla1, text = "").pack()  #Dejamos un espacio para la creacion del boton
    Button(pantalla1, text = "Registro Tradicional", width = 15, height = 1, command = registrar_usuario).pack()  #Creamos el boton

    #------------ Vamos a crear el boton para hacer el registro facial --------------------
    Label(pantalla1, text = "").pack()
    Button(pantalla1, text = "Registro Facial", width = 15, height = 1, command = registro_facial).pack()


#------------------------------------------- Funcion para verificar los datos ingresados al login ------------------------------------
    
def verificacion_login():

    global verificacion_usuario
    
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()

    usuario_entrada2.delete(0, END)
    contra_entrada2.delete(0, END)

    lista_archivos = os.listdir()   #Vamos a importar la lista de archivos con la libreria os
    if log_usuario in lista_archivos:   #Comparamos los archivos con el que nos interesa
        archivo2 = open(log_usuario, "r")  #Abrimos el archivo en modo lectura
        verificacion = archivo2.read().splitlines()  #leera las lineas dentro del archivo ignorando el resto
        if log_contra in verificacion:
            print("Inicio de sesion exitoso")

            verificacion_usuario=log_usuario
            Label(pantalla2, text = "Inicio de Sesion Exitoso", fg = "green", font = ("Calibri",11)).pack()
            login_session(verificacion_usuario,verificacion_contra)
        else:
            print("Contraseña incorrecta, ingrese de nuevo")
            Label(pantalla2, text = "Contraseña Incorrecta", fg = "red", font = ("Calibri",11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla2, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()
    
#--------------------------Funcion para el Login Facial --------------------------------------------------------
def login_facial():
#------------------------------Vamos a capturar el rostro-----------------------------------------------------
    cap = cv2.VideoCapture(0)               #Elegimos la camara con la que vamos a hacer la deteccion
    while(True):
        ret,frame = cap.read()              #Leemos el video
        cv2.imshow('Login Facial',frame)         #Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:            #Cuando oprimamos "Escape" rompe el video
            break
    usuario_login = verificacion_usuario    #Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir

    
    cv2.imwrite(usuario_login+"LOG.jpg",frame)       #Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()                               #Cerramos
    cv2.destroyAllWindows()

    usuario_entrada2.delete(0, END)   #Limpiamos los text variables
    contra_entrada2.delete(0, END)

    #----------------- Funcion para guardar el rostro --------------------------
    
    def log_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1,ancho, alto = lista_resultados[i]['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC) #Guardamos la imagen 150x200
            cv2.imwrite(usuario_login+"LOG.jpg",cara_reg)
            return pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    #-------------------------- Detectamos el rostro-------------------------------------------------------
    
    img = usuario_login+"LOG.jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    log_rostro(img, caras)

    #-------------------------- Funcion para comparar los rostros --------------------------------------------
    def orb_sim(img1,img2):
        orb = cv2.ORB_create()  #Creamos el objeto de comparacion
 
        kpa, descr_a = orb.detectAndCompute(img1, None)  #Creamos descriptor 1 y extraemos puntos claves
        kpb, descr_b = orb.detectAndCompute(img2, None)  #Creamos descriptor 2 y extraemos puntos claves

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) #Creamos comparador de fuerza

        matches = comp.match(descr_a, descr_b)  #Aplicamos el comparador a los descriptores

        regiones_similares = [i for i in matches if i.distance < 70] #Extraemos las regiones similares en base a los puntos claves
        if len(matches) == 0:
            return 0
        return len(regiones_similares)/len(matches)  #Exportamos el porcentaje de similitud
        
    #---------------------------- Importamos las imagenes y llamamos la funcion de comparacion ---------------------------------
    
    im_archivos = os.listdir()   #Vamos a importar la lista de archivos con la libreria os
    if usuario_login.set()+".jpg" in im_archivos:   #Comparamos los archivos con el que nos interesa
        rostro_reg = cv2.imread(usuario_login+".jpg",0)     #Importamos el rostro del registro
        rostro_log = cv2.imread(usuario_login+"LOG.jpg",0)  #Importamos el rostro del inicio de sesion
        similitud = orb_sim(rostro_reg, rostro_log)
        if similitud >= 0.98:
            Label(pantalla2, text = "Inicio de Sesion Exitoso", fg = "green", font = ("Calibri",11)).pack()

            print(log_usuario)
            login_session("72598829","123456")
            print("Bienvenido al sistema usuario: ",usuario_login)
            print("Compatibilidad con la foto del registro: ",similitud)
            
        else:
            print("Rostro incorrecto, Cerifique su usuario")
            print("Compatibilidad con la foto del registro: ",similitud)
            Label(pantalla2, text = "Incompatibilidad de rostros", fg = "red", font = ("Calibri",11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla2, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()
            

#------------------------Funcion que asignaremos al boton login -------------------------------------------------
        
def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2
    
    pantalla2 = Toplevel(pantalla)
    
    pantalla2.title("Login")
    pantalla2.geometry("300x250")   #Creamos la ventana
    pantalla2.iconbitmap('uno.ico')
    Label(pantalla2, text = "Login facial: debe de asignar un usuario:").pack()
    Label(pantalla2, text = "Login tradicional: debe asignar usuario y contraseña:").pack()
    Label(pantalla2, text = "").pack()  #Dejamos un poco de espacio
    
    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()
    
    #---------------------------------- Ingresamos los datos --------------------------
    Label(pantalla2, text = "Usuario * ").pack()
  
    usuario_entrada2 = Entry(pantalla2, textvariable = verificacion_usuario)
    usuario_entrada2.pack()
    Label(pantalla2, text = "Contraseña * ").pack()
    contra_entrada2 = Entry(pantalla2, textvariable = verificacion_contra)
    contra_entrada2.pack()
    Label(pantalla2, text = "").pack()
    Button(pantalla2, text = "Inicio de Sesion Tradicional", width = 20, height = 1, command = verificacion_login).pack()

    #------------ Vamos a crear el boton para hacer el login facial --------------------
    Label(pantalla2, text = "").pack()
    Button(pantalla2, text = "Inicio de Sesion Facial", width = 20, height = 1, command = login_facial).pack()
        
#------------------------- Funcion de nuestra pantalla principal ------------------------------------------------
    
def pantalla_principal():
    global pantalla          #Globalizamos la variable para usarla en otras funciones
    pantalla = Tk()
    pantalla.geometry("300x500")  #Asignamos el tamaño de la ventana 
    pantalla.config(bg="#C7C7C7")
    pantalla.title("Condor Bank System")       #Asignamos el titulo de la pantalla
    pantalla.iconbitmap('images/uno.ico')
    imagenL=PhotoImage(file="images/logo.png")
    lblImagen=Label(pantalla, image=imagenL).place(x=0, y=0)
#------------------------- Vamos a Crear los Botones ------------------------------------------------------


    Button(text = "Iniciar Sesion", bg="black",fg=("white"), height = "2", width = "20",  command = login).place(x=75, y=330)
    Label(text = "").pack() #Creamos el espacio entre el primer boton y el segundo boton
    Button(text = "Registro",bg="black",fg=("white"), height = "2", width = "20", command = registro).place(x=75, y=400)


    pantalla.mainloop()







#========================================================================================================

def login_session(verif_usuario,verif_contra):
    
    global pantalla_p         #Globalizamos la variable para usarla en otras funciones
    global login_name
    global login_password
    pantalla_p  = Tk()
    all_accounts = os.listdir()
    login_name = verif_usuario
    login_password = verif_contra

    for name in all_accounts:
        if name == login_name:
            file = open(login_name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            USUARIO  = file_data[2]
            #Account Dashboard
            
            pantalla_p.title('Dashboard')
            pantalla_p.iconbitmap('images/uno.ico')
            #Labels
            Label(pantalla_p, text="Panel de cuenta", bg = "gray", width = 30, height = 2, font = ("Verdana",13)).grid(row=1,sticky=N,padx=10)
            Label(pantalla_p, text="Bienvenido "+USUARIO, font=('Calibri',12)).grid(row=2,sticky=N,pady=5)
            #Buttons
            Button(pantalla_p, text="Detalle de la cuenta",font=('Calibri',12),width=30,command=personal_details).grid(row=3,sticky=N,padx=10)
            Button(pantalla_p, text="Depositos",font=('Calibri',12),width=30,command=deposit).grid(row=4,sticky=N,padx=10)
            Button(pantalla_p, text="Retiro",font=('Calibri',12),width=30,command=withdraw).grid(row=5,sticky=N,padx=10)
            pantalla.iconbitmap('images/uno.ico')
            Label(pantalla_p).grid(row=5,sticky=N,pady=10)
            pantalla_p.mainloop()
            return



#===================================DETALLE DE LA CUENTA==============================================================


def personal_details():
    #Vars



    
    global pantalla_sys_1        #Globalizamos la variable para usarla en otras funciones
    global login_name
    log_usu=login_name
    pantalla_sys_1=Tk()
    file = open(log_usu, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_usuario =user_details[2]
    details_age = user_details[3]
    details_balance = user_details[4]
    #Personal details screen
    
    
    pantalla_sys_1.title('Detalle personal y Estado de Cuenta')
    pantalla_sys_1.iconbitmap('images/uno.ico')
    #Labels
    Label(pantalla_sys_1, text="Detalle de la cuenta bancaria", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(pantalla_sys_1, text="Nombre : "+details_usuario, font=('Calibri',12)).grid(row=1,sticky=W)
    Label(pantalla_sys_1, text="Año  de nacimiento : "+details_age, font=('Calibri',12)).grid(row=2,sticky=W)
    Label(pantalla_sys_1, text="Balance :S/."+details_balance, font=('Calibri',12)).grid(row=4,sticky=W)
    pantalla_sys_1.mainloop()
       
            
def close_window():
    root.destroy()


def deposit():
    #Vars
    global amount
    global deposit_notif
    global current_balance_label
    global login_name
    global pantalla_sys_5
    log_usu=login_name
    amount = StringVar()
    file   = open(log_usu, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    print(user_details[4])
    pantalla_sys_5  = Tk()
    #Deposit Screen
    pantalla_sys_5.title('Depositar')
    pantalla_sys_5.iconbitmap('images/uno.ico')

    #Label
    Label(pantalla_sys_5, text="Depositar", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(pantalla_sys_5, text="Monto : S/."+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(pantalla_sys_5, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    deposit_notif = Label(pantalla_sys_5,font=('Calibri',12))
    deposit_notif.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(pantalla_sys_5, textvariable=amount).grid(row=2,column=1)
    #Button
    Button(pantalla_sys_5,text="Finish",font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=W,pady=5)
    pantalla_sys_5.mainloop()

def finish_deposit():
    usuario=login_name
    if amount.get() == "":
        deposit_notif.config(text='Amount is required!',fg="red")
        return
    if float(amount.get()) <=0:
        deposit_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(usuario, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : £"+str(updated_balance),fg="green")
    deposit_notif.config(text='Balance Updated', fg='green')

 
def withdraw():
     #Vars
    global pantalla_sys_2         #Globalizamos la variable para usarla en otras funciones
    pantalla_sys_2  = Tk()
    global withdraw_amount
    global withdraw_notif
    usuario=login_name
    global current_balance_label
    withdraw_amount = StringVar()
    file   = open(usuario, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    pantalla_sys_2  = Tk()
    #Deposit Screen
    
    pantalla_sys_2.title('Withdraw')
    pantalla_sys_2.iconbitmap('images/uno.ico')
    #Label
    Label(pantalla_sys_2, text="Deposit", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(pantalla_sys_2, text="Current Balance : £"+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(pantalla_sys_2, text="Amount : ", font=('Calibri',12)).grid(row=2,sticky=W)
    withdraw_notif = Label(pantalla_sys_2,font=('Calibri',12))
    withdraw_notif.grid(row=4, sticky=N,pady=5)
    #Entry
    Entry(pantalla_sys_2, textvariable=withdraw_amount).grid(row=2,column=1)
    #Button
    Button(pantalla_sys_2,text="Finish",font=('Calibri',12),command=finish_withdraw).grid(row=3,sticky=W,pady=5)
    pantalla_sys_2.mainloop()

def finish_withdraw():
    usuario=login_name.get()
    if withdraw_amount.get() == "":
        withdraw_notif.config(text='Amount is required!',fg="red")
        return
    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text='Negative currency is not accepted', fg='red')
        return

    file = open(usuario, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]

    if float(withdraw_amount.get()) >float(current_balance):
        withdraw_notif.config(text='Insufficient Funds!', fg='red')
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Monto : S/."+str(updated_balance),fg="green")
    withdraw_notif.config(text='Balance Updated', fg='green')


pantalla_principal()





    
