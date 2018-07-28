from tkinter import *

class Textbox():
	def __init__(self):
		self.Master = Tk()
		self.Entry=Entry(self.Master)
		self.Entry.pack()
		self.Button=Button(self.Master,text="Submit",command=self.Return)
		self.Button.pack()            

		self.Master.mainloop()

	def Return(self):
		self.TempVar=self.Entry.get()
		self.Master.destroy()