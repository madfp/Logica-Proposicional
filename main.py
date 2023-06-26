import customtkinter as ctk
from src.aside import asideFrame
from src.input import inputFrame, frameProp
from src.saved import savedFrame


# Ventana principal
class main(ctk.CTk):
  def __init__(self):
    super().__init__()
    # Informacion de las Proposiciones
    self.props = [] # Lista de diccionarios var, prop
    self.clearProps = [] # Proposiciones limpias
    self.values = ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o"] # Variables para las proposiciones
    self.used = [] # Variables usadas
    # Configurando la ventana principal
    self._set_appearance_mode("dark") # Tema de la aplicacion
    self.title("Lógica proposicional") # Titulo de la aplicacion
    self.geometry("750x500") # Tamaño de la ventana
    self.grid_rowconfigure(1, weight=1)
    self.grid_columnconfigure(3, weight=1)
    self.resizable(False, False) # No se escala a pantalla completa (tamaño definido)

    # Frame con Scroll
    self.scroll = savedFrame(self, self.props, self.clearProps, self.values, self.used)
    self.scroll.grid(row=0, column=2, padx=10, pady=10, columnspan=3, sticky="nsew")

    # Frame lateral
    self.aside = asideFrame(self, self.props)
    self.aside.grid(row=0, column=0, rowspan=2, sticky="nsew")

    # Frame de captura
    self.input = inputFrame(self, self.props, self.clearProps, self.values, self.used)
    self.input.grid(row=1, column=2, padx=10, pady=10, columnspan=3, sticky="nsew")
  
  # Metodo para añadir una nueva proposicion
  def añadirProposicion(self):
    var = self.selectVar() # Seleccionar el nombre de la variable
    self.used.append(var) # Añadir la variable dentro de la lista de usadas
    prop = self.input.entry.get() # Obtener proposicion
    self.clearProps.append(self.input.entry.get()) # Añadir la proposicion a la lista
    if prop != "":
      self.input.entry.delete(0, len(prop)) # Eliminar proposicion del entry
      self.createFrame(prop, var)
      self.props.append({var:prop}) # Añadiendo al vector con las proposiciones la proposicion
  
  # Metodo para elegir la variable a trabajar
  def selectVar(self):
    for i in self.values: 
      if i not in self.used:
        return i
      
  # Metodo para añadir el nuevo frame con la proposicion
  def createFrame(self, pr, va):
    self.newFrame = frameProp(self.scroll, pr, va)
    self.newFrame.prop.configure(state="disabled")
    self.scroll.newFrame(self.newFrame)

if __name__ == "__main__":
  app = main()
  app.mainloop()