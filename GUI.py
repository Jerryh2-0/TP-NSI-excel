import tkinter as tk
from tkinter import ttk

from core import text2display as txtList


selectedEx = 0

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)


def select(index):
    selectedEx = index
    buttons=[]
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    for exercise in txtList:
        callback = lambda n : lambda : select(n)
        button = tk.Button(scrollable_frame, text=exercise['question'], command=callback(txtList.index(exercise)))
        button.pack()
        if txtList.index(exercise)  == selectedEx:
            for answer in exercise['answer']:
                label = tk.Label(scrollable_frame, text=answer)
                label.pack()


buttons=[]
for exercise in txtList:
    callback = lambda n : lambda : select(n)
    button = tk.Button(scrollable_frame, text=exercise['question'], command=callback(txtList.index(exercise)))
    button.pack()

container.pack(fill="both", expand=True, padx=20, pady=20)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.attributes('-fullscreen', True)

root.mainloop()
