import tkinter as tk


root = tk.Tk()

def onClick():
  print("Training")

def onClick1():
  print("Testing")

root.geometry("300x200")
root.title("Speaker Identification")

label = tk.Label(root, text="")
label.pack()

button1 = tk.Button(root, text="Train", command=onClick)
button1.pack()

button2 = tk.Button(root, text="Test", command=onClick1)
button2.pack()

root.mainloop()
