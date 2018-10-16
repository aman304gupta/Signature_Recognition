import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
# from PyQt5.QtGui import QIcon
# from PyQt5 import QtCore
from keras.models import load_model
import tensorflow as tf
import cv2
import numpy as np
import sys
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

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


#Loading keras saved model

def triplet_loss(y_true, y_pred, alpha = 0.2):

    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    
    # distance between the anchor and the positive, you will need to sum over axis=-1
    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor,positive)))
    # distance between the anchor and the negative, you will need to sum over axis=-1
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor,negative)))
    basic_loss = tf.add(tf.subtract(pos_dist,neg_dist),alpha)
    loss = tf.maximum(basic_loss,0)
    return loss

FRmodel=load_model('model.h5',custom_objects={'triplet_loss':triplet_loss})
FRmodel.summary()

#image encoding

def img_to_encoding1(image_path, model):
	img1 = cv2.imread(image_path, 1)
	dim = (96,96)
	img1 = cv2.resize(img1,dim, interpolation = cv2.INTER_AREA)
	img = img1[...,::-1]
	img = np.around(np.transpose(img, (2,0,1))/255.0, decimals=12)
	x_train = np.array([img])
	embedding = model.predict_on_batch(x_train)
	return embedding

#database for verification

database = {}
# database["HJC_Peshchan"] =img_to_encoding1("genuine/NFI-00101001.png", FRmodel)
database["Vermututr"] = img_to_encoding1("genuine/NFI-00201002.png", FRmodel)
database["Yuan"] = img_to_encoding1("genuine/NFI-00301003.png", FRmodel)
database["Cbugn"] =img_to_encoding1("genuine/NFI-00401004.png", FRmodel)
database["GJ"] =img_to_encoding1("genuine/NFI-00501005.png", FRmodel)
database["Mary_Van_Camp"] =img_to_encoding1("genuine/NFI-00601006.png", FRmodel)
database["SUruin"] =img_to_encoding1("genuine/NFI-00701007.png", FRmodel)
database["Hmceycey"] =img_to_encoding1("genuine/NFI-00801008.png", FRmodel)
database["Pramod"] =img_to_encoding1("genuine/NFI-00901009.png", FRmodel)

database["Paul_J"] =img_to_encoding1("genuine/NFI-02303023.png", FRmodel)
database["Myuan_Priyush"] =img_to_encoding1("genuine/NFI-02404024.png", FRmodel)

def verify(image_path, identity, database, model):
    #encoding for the image. 
	encoding = img_to_encoding1(image_path,model)
    # distance with identity'
	dist = np.linalg.norm(encoding - database[identity])
		
	if dist < 0.7:
		print("It's " + str(identity) + ", Welcome to Bank!!!")
		door_open = True
	else:
		print("It's not " + str(identity) + ", Call the Police!!!")
		door_open = False
			
	return dist, door_open

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

        top.geometry("600x450+519+122")
        top.title("New Toplevel")
        top.configure(background="#c0d8d4")

        def buttonClick2():
            # print(self.Entry1.get())
            Tk().withdraw()
            filename=askopenfilename()
            new_entry=self.Entry1.get()
            database[new_entry]=img_to_encoding1(filename,FRmodel)
            message=new_entry+" added!!"
            messagebox.showinfo("Added",message)

        self.original = Button(top,command=buttonClick2)
        self.original.place(relx=0.683, rely=0.6, height=33, width=126)
        self.original.configure(activebackground="#d9d9d9")
        self.original.configure(activeforeground="#000000")
        self.original.configure(background="#d8c599")
        self.original.configure(disabledforeground="#a3a3a3")
        self.original.configure(foreground="#000000")
        self.original.configure(highlightbackground="#d9d9d9")
        self.original.configure(highlightcolor="black")
        self.original.configure(pady="0")
        self.original.configure(text='''Enter''')
        self.original.configure(width=126)

        def buttonClick():
            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
            print(filename)
            dist,ver=verify(filename,self.Entry2.get(),database,FRmodel)
            message1=self.Entry2.get()+" ,Welcome to bank!!"
            message2="Call the police!!"
            if ver:
                messagebox.showinfo(self.Entry2.get(),message1)
            else:
                messagebox.showinfo(self.Entry2.get(),message2)



        self.Check = Button(top,command=buttonClick)
        self.Check.place(relx=0.683, rely=0.8, height=33, width=126)
        self.Check.configure(activebackground="#d9d9d9")
        self.Check.configure(activeforeground="#000000")
        self.Check.configure(background="#d8c599")
        self.Check.configure(disabledforeground="#a3a3a3")
        self.Check.configure(foreground="#000000")
        self.Check.configure(highlightbackground="#d9d9d9")
        self.Check.configure(highlightcolor="black")
        self.Check.configure(pady="0")
        self.Check.configure(text='''Verify''')
        self.Check.configure(width=126)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.3, rely=0.6,height=24, relwidth=0.34)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = Label(top)
        self.Label2.place(relx=0.2, rely=0.2, height=86, width=372)
        self.Label2.configure(background="#bcd8ce")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Signature Verification''')
        self.Label2.configure(width=372)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.3, rely=0.511, height=26, width=202)
        self.Label3.configure(background="#d8a4d3")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''New Entry''')
        self.Label3.configure(width=202)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.3, rely=0.711, height=26, width=202)
        self.Label4.configure(background="#d8a4d3")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Check''')
        self.Label4.configure(width=202)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.3, rely=0.8,height=24, relwidth=0.34)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label5 = Label(top)
        self.Label5.place(relx=0.1, rely=0.6, height=26, width=112)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Enter Name''')
        self.Label5.configure(width=112)

        self.Label5_1 = Label(top)
        self.Label5_1.place(relx=0.1, rely=0.8, height=26, width=112)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(activeforeground="black")
        self.Label5_1.configure(background="#d9d9d9")
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''Enter Name''')



        
if __name__ == '__main__':
	vp_start_gui()