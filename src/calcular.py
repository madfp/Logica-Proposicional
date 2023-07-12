import customtkinter as ctk

class calcularProp(ctk.CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # Configuraciones de la ventana
        self.geometry("750x500")
        self.title("Calculadora")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1)
        # Proposiciones almacenadas
        self.props = self.master.props
        # Frame de la ventana
        self.my_frame = calculadora(self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
class calculadora(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Informacion de la ventana
        self.finalData = ""
        self.label = ctk.CTkLabel(self, text="Calcular proposiciones moleculares", font=("Helvetica", 17, "bold"))
        self.label.pack(pady = 20)
        # Resultado de la operacion
        self.resultado = ctk.CTkEntry(self, placeholder_text="Resultado de la operacion...", font=("Helvetica", 15, "bold"))
        self.resultado.configure(state="disabled")
        self.resultado.pack(pady = 10, fill = "x", padx = 20)
        # Captura de la operacion
        self.captura = ctk.CTkEntry(self, placeholder_text="Ingrese la operacion deseada...", font=("Helvetica", 17, "bold"))
        self.captura.pack(pady=10, fill="x", padx = 200)
        # Botones para ingresar los operadores

        # Boton para obtener el resultado
        self.getResult = ctk.CTkButton(self, text = "Obtener", font = ("Helvetica", 17, "bold"), command = self.obtenerResultado)
        self.getResult.pack(pady = 10)

    # Metodo para obtener el resultado de la entrada de texto
    def obtenerResultado(self):
        self.finalData = self.captura.get()
        self.captura.delete(0, len(self.finalData))
        self.setResultado()

    # Metodo para escribir el resultado en la entrada de texto (desactivada)
    def setResultado(self):
        self.resultado.configure(state="normal")
        self.clearResultado()
        self.resultado.insert(0, self.finalData)
        self.resultado.configure(state="disabled")

    # Metodo para limpiar la informacion en la entrada de texto (desactivada)
    def clearResultado(self):
        clear = self.resultado.get()
        self.resultado.delete(0, len(clear))

# Validar la cantidad de caracteres permitidos en el input