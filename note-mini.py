from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

def createNewWindow():
    global newWindow
    newWindow = Tk()
    newWindow.geometry('500x500')

    global text1
    fram = Frame(newWindow)
    Label(fram,text='Text to find:').pack(side=LEFT)
    edit = Entry(fram)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    searchfind = Button(fram, text='Find')
    searchfind.pack(side=RIGHT)
    fram.pack(side=TOP)
    
    h1 = Scrollbar(newWindow, orient = 'horizontal')		
    h1.pack(side = BOTTOM, fill = X)
    v1 = Scrollbar(newWindow)		
    v1.pack(side = RIGHT, fill = Y)

    text1 = Text(newWindow, width = 500, height = 500, wrap = NONE,
			xscrollcommand = h1.set,
			yscrollcommand = v1.set, undo=True
            )

    goback = Button(newWindow, text = 'Quit without Saving', command = newWindow.destroy)
    undo = Button(newWindow, text = 'Undo', command = text1.edit_undo)
    redo = Button(newWindow, text = 'Redo', command = text1.edit_redo)
    openfile = Button(newWindow, text = 'Open File', command = openthefile)
    save = Button(newWindow, text = 'Save', command = savethefile)
    frame = Frame(newWindow)

    goback.pack(side=TOP)
    undo.place(x=340,y=26)
    redo.place(x=380,y=26)
    openfile.place(x=0,y=26)
    save.place(x=105,y=26)
    frame.pack(side=RIGHT)

    text1.pack(side=TOP, fill=X)		
    h1.config(command=text1.xview)	
    v1.config(command=text1.yview)

    def find():
        text1.tag_remove('found', '1.0', END)
        s = edit.get()
        if s:
            idx = '1.0'
            while 1:
                idx = text1.search(s, idx, nocase=1,
                                stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                text1.tag_add('found', idx, lastidx)
                idx = lastidx
            text1.tag_config('found', foreground='red')
        edit.focus_set()
    searchfind.config(command=find)

    newWindow.mainloop()

def tips():
    tipswindow = Tk()
    tipswindow.geometry('500x200')

    labeltitle = Label(tipswindow, text = 'Need some help with the program?')
    helplist = Label(tipswindow,
    text = ('''
New File   : make new file
Open File : open any available files and edit it
Doodle Area : prevent getting bored by drawing something
Help         : you currently using it right now, help list to help understanding the program
Undo        : go back to the previous thing you type/edit
Redo        : can be used after you decided to un-Undo the edit, simply press the Redo button
Save        : save your newly created file (or save the edited file one)
Kill Window : instantly destroy the window in New File, save your file before clicking the button
Quit         : destroy the program'''), justify='left')

    labeltitle.pack(side='top')
    helplist.place(x=0, y=25)

def openthefile():
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    text1.delete(1.0, END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        text1.insert(END, text)
    newWindow.title(filepath)
    
def savethefile():
    try:
        path = asksaveasfilename(defaultextension = '.txt')
        newWindow.title(path)
    
    except:
        return   
    
    with open(path, 'w') as output_file:
        output_file.write(text1.get('1.0', END))

def painter(event):
    color = 'red'
    x1,y1 = (event.x-1), (event.y-1)
    x2,y2 = (event.x+1), (event.y+1)
    cnv.create_oval(x1,y1,x2,y2, fill=color, outline=color)

def pain():
    global newWindow2
    newWindow2 = Tk()
    newWindow2.geometry()
    newWindow2.title('Doodle Area')

    doodletitle = Label(newWindow2, text = 'Drag your mouse to draw')
    doodletitle.pack(side='top')

    global cnv
    cnv = Canvas(newWindow2, width=500, height=500, bg='white')
    cnv.pack(expand=YES, fill=BOTH)
    cnv.bind('<B1-Motion>', painter)

window = Tk()
window.geometry('200x200')
note = Label(window, text='Notepad Mini\n', font=150)
new = Button(window, text = 'New Text File', command = createNewWindow)
doodlearea = Button(window, text = 'Doodle Area', command = pain)
help = Button(window, text = 'Help', command = tips)
quit = Button(window, text='Quit', command = window.destroy)

note.pack(side=TOP)
new.pack(side='top')
doodlearea.pack(side='top')
help.pack(side='top')
quit.pack(side='top')

window.mainloop()