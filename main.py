from Tkinter import *

commands = []

Class dev_window:
  
  def __init__(self,root):
    
    frame = Frame(root)
    frame.pack
    
    i = Entry(root)
    i.pack
    
    comment = Text(root)
    comment.pack
    
    read = Button(root,text = "Get code", command = self.readcode(i,comment))
    read.pack
    
    options = 
    
    def readcode(self,i,out):
      text = i.get()
      comment = out.get()
      print("find comment:"+text)
      print("Write comment:"+ comment)
      
    
    
root = Tk("Reddit bot creator")

