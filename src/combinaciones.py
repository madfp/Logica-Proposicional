import customtkinter as ctk

class combPosibles(ctk.CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.props = self.master.props # Capturar las proposiciones del elemento padre
        # Configuracion de la ventana
        self.geometry("750x500")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Elementos de la ventana
        self.scroll = scrollFrame(master=self)
        self.scroll.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        # Crear las combinaciones
        self.createComb()

    # Metodo para crear las combinaciones
    def createComb(self):
        operaciones = [" y ", " o ", ", entonces ", ", si y solo si, "]
        equivalencia = {" y ": " ∧ ", " o ":" V ", ", entonces ":"→", ", si y solo si, ":" ↔ "}
        operadores = [" ¬ ", " ∧ ", " V ", " → ", " ↔ "]
        negaciones = ["Es falso que ", " es falso que "]
        # Crear la combinacion de proposiciones
        for i in self.props:
            info1 = list(i.values())[0]
            var1 = list(i.keys())[0]
            for j in self.props:
                info2 = list(j.values())[0]
                var2 = list(j.keys())[0]
                if i != j:
                    for k in operaciones:
                        print(info1 + k +info2, var1 + equivalencia.get(k) + var2)
                        print(negaciones[0]+info1+k+info2, operadores[0]+var1+equivalencia.get(k)+var2)
                        print(info1+k+negaciones[1]+info2, var1+equivalencia.get(k)+operadores[0]+var2)
                        print(negaciones[0]+info1+k+negaciones[1]+info2, operadores[0]+var1+equivalencia.get(k)+operadores[0]+var2)

    # Metodo para agregar el frame con la proposicion
    def addComb(self):
        pass

# ScrollFrame para agregar frames con las combinaciones
class scrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self, text="Combinaciones posibles", font=("Helvetica", 17, "bold"))
        self.label.pack(pady=10)
    
    def addFrame(self, frame):
        info = frame(master = self)
        info.setInfo()

# Frame con la informacion (operacion/cadena)
class frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Entry de la operacion
        self.op = ctk.CTkEntry(self, font=("Helvetica", 17, "bold"), width=200)
        self.op.configure(state="disabled")
        self.op.pack(pady = 10, padx = 20)

        # Entry de la cadena resultante
        self.entry = ctk.CTkEntry(self, font=("Helvetica", 17, "bold"), width=400)
        self.entry.configure(state="disabled")
        self.entry.pack(pady = 10, padx = 20)
    
    # Metodo para agregar la proposicion molecular
    def setInfo(self, data):
        self.entry.configure(state="disabled")
        self.entry.insert(0, data)
        self.entry.configure(state="disabled")

    # Metodo para agregar la operacion con las variables
    def setOp(self, data):
        self.op.configure(state="normal")
        self.op.insert(0, data)
        self.op.configure(state="disabled")
