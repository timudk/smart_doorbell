from tkinter import *

class Textbox():
	def __init__(self):
		self.master = Tk()

		self.entry = Entry(self.master)
		self.entry.pack()

		self.button = Button(self.master,text="Submit",command=self.return_variable)
		self.button.pack()            

		self.master.mainloop()

	def return_variable(self):
		self.temp_var = self.entry.get()
		self.master.destroy()