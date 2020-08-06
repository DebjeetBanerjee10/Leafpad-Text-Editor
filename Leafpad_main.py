# importing only  those functions  
# which are needed 
from tkinter import * 
from tkinter.ttk import * 
from tkinter.filedialog import askopenfile, asksaveasfile
   
# creating tkinter window 
root = Tk() 
root.title('Leafpad') 

# initializing text area
Text_area=  Text(root,wrap = WORD,bd = 5,height = 42.5)
Text_area.pack(fill = BOTH)

# Creating Menubar 
menubar = Menu(root) 
  
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File', command = lambda:New_File()) 
file.add_command(label ='Open...', command = lambda:open_file()) 
file.add_command(label ='Save', command = lambda:save_file()) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 

# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = lambda:Text_area.event_generate("<<Cut>>")) 
edit.add_command(label ='Copy', command = lambda:Text_area.event_generate("<<Copy>>")) 
edit.add_command(label ='Paste', command = lambda:Text_area.event_generate("<<Paste>>")) 
edit.add_command(label ='Select All', command = lambda:Text_area.event_generate("<<SelectAll>>")) 
edit.add_separator() 
edit.add_command(label = 'Undo', command= lambda:Text_area.event_generate("<<Undo>>"))
edit.add_command(label = 'Redo', command = lambda:Text_area.event_generate("<<Redo>>"))

# Adding Format Menu and its command
Format = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Format', menu = Format)
Format.add_command(label = 'Font',command = lambda:font_window())

  
# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Help', command = None) 
help_.add_separator() 
help_.add_command(label ='About Leafpad', command = None) 
  
# display Menu 
root.config(menu = menubar)

#defining the function for saving a file
def save_file():
    save = asksaveasfile(mode = 'w',defaultextension = '.txt')
    if save is None:
        return
    content = str(Text_area.get(1.0, END))
    save.write(content)
    save.close()

#defining the function for opening a file
def open_file():
    open_file = askopenfile(filetypes = [('Text File','*.txt')])
    if open_file is not None:
        content = open_file.read()
        Text_area.delete(1.0, END)
        Text_area.insert(INSERT,content)

# defining functions for the font window
def font_ok():
    text_get = text_font.get()
    text_get = str(text_get)
    size_get = text_font_size.get()
    size_get = int(size_get)
    style_get = text_font_style.get()
    style_get = str(style_get)
    Text_area.config(font = (text_get,size_get,style_get))

def font_window():
    global text_font 
    global text_font_size
    global text_font_style
    
    # initializing the font window
    windows = Tk()
    windows.title('Font')
    
    #labels for each combobox
    font_label = Label(windows,text = "<<Font")
    font_label.grid(row = 5, column=10)
    size_label = Label(windows, text = "<<Size")
    size_label.grid(row = 6, column=10)
    style_label = Label(windows, text = "<<Style")
    style_label.grid(row = 7, column = 10)
    
    # combobox for font, font size and its style respectively
    text_font = Combobox(windows)
    text_font['values']=['Agency FB','Algerian','Arial','Arial Rounded MT','Arial Unicode MS','Baskerville Old Face','Bauhaus','Bell MT','Berlin Sans FB','Bernard MT','Blackadder ITC','Bodoni MT','Bradley Hand ITC','Britannic','Broadway','Brush Script MT','Calibri','Californian FB','Castellar','Chiller','Century Schoolbook','Colonna MT','Comic Sans MS','Consolas','Cooper','Copperplate Gothic','Corbel','Edwardian Script ITC','Elephant','Engravers MT','Fixedsys','Forte']
    text_font.grid(row = 5, column=3)
    text_font_size = Combobox(windows)
    text_font_size['values']=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60']
    text_font_size.grid(row = 6, column=3)
    text_font_style = Combobox(windows)
    text_font_style['values']=['normal','bold','italic','underline']
    text_font_style.grid(row=7,column=3)
    
    #ok button for finalizing the changes of fonts and cancel button for exiting the font window
    cancel_but = Button(windows, text = "Cancel", command = windows.destroy)
    cancel_but.grid(row = 8, column=10)
    ok_but = Button(windows,text = "OK", command = lambda:font_ok())
    ok_but.grid(row=8, column=5)

    #display the font window
    windows.mainloop()

