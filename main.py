import tkinter as tk
#главное окно
root = tk.Tk()
root.title("Текстовый редактор")
root.geometry("800x600")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

editor = tk.Text(root, wrap=tk.WORD)
editor.pack(fill=tk.BOTH, expand=1)
# прокрутка
scrollbar = tk.Scrollbar(root, command=editor.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
editor.config(yscrollcommand=scrollbar.set)
# функиции для изменения текста 
def apply_bold():
    try:
        # Проверяем, есть ли уже тег "bold" на выделенном тексте
        current_tags = editor.tag_names("sel.first")
        if "bold" in current_tags:
            editor.tag_remove("bold", "sel.first", "sel.last")
        else:
            editor.tag_configure("bold", font=("Arial", 12, "bold"))
            editor.tag_add("bold", "sel.first", "sel.last")
    except tk.TclError:
        print("Выделите текст, чтобы применить жирный стиль.")

def apply_italic():
    try:
        current_tags = editor.tag_names("sel.first")
        if "italic" in current_tags:
            editor.tag_remove("italic", "sel.first", "sel.last")
        else:
            editor.tag_configure("italic", font=("Arial", 12, "italic"))
            editor.tag_add("italic", "sel.first", "sel.last")
    except tk.TclError:
        print("Выделите текст, чтобы применить курсив.")

def change_font_size(size):
    try:
        tag_name = f"size{size}"
        editor.tag_configure(tag_name, font=("Arial", size))
        editor.tag_add(tag_name, "sel.first", "sel.last")
    except tk.TclError:
        print("Выделите текст, чтобы изменить размер шрифта.")
# панель инструментов
toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)
# кнопки стилей
bold_button = tk.Button(toolbar, text="Bold", command=apply_bold)
bold_button.pack(side=tk.LEFT, padx=5, pady=5)

italic_button = tk.Button(toolbar, text="Italic", command=apply_italic)
italic_button.pack(side=tk.LEFT, padx=5, pady=5)
# изменение размера шрифта 
font_size_button = tk.Button(toolbar, text="Increase Size", command=lambda: change_font_size(16))
font_size_button.pack(side=tk.LEFT, padx=5, pady=5)

font_size_small_button = tk.Button(toolbar, text="Decrease Size", command=lambda: change_font_size(10))
font_size_small_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()