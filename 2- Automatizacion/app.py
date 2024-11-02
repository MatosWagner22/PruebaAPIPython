import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Función para descargar la imagen en un hilo separado
def descargar_imagen_async(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        img_data = response.content

        # Ejecutamos la actualización en el hilo principal
        ventana.after(0, actualizar_imagen, img_data)
    except Exception as e:
        print(f"Error al descargar la imagen: {e}")
        ventana.after(0, mostrar_error)

# Función para actualizar la imagen en la interfaz
def actualizar_imagen(img_data):
    global imagen_original
    imagen_original = Image.open(BytesIO(img_data))
    imagen_tk = ImageTk.PhotoImage(imagen_original)

    label_imagen.config(image=imagen_tk)
    label_imagen.image = imagen_tk  # Guardar referencia
    label_cargando.pack_forget()  # Ocultar el mensaje de carga

# Función para mostrar un error si la descarga falla
def mostrar_error():
    label_cargando.config(text="Error al cargar la imagen.")

# Función para iniciar Selenium WebDriver
def iniciar_driver():
    chrome_driver_path = r"C:\Users\Dell\Desktop\chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def agregar():
    try:
        # Inicializar el driver de Selenium
        chrome_driver_path = r"C:\Users\Dell\Desktop\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)

        # Navegar a la URL donde se encuentra el formulario
        driver.get("http://127.0.0.1:5000/")
        driver.maximize_window()
        time.sleep(2)  # Esperar que la página cargue

        # Abrir el archivo DatosVinlandSaga.txt y leer todas las líneas
        with open("DatosVinlandSaga.txt", "r") as archivo:
            estudiantes = archivo.readlines()

       # Procesar cada entrada
        for linea in estudiantes:
            # Ignorar líneas vacías o mal formateadas
            if not linea.strip():
                continue
            try:
                personaje, tierra_favorita, aliado, armas, actividades, aventura, fecha = linea.strip().split(",")
            except ValueError:
                messagebox.showerror("Error", f"La línea está mal formateada: {linea}")
                continue

            # Llenar el formulario en la web
            driver.find_element(By.ID, "personaje").send_keys(personaje)
            driver.find_element(By.ID, tierra_favorita).click()
            driver.find_element(By.ID, "compañero").send_keys(aliado)

            # Seleccionar armas y actividades
            for arma in armas.split(";"):
                driver.find_element(By.XPATH, f"//option[@value='{arma.strip()}']").click()
            for actividad in actividades.split(";"):
                driver.find_element(By.ID, actividad.strip()).click()

            # Completar el resto del formulario
            driver.find_element(By.ID, "aventura").send_keys(aventura)
            driver.find_element(By.ID, "fecha").send_keys(fecha)
            time.sleep(3)  # Esperar a que el mensaje de éxito aparezca

            # Enviar el formulario
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(3)  # Esperar a que el mensaje de éxito aparezca

            boton_ok = driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm")
            boton_ok.click()
         

            time.sleep(2)  # Esperar antes de pasar 

            boton_volver = driver.find_element(By.XPATH, "//a[text()='Volver al Formulario']")
            boton_volver.click()



    except FileNotFoundError:
        # Manejar el error si el archivo no se encuentra
        messagebox.showerror("Error", "El archivo DatosVinlandSaga.txt no se encontró.")
    except Exception as e:
        # Manejar cualquier otro error
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    finally:
        # Asegurarse de cerrar el navegador al finalizar
        driver.quit()

def cerrar():
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas cerrar el programa?")
    if respuesta:
        ventana.destroy()  
        sys.exit()  

ventana = tk.Tk()
ventana.attributes("-fullscreen", True)
ventana.configure(bg="#f5f5f5")

label_cargando = tk.Label(
    ventana, text="Cargando...", font=("Helvetica", 24), bg="#f5f5f5", fg="#333"
)
label_cargando.pack(expand=True)

label_imagen = tk.Label(ventana, bg="#f5f5f5")
label_imagen.place(x=0, y=0, relwidth=1, relheight=1)

boton_frame = tk.Frame(ventana, bg="#f5f5f5")
boton_frame.place(relx=0.5, rely=0.9, anchor="center")

boton_style = {
    "width": 15,
    "height": 2,
    "font": ("Arial", 14),
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#4945a0",
    "relief": "flat",
    "bd": 0
}

# Botones del menú
boton_agregar = tk.Button(boton_frame, text="Agregar", command=agregar, **boton_style)
boton_agregar.grid(row=0, column=0, padx=10, pady=10)

boton_cerrar = tk.Button(boton_frame, text="Cerrar", command=cerrar, **boton_style)
boton_cerrar.grid(row=0, column=3, padx=10, pady=10)

# Descargar la imagen en un hilo separado
imagen_url = "https://static.wikia.nocookie.net/dubbing9585/images/3/3a/Sentai-filmworks-vinland-saga-blu-ray.jpg/revision/latest?cb=20210724212758"
threading.Thread(target=descargar_imagen_async, args=(imagen_url,)).start()

ventana.bind("<Escape>", lambda e: ventana.attributes("-fullscreen", False))

ventana.mainloop()
