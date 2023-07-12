import customtkinter as ctk
class frameProp(ctk.CTkFrame):
  def __init__(self, master, info, var):
    super().__init__(master)
    # Datos del frame
    self.info = info
    self.var = var
    # Proposicion almacenada
    self.prop = ctk.CTkEntry(self, font=("Helvetica", 17, "bold"), width=450)
    self.prop.insert(0, info)
    self.prop.pack(pady=20)
    # Boton para eliminar la proposicion
    self.button = ctk.CTkButton(self, text=f'Eliminar "{var}"', font=("Helvetica", 14, "bold"), command=self.clear, width=300)
    self.button.pack()
  
  # Metodo para eliminar el frame con la proposicion
  def clear(self):
    self.master.props.remove({self.var:self.info})
    self.master.used.remove(self.var)
    self.master.clearProps.remove(self.info)
    self.destroy()

  # Metodo para obtener los datos del frame
  def getProp(self):
    return [self.var, self.info]

# Frame para ingresar proposiciones
class inputFrame(ctk.CTkFrame):
  def __init__(self, master, props, clearProps, values, used):
    super().__init__(master)
    # Info del frame
    self.label = ctk.CTkLabel(self, text="Añadir proposiciones", font=("Helvetica", 18, "bold"))
    self.label.pack(pady=20)

    # Captura de la proposicion
    self.entry = ctk.CTkEntry(self, placeholder_text="Ingrese la proposicion lógica...", font=("Helvetica", 17, "bold"))
    self.entry.pack(padx=30, pady=20, fill="x")

    # Boton añadir proposicion
    self.añadir = ctk.CTkButton(self, text="Añadir proposicion", font=("Helvetica", 14, "bold"), command=self.master.añadirProposicion)
    self.añadir.pack(padx=80, fill="x")