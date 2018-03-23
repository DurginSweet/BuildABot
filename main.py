from Tkinter import *

commands = []

Class dev_window:
  
  def __init__(self,root):
    
    frame = Frame(root)
    frame.pack
    
    in = Entry(root)
    in.pack
    
    read = Button(root,text = "Get code", command = self.readcode,in)
    read.pack
    
    def readcode(self,in):
      text = in.get()
      print(text)
    
    
root = Tk("Reddit bot creator")