#defining the New file function 
'''
The concept of new file is very simple. All we need to do is to just copy the 
whole program inside a method which we will be creating. And creating another 
method with the same commands so that it runs till the user wants to close the program.
'''
# first new file function
def New_File():
    root_2 =Tk()
    root_2.title('Leafpad')
    
    # initializing text area
    Text_area_2=  Text(root_2,wrap = WORD,bd = 5,height = 42.5)
    Text_area_2.pack(fill = BOTH)

    # Creating Menubar 
    menubar_2 = Menu(root_2) 
  
    # Adding File Menu and commands 
    file_2 = Menu(menubar_2, tearoff = 0) 
    menubar_2.add_cascade(label ='File', menu = file_2) 
    file_2.add_command(label ='New File', command = lambda:new_file()) 
    file_2.add_command(label ='Open...', command = lambda:Open_File()) 
    file_2.add_command(label ='Save', command = lambda:Save_File())     
    file_2.add_separator() 
    file_2.add_command(label ='Exit', command = root_2.destroy) 

    # Adding Edit Menu and commands 
    edit_2 = Menu(menubar_2, tearoff = 0) 
    menubar_2.add_cascade(label ='Edit', menu = edit_2) 
    edit_2.add_command(label ='Cut', command = lambda:Text_area_2.event_generate("<<Cut>>")) 
    edit_2.add_command(label ='Copy', command = lambda:Text_area_2.event_generate("<<Copy>>")) 
    edit_2.add_command(label ='Paste', command = lambda:Text_area_2.event_generate("<<Paste>>")) 
    edit_2.add_command(label ='Select All', command = lambda:Text_area_2.event_generate("<<SelectAll>>")) 
    edit_2.add_separator() 
    edit_2.add_command(label = 'Undo', command= lambda:Text_area_2.event_generate("<<Undo>>"))
    edit_2.add_command(label = 'Redo', command = lambda:Text_area_2.event_generate("<<Redo>>"))

    # Adding Format Menu and its command
    Format_2 = Menu(menubar_2, tearoff = 0)
    menubar_2.add_cascade(label ='Format', menu = Format_2)
    Format_2.add_command(label = 'Font',command = lambda:Font_Window())

  
    # Adding Help Menu 
    help_2 = Menu(menubar_2, tearoff = 0) 
    menubar_2.add_cascade(label ='Help', menu = help_2) 
    help_2.add_command(label ='Help', command = None) 
    help_2.add_separator() 
    help_2.add_command(label ='About Leafpad', command = None) 
  
    # display Menu 
    root_2.config(menu = menubar_2)

    #defining the function for saving a file
    def Save_File():
        save_2 = asksaveasfile(mode = 'w',defaultextension = '.txt')
        if save_2 is None:
            return
        content_2 = str(Text_area_2.get(1.0, END))
        save_2.write(content_2)
        save_2.close()

    #defining the function for opening a file
    def Open_File():
        open_file_2 = askopenfile(filetypes = [('Text File','*.txt')])
        if open_file_2 is not None:
            content_2 = open_file_2.read()
            Text_area_2.delete(1.0, END)
            Text_area_2.insert(INSERT,content_2)

    # defining functions for the font window
    def Font_Ok():
        text_get_2 = text_font_2.get()
        text_get_2 = str(text_get_2)
        size_get_2 = text_font_size_2.get()
        size_get_2= int(size_get_2)
        style_get_2 = text_font_style_2.get()
        style_get_2 = str(style_get_2)
        Text_area_2.config(font = (text_get_2,size_get_2,style_get_2))
    
    def Font_Window():
        global text_font_2 
        global text_font_size_2
        global text_font_style_2
        
        # initializing the font window
        wind = Tk()
        wind.title('Font')
        
        #labels for each combobox
        font_label_2 = Label(wind,text = "<<Font")
        font_label_2.grid(row = 5, column=10)
        size_label_2 = Label(wind, text = "<<Size")
        size_label_2.grid(row = 6, column=10)
        style_label_2 = Label(wind, text = "<<Style")
        style_label_2.grid(row = 7, column = 10)
        
        # combobox for font, font size and its style respectively
        text_font_2 = Combobox(wind)
        text_font_2['values']=['Agency FB','Algerian','Arial','Arial Rounded MT','Arial Unicode MS','Baskerville Old Face','Bauhaus','Bell MT','Berlin Sans FB','Bernard MT','Blackadder ITC','Bodoni MT','Bradley Hand ITC','Britannic','Broadway','Brush Script MT','Calibri','Californian FB','Castellar','Chiller','Century Schoolbook','Colonna MT','Comic Sans MS','Consolas','Cooper','Copperplate Gothic','Corbel','Edwardian Script ITC','Elephant','Engravers MT','Fixedsys','Forte']
        text_font_2.grid(row = 5, column=3)
        text_font_size_2 = Combobox(wind)
        text_font_size_2['values']=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60']
        text_font_size_2.grid(row = 6, column=3)
        text_font_style_2 = Combobox(wind)
        text_font_style_2['values']=['normal','bold','italic','underline']
        text_font_style_2.grid(row=7,column=3)
    
        #ok button for finalizing the changes of fonts and cancel button for exiting the font window
        cancel_but_2 = Button(wind, text = "Cancel", command =wind.destroy)
        cancel_but_2.grid(row = 8, column = 10)
        ok_but_2 = Button(wind,text = "OK", command = lambda:Font_Ok())
        ok_but_2.grid(row=8, column=5)

        #display the window
        wind.mainloop()

