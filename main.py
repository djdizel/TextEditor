import tkinter as tk
root = tk.Tk()
root.title("Текстовый редактор")
root.geometry("800x600")
editor = tk.Text()
editor.pack(fill=tk.BOTH,expand = 1)
root.mainloop()