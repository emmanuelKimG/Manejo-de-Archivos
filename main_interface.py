import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from Registro import *
from fpdf import FPDF
import subprocess
import os
import re

PATH = "./documents/"

def get_entry_values(row_pos):
    registro = Registro
    for item in variables:
        setattr(registro,item[0], item[1].get())

    if registro.name:
        ttk.Button(tab1,text="Generar Documento",command= lambda r = registro: generate_documents(r)).grid(column=0,row= row_pos+1, columnspan=2)
        
def generate_documents(registro: Registro):
    with open("oficio.txt") as officio: 
        content = officio.read()
        
        for field in vars(registro):
            content = content.replace(f"[{field}]", str(getattr(registro,field)))
            
        with open(f"{PATH}document_{registro.name}_{registro.apellido1}.txt","w") as new_officio:
            new_officio.write(content)
    document_list()
        
def view_document(document_name : str):
    doc = re.sub('""',"",document_name)
    pdf = FPDF() 
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    f = open(PATH+doc, "r")

    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        
    pdf.output(f"{document_name}.pdf")
    subprocess.Popen([f"{document_name}.pdf"], shell=True)
        
def eliminar_doc(document_name :str):
    try:
        option = tkinter.messagebox.askyesnocancel(f'Remove Document', f'¿ Seguro que quieres eliminar  {document_name} ?')
        if option:
            os.remove(PATH+document_name)
            tkinter.messagebox.showinfo("Documento Eliminado",f"Documento {document_name} ha sido Removido")
            document_list()
            return True
    except:
        return False
    
def document_list():
    j = 0
    print("LISTANDO DOCUMENTOS")
    for file in os.listdir(PATH):
        name = re.sub("document_|.txt","",file)
        name = re.sub("_"," ",name)
        ttk.Label(tab2, text=f"{name}").grid(column=0, row=1+j)
        ttk.Button(tab2, text="Abrir Archivo",command= lambda f=file:view_document(f)).grid(column=1 , row= 1+j)
        ttk.Button(tab2, text="Eliminar",command= lambda f = file : eliminar_doc(f)).grid(column=2, row=j+1)
        j += 1
        

root = tk.Tk()
root.geometry("350x600")
tabControl = ttk.Notebook(root)
register_loaded = False

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1,text="Agregar")
tabControl.add(tab2,text="Ver")
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1, text="Agregar Registro").grid(column=0,row=0,padx=30,pady=30)
ttk.Label(tab2, text="Consultar Registro").grid(column=0,row=0,padx=30,pady=30)

variable_names = [field.name for field in fields(Registro)]
i = 0
variables = []

for item in variable_names:
    ttk.Label(tab1,text=f"{item}").grid(column=0,row=i+1)
    variables.append((item ,ttk.Entry(tab1,background="red"))) 
    variables[i][1].grid(column=1,row=i+1)
    i += 1

document_list()
    
ttk.Button(tab1, text="Get Values", command= lambda: get_entry_values(i+1)).grid(column=0, row=i+1, columnspan=2,pady=30)
    



# ttk.Button(tab1, text="Agregar",width=10).grid(column=1,row=1,padx=30,pady=30)


root.mainloop() 