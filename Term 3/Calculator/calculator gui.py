#calculator
#3/19
#Logan Nelson

from tkinter import *

class Application(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
        self.pos1 = ""
        self.pos2 = ""
        self.opperator = ""
        self.displayarea = ""
    
    def create_widgets(self):
        
        """ Create entry box, buttons 0-9, all signs and 'clear' buttons """
        self.display = Entry(self, text=' ',  width = 40)
        self.display.grid(row=0, column = 0, columnspan = 4)

        
        self.button1 = Button(self, text='1', command=self.press1,height=1, width=7)
        self.button1.grid(row=1, column=0)

        self.button2 = Button(self, text='2', command=self.press2,height=1, width=7)
        self.button2.grid(row=1, column=1)

        self.button3 = Button(self, text='3', command=self.press3,height=1, width=7)
        self.button3.grid(row=1, column=2)

        self.button4 = Button(self, text='4', command=self.press4,height=1, width=7)
        self.button4.grid(row=2, column=0)

        self.button5 = Button(self, text='5', command=self.press5,height=1, width=7)
        self.button5.grid(row=2, column=1)

        self.button6 = Button(self, text='6', command=self.press6,height=1, width=7)
        self.button6.grid(row=2, column=2)

        self.button7 = Button(self, text='7', command=self.press7,height=1, width=7)
        self.button7.grid(row=3, column=0)

        self.button8 = Button(self, text='8', command=self.press8,height=1, width=7)
        self.button8.grid(row=3, column=1)

        self.button9 = Button(self, text='9', command=self.press9,height=1, width=7)
        self.button9.grid(row=3, column=2)

        self.button0 = Button(self, text='0', command=self.press0,height=1, width=7)
        self.button0.grid(row=4, column=1)

        self.addbutton = Button(self, text='+', command=self.addpress,height=1, width=7)
        self.addbutton.grid(row=1, column=3)

        self.subbutton = Button(self, text='-', command=self.subpress,height=1, width=7)
        self.subbutton.grid(row=2, column=3)

        self.multbutton = Button(self, text='*', command=self.multpress,height=1, width=7)
        self.multbutton.grid(row=3, column=3)

        self.divbutton = Button(self, text='/', command=self.divpress,height=1, width=7)
        self.divbutton.grid(row=4, column=3)

        self.equalbutton = Button(self, text='=', command=self.equpress,height=1, width=7)
        self.equalbutton.grid(row=4, column=2)

        self.delbutton = Button(self, text='clear', command=self.clrpress,height=1, width=7)
        self.delbutton.grid(row=4, column=0)
    def press1(self):
        self.displayarea += ("1")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press2(self):
        self.displayarea += ("2")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press3(self):
        self.displayarea += ("3")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press4(self):
        self.displayarea += ("4")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press5(self):
        self.displayarea += ("5")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press6(self):
        self.displayarea += ("6")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press7(self):
        self.displayarea += ("7")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press8(self):
        self.displayarea += ("8")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press9(self):
        self.displayarea += ("9")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def press0(self):
        self.displayarea += ("0")
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def addpress(self):
        self.pos1 = self.displayarea
        self.opperator = "+" 
        self.displayarea = ""
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)

    def subpress(self):
        self.pos1 = self.displayarea
        self.opperator = ("-")
        self.display.delete(0, END)
        self.displayarea = ""
        self.display.insert(0,self.displayarea)

    def divpress(self):
        self.pos1 = self.displayarea
        self.opperator = ("/")
        self.display.delete(0, END)
        self.displayarea = ""
        self.display.insert(0,self.displayarea)

    def multpress(self):
        self.pos1 = self.displayarea
        self.opperator = ("*")
        self.display.delete(0, END)
        self.displayarea = ""
        self.display.insert(0,self.displayarea)

    def clrpress(self):
        self.pos1 = ""
        self.pos2 = ""
        self.opperator = ("")
        self.display.delete(0, END)
        self.displayarea = ""
        self.display.insert(0,self.displayarea)

    def equpress(self):
        self.pos2 = self.displayarea
        self.displayarea= ""
        if self.opperator == "+":
            self.displayarea = str(int(self.pos1) + int(self.pos2))
        elif self.opperator == "-":
            self.displayarea = str(int(self.pos1) - int(self.pos2))
        elif self.opperator == "*":
            self.displayarea = str(float(self.pos1) * float(self.pos2))
        elif self.opperator == "/":
            try:
                
                self.displayarea = str(float(self.pos1) / float(self.pos2))
            except:
                self.displayarea = "Can't divide by 0"
        self.display.delete(0, END)
        self.display.insert(0,self.displayarea)
        self.pos1 = (self.displayarea)








# main
root = Tk()
root.title("Calculator")
root.geometry("250x300")
app = Application(root)
root.mainloop()
