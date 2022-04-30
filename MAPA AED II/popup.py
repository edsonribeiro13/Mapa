import tkinter as tk  
from tkinter import ttk
def msgErro():
    err = tk.Tk()  
    #Add a Title  
    err.title("Erro na aplicação")  
    #Label  
    ttk.Label(err, text="Error: Caminho impossível").grid(column=0,row=0,padx=20,pady=30)

def msgLimpar():
    popup = tk.Tk()  
    #Add a Title  
    popup.title("Limpar aplicação")  
    #Label  
    ttk.Label(popup, text="Clique mais uma vez para limpar").grid(column=0,row=0,padx=20,pady=30)

def msgDistancia(dist):
    popup = tk.Tk()  
    #Add a Title  
    popup.title("Distância total")  
    #Label  
    ttk.Label(popup, text=f"Distância total: {dist}").grid(column=10,row=10,padx=20,pady=30)