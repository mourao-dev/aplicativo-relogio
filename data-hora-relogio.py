from tkinter import *
from tkinter import ttk
import datetime

hoje = datetime.datetime.now()
data = str(hoje).split(" ")[0]
dia = data.split("-")[2]
mes = data.split("-")[1]
ano = data.split("-")[0]
horario = str(hoje).split(" ")[1]
segundos = float(horario.split(":")[2])
segundos = round(segundos)
minuto = horario.split(":")[1]
hora = horario.split(":")[0]

root = Tk()
root.title("Relógio")
frm = ttk.Frame(root, padding=100)
frm.grid()
root.resizable(False,False)
ttk.Label(frm, text=f"Hoje é dia \n{dia}/{mes}/{ano}\n{hora}:{minuto}:{segundos}\nHorário de Brasília").grid(column=0, row=0)
ttk.Button(frm, text="Sair", command=root.destroy).grid(column=0, row=1000)
root.mainloop()
