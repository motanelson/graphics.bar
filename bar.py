import tkinter as tk







class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("bars")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas = tk.Canvas(background="black",width=640,height=480)
        self.canvas.pack(padx=0,pady=0)
        c=self.canvas
        for a in range(0,640,40):
            
            
            c.create_rectangle(a,0,a+20,480,fill="white")
        for a in range(0,480,40):
            
            
            c.create_rectangle(0,a,640,a+20,fill="white")





root=tk.Tk()
apps=myapps(root)
root.mainloop()