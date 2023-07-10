import customtkinter as ctk

class savedFrame(ctk.CTkScrollableFrame):
  def __init__(self, master, props, clearProps, used):
    super().__init__(master)
    # Info del frame
    self.label = ctk.CTkLabel(self, text="Proposiciones Añadidas", font=("Helvetica", 18, "bold"))
    self.label.pack(pady=20)
    # Proposiciones
    self.props = props
    self.clearProps = clearProps
    self.used = used
    self.savedFrames = []

  def newFrame(self, frame):
    frame.pack(pady=10)
    self.savedFrames.append(frame)
