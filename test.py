import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI Emoji} -size 22 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("600x450+540+213")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.original = Button(top)
        self.original.place(relx=0.683, rely=0.6, height=33, width=126)
        self.original.configure(activebackground="#d9d9d9")
        self.original.configure(activeforeground="#000000")
        self.original.configure(background="#d9d9d9")
        self.original.configure(disabledforeground="#a3a3a3")
        self.original.configure(foreground="#000000")
        self.original.configure(highlightbackground="#d9d9d9")
        self.original.configure(highlightcolor="black")
        self.original.configure(pady="0")
        self.original.configure(text='''Select Image''')
        self.original.configure(width=126)

        self.Check = Button(top)
        self.Check.place(relx=0.683, rely=0.756, height=33, width=126)
        self.Check.configure(activebackground="#d9d9d9")
        self.Check.configure(activeforeground="#000000")
        self.Check.configure(background="#d9d9d9")
        self.Check.configure(disabledforeground="#a3a3a3")
        self.Check.configure(foreground="#000000")
        self.Check.configure(highlightbackground="#d9d9d9")
        self.Check.configure(highlightcolor="black")
        self.Check.configure(pady="0")
        self.Check.configure(text='''Choose''')
        self.Check.configure(width=126)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.3, rely=0.6,height=24, relwidth=0.34)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.result = Label(top)
        self.result.place(relx=0.25, rely=0.889, height=26, width=292)
        self.result.configure(background="#d9d9d9")
        self.result.configure(disabledforeground="#a3a3a3")
        self.result.configure(foreground="#000000")
        self.result.configure(text='''Result''')
        self.result.configure(width=292)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.2, rely=0.2, height=86, width=372)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Signature Verification''')
        self.Label2.configure(width=372)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.067, rely=0.6, height=26, width=122)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''New Entry''')
        self.Label3.configure(width=122)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.067, rely=0.756, height=26, width=132)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Check''')
        self.Label4.configure(width=132)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.3, rely=0.756,height=24, relwidth=0.34)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")






if __name__ == '__main__':
    vp_start_gui()

