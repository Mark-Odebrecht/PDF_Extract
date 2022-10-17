import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 640, height = 360)
canvas1.pack()

tk.filedialog.askopenfile(mode='r', **options)


root.mainloop()