import tkinter as tk

from core import text2display as txtList

root = tk.Tk()
selectedEx = 0


canvas = tk.Canvas(root, height=700, width=700)


frame = tk.Frame(root, bg="white")

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

def select(index):
    selectedEx = index
    buttons=[]
    for widget in frame.winfo_children():
        widget.destroy()
    for exercise in txtList:
        callback = lambda n : lambda : select(n)
        button = tk.Button(frame, text=exercise['question'], command=callback(txtList.index(exercise)))
        button.pack()
        if txtList.index(exercise)  == selectedEx:
            print(selectedEx)
            for answer in exercise['answer']:
                label = tk.Label(frame, text=answer)
                label.pack()

buttons=[]
for exercise in txtList:
    callback = lambda n : lambda : select(n)
    button = tk.Button(frame, text=exercise['question'], command=callback(txtList.index(exercise)))
    button.pack()

root.mainloop()