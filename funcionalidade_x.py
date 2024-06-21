
import tkinter as tk

# Criar a janela
root = tk.Tk()
root.title("Minha Aplicação Customizada")
root.geometry("600x400")

# Adicionar widgets
label = tk.Label(root, text="Olá, Mundo!")
label.pack()

# Executar a aplicação
root.mainloop()