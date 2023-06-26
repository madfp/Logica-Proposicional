import customtkinter as ctk
from tkinter import messagebox

class asideFrame(ctk.CTkFrame):
  def __init__(self, master, props):
    super().__init__(master)
    # Proposiciones almacenadas
    self.props = props

    # Titulo del frame
    self.label = ctk.CTkLabel(self, text="Combinatoria de\nproposiciones logicas", font=("Helvetica", 16, "bold"))
    self.label.pack(pady=40, padx=30)
    
    # Boton-Generar combinaciones posibles
    self.combinaciones = ctk.CTkButton(self, text="Generar\ncombinatoria", font=("Helvetica", 14, "bold"), command = self.generarCombinatoria)
    self.combinaciones.pack(pady=10, padx=30)

    # Boton-Calcular proposiciones especificas
    self.calcular = ctk.CTkButton(self, text="Calcular\nCombinatoria", font=("Helvetica", 14, "bold"), command = self.calcular_operacion)
    self.calcular.pack(pady=10, padx=30)

  # Metodo para obtener todas las combinaciones posibles
  def generarCombinatoria(self):
    if len(self.props) >= 2:
      print(self.props)
    else:
      messagebox.showwarning("showwarning", "¡Debe ingresar al menos 2 proposiciones!")

  # Metodo para calcular cierta operacion con las proposiciones almacenadas
  def calcular_operacion(self):
    if len(self.props)>=2:
      print(self.props)
    else:
      messagebox.showwarning("showwarning", "¡Debe ingresar al menos 2 proposiciones!")