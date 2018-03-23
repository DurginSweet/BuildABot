from Tkinter import *

commands = []

Class dev_window:
  
  def __init__(self,root):
    
    frame = Frame(root)
    frame.pack
    
    in = Entry(root)
    in.pack
    
    comment = Text(root)
    comment.pack
    
    read = Button(root,text = "Get code", command = self.readcode(in,comment))
    read.pack
    
    options = 
    
    def readcode(self,in,out):
      text = in.get()
      comment = out.get()
      print("find comment:"+text)
      print("Write comment:"+ comment)
      
    
    
root = Tk("Reddit bot creator")

