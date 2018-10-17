# Mubeen Shahid :: email@mubeen.info
import os, sys, Tkinter
from tkFileDialog import askdirectory
from datetime import datetime

class simpleapp_tk(Tkinter.Tk):
	rootDir=""
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
	def initialize(self):
		self.grid()
		#root directory to start search in.
		self.entry1 = Tkinter.Entry(self)
		self.entry1.grid(column=3,row=1,columnspan=9,sticky='EW')
		button = Tkinter.Button(self,text=u" Select Folder: ",command=self.OnButtonClick)
		button.grid(column=0,row=1,sticky='EW')
		#search string entry field
		self.entry2 = Tkinter.Entry(self)
		self.entry2.grid(column=3,row=2,columnspan=9,sticky='EW')
		self.entry2.bind("<Return>", self.OnPressEnter)
		label0 = Tkinter.Label(self,anchor="w",fg="black",text="   Search string: ")
		label0.grid(column=0,row=2,columnspan=2,sticky='EW')
		#text label to direct about starting search.
		label1 = Tkinter.Label(self,anchor="w",fg="blue",bg="gray",text="Press Enter to search the above entered string.")
		label1.grid(column=0,row=3,columnspan=10,sticky='EW')
		#text box for search results and output comments.
		self.resultText=Tkinter.Text(self)
		self.resultText.grid(column=0, row=4, columnspan=10)
	def OnButtonClick(self):
		self.rootDir = askdirectory()
		if self.rootDir:
			self.entry1.delete(0,Tkinter.END)
			self.entry1.insert(0,self.rootDir)
	def OnPressEnter(self,event):
		if self.rootDir: 
			rootDir=self.rootDir
			searchString=str(self.entry2.get()).lower()
			header="Searching '{}' in {} .\n".format(searchString,rootDir)
			self.resultText.insert(Tkinter.END,header)
			if len(searchString)>0:
				stime=datetime.now()
				searchList =[]
				for root, directories, filenames in os.walk(rootDir):
					for filename in filenames: 
						if searchString in filename.lower():
							searchList.append(os.path.join(root,filename))
							self.resultText.insert(Tkinter.END,root.replace(rootDir,"")+"\\"+filename+"\n")
				etime=datetime.now()
				if len(searchList)==0:
					self.resultText.insert(Tkinter.END,"\n>>Sorry, no file found with the search string.")
				self.resultText.insert(Tkinter.END,"\n>>Search time: "+str(etime-stime)+"\n\n\n")
			else:
				self.resultText.insert("0.0","Please re-run the script with a search string as input.")
#
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title("Mubeen's pysearch - a simple file search tool")
    app.mainloop()