# the second new file function 
def new_file():
    root_3 =Tk()
    root_3.title('Leafpad')
    
    # initializing text area
    Text_area_3=  Text(root_3,wrap = WORD,bd = 5,height = 42.5)
    Text_area_3.pack(fill = BOTH)

    # Creating Menubar 
    menubar_3 = Menu(root_3) 
  
    # Adding File Menu and commands 
    file_3 = Menu(menubar_3, tearoff = 0) 
    menubar_3.add_cascade(label ='File', menu = file_3) 
    file_3.add_command(label ='New File', command = lambda:New_File()) 
    file_3.add_command(label ='Open...', command = lambda:Open_file()) 
    file_3.add_command(label ='Save', command = lambda:Save_file())     
    file_3.add_separator() 
    file_3.add_command(label ='Exit', command = root_3.destroy) 

    # Adding Edit Menu and commands 
    edit_3 = Menu(menubar_3, tearoff = 0) 
    menubar_3.add_cascade(label ='Edit', menu = edit_3) 
    edit_3.add_command(label ='Cut', command = lambda:Text_area_3.event_generate("<<Cut>>")) 
    edit_3.add_command(label ='Copy', command = lambda:Text_area_3.event_generate("<<Copy>>")) 
    edit_3.add_command(label ='Paste', command = lambda:Text_area_3.event_generate("<<Paste>>")) 
    edit_3.add_command(label ='Select All', command = lambda:Text_area_3.event_generate("<<SelectAll>>")) 
    edit_3.add_separator() 
    edit_3.add_command(label = 'Undo', command= lambda:Text_area_3.event_generate("<<Undo>>"))
    edit_3.add_command(label = 'Redo', command = lambda:Text_area_3.event_generate("<<Redo>>"))

    # Adding Format Menu and its command
    Format_3 = Menu(menubar_3, tearoff = 0)
    menubar_3.add_cascade(label ='Format', menu = Format_3)
    Format_3.add_command(label = 'Font',command = lambda:Font_window())

  
    # Adding Help Menu 
    help_3 = Menu(menubar_3, tearoff = 0) 
    menubar_3.add_cascade(label ='Help', menu = help_3) 
    help_3.add_command(label ='Tk Help', command = None) 
    help_3.add_command(label ='Demo', command = None) 
    help_3.add_separator() 
    help_3.add_command(label ='About Tk', command = None) 
  
    # display Menu 
    root_3.config(menu = menubar_3)

    def Save_file():
        save_3 = asksaveasfile(mode = 'w',defaultextension = '.txt')
        if save_3 is None:
            return
        content_3 = str(Text_area.get(1.0, END))
        save_3.write(content_3)
        save_3.close()

    #defining the function for opening a file
    def Open_file():
        open_file_3 = askopenfile(filetypes = [('Text File','*.txt')])
        if open_file_3 is not None:
            content_3 = open_file_2.read()
            Text_area_3.delete(1.0, END)
            Text_area_3.insert(INSERT,content_3)

    # defining functions for the font window
    def Font_OK():
        text_get_3 = text_font_3.get()
        text_get_3 = str(text_get_3)
        size_get_3 = text_font_size_3.get()
        size_get_3= int(size_get_3)
        style_get_3 = text_font_style_3.get()
        style_get_3 = str(style_get_3)
        Text_area_3.config(font = (text_get_3,size_get_3,style_get_3))
    
    def Font_window():
        global text_font_3 
        global text_font_size_3
        global text_font_style_3
        # initializing the font window
        win = Tk()
        win.title('Font')
        
        #labels for each combobox
        font_label_3 = Label(win,text = "<<Font")
        font_label_3.grid(row = 5, column=10)
        size_label_3 = Label(win, text = "<<Size")
        size_label_3.grid(row = 6, column=10)
        style_label_3 = Label(win, text = "<<Style")
        style_label_3.grid(row = 7, column = 10)
        
        # combobox for font, font size and its style respectively
        text_font_3 = Combobox(win)
        text_font_3['values']=['Agency FB','Algerian','Arial','Arial Rounded MT','Arial Unicode MS','Baskerville Old Face','Bauhaus','Bell MT','Berlin Sans FB','Bernard MT','Blackadder ITC','Bodoni MT','Bradley Hand ITC','Britannic','Broadway','Brush Script MT','Calibri','Californian FB','Castellar','Chiller','Century Schoolbook','Colonna MT','Comic Sans MS','Consolas','Cooper','Copperplate Gothic','Corbel','Edwardian Script ITC','Elephant','Engravers MT','Fixedsys','Forte']
        text_font_3.grid(row = 5, column=3)
        text_font_size_3 = Combobox(win)
        text_font_size_3['values']=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60']
        text_font_size_3.grid(row = 6, column=3)
        text_font_style_3 = Combobox(win)
        text_font_style_3['values']=['normal','bold','italic','underline']
        text_font_style_3.grid(row=7,column=3)
    
        #ok button for finalizing the changes of fonts and cancel button for exiting the font window
        cancel_but_3 = Button(win, text = "Cancel", command =win.destroy)
        cancel_but_3.grid(row = 8, column = 10)
        ok_but_3 = Button(win,text = "OK", command = lambda:Font_OK())
        ok_but_3.grid(row=8, column=5)

        #display the window
        win.mainloop()
#display the main screen
root.mainloop() 
