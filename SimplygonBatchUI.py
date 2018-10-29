import tkinter as tk
import os
import ctypes


LARGE_FONT= ("Verdana", 12)
SMALL_FONT= ("Verdana", 8)
class BatchTool(tk.Tk):


    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        continer = tk.Frame(self)
        continer.pack(side="top", fill="both", expand = True)
        continer.grid_rowconfigure(0, weight=1)


        continer.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(continer, self)
        self.frames[StartPage] = frame
        frame.grid(row = 0, column = 0, sticky="nsew")
        self.show_frame(StartPage)


    def show_frame(self, cont):

        currentframe = self.frames[cont]
        currentframe.tkraise()


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Simplygon Batch Tool", font = LARGE_FONT)
        label.grid(row=0,column=0)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)

        e1label = tk.Label(self, text = "Model Path",font = SMALL_FONT)
        e2label = tk.Label(self, text = "Export Path",font = SMALL_FONT)
        e3label = tk.Label(self, text = "Simplygon Rules Template Path .spl",font = SMALL_FONT)

        e1.grid(row=1, column=1)
        e2.grid(row=2,column=1)
        e3.grid(row=3,column=1)

        e1label.grid(row=1,column=0)
        e2label.grid(row=2,column=0)
        e3label.grid(row=3,column=0)

        button1 = tk.Button(self, text="Start Batch", command=lambda:starttool(e1.get(), e2.get(), e3.get()))
        button1.grid(row=4,column=0)




def starttool(fbxstart,fbxend,rules):
    command = "\Program Files\Simplygon\8\Tools\SimplygonBatch\SimplygonBatch.exe" '"' " --Input " + str(fbxstart) + " --Output " + str(fbxend) + " --Spl " + str(rules) +" --Verbose"


    #print('"' + command + '"')
    os.system('"' + command)
    #print(command)

    #Mbox('Finished','Finished',0)
    #popup("Finished")
    print("Finished")

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def popup(msg):
    popup = tk.Tk()
    popup.wm_title("Notification")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady = 10)
    B1 = tk.Button(popup, text="Okay",command = exit())
    B1.pack()
    popup.mainloop()

app = BatchTool()

app.mainloop()
