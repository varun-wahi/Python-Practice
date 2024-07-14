import tkinter as tk
r=tk.Tk()
r.title("Calculator")
button=tk.Button(r,text="exit",width=25,height=5,
    bg='grey',command=r.destroy)
button.pack()
button2=tk.Button(r,text="+",width=25,height=5,
    bg='grey')
button2.pack()
r.mainloop()
