import customtkinter as ctk
from src.combinaciones import combPosibles
from tkinter import messagebox

class asideFrame(ctk.CTkFrame):
  def __init__(self, master, props):
    super().__init__(master)
    # Proposiciones almacenadas
    self.props = props 

    # Titulo del frame
    self.label = ctk.CTkLabel(self, text="Combinatoria de\nproposiciones logicas", font=("Helvetica", 16, "bold"))
    self.label.pack(pady=30, padx=30)
    
    # Boton-Generar combinaciones posibles
    self.combinaciones = ctk.CTkButton(self, text="Generar\ncombinatoria", font=("Helvetica", 14, "bold"), command = self.generarCombinatoria)
    self.combinaciones.pack(pady=20, padx=30)

  # Metodo para obtener todas las combinaciones posibles
  def generarCombinatoria(self):
    if len(self.props) >= 2:
      self.toplevel = combPosibles(master = self)
      self.toplevel.grab_set()
    else:
      messagebox.showwarning("Advertencia", "¡Debe ingresar al menos 2 proposiciones!")