#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# Author:-Omar Faruk
# Program Name:-Encryptho
# Created:Mon 11:55AM November 12 2018
try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        print("You dont have tkinter module.please install it by[sudo apt-get install python-tk]")

try:
    import ttk
    py3 = False
except ImportError:
    try:
        import tkinter.ttk as ttk
        py3 = True
    except ImportError:
        print("You dont have tkinter module.please install it by[sudo apt-get install python-tk]")

try:
    from cryptography.fernet import Fernet
    import tkinter.messagebox as ttm
except ImportError:
    temp="[pip3 install cryptography]" if py3==True else "[pip install cryptography]"
    print("You Dont Have Cryptography Module"+" please install it by "+temp)

def start_gui():
    '''Starting point when module is the main routine.'''
    root = tk.Tk()
    top = Main_conf_Gui (root)
    root.mainloop()

class Main_conf_Gui:
    def encrypt(self,text):
        key=self.key
        en=Fernet(key).encrypt(bytes(text,"utf-8"))
        return en
    def decrypt(self,key,en_text):
        de=Fernet(key).decrypt(bytes(en_text,"utf-8"))
        return de
    def error_msg_box(self,errormsg):
        ttm.showinfo("Error!",errormsg)
    def show_key(self,key):
        # ttm.askokcancel("Encryption Key!",key)
        keybox=tk.Tk()
        keybox.geometry("400x150")
        keybox.title("Encryption Key!")
        keybox.configure(background="#4785ff")
        #text box
        keytext=tk.Text(keybox)
        keytext.place(relx=0.100, rely=0.15, relheight=0.600, relwidth=0.800)
        keytext.configure(background="#f7f7f7")
        keytext.configure(font=self.font12)
        keytext.configure(foreground="#4785ff")
        keytext.configure(insertborderwidth="5")
        keytext.configure(selectbackground="#c4c4c4")
        keytext.configure(width=236)
        keytext.configure(wrap='word')
        keytext.insert(1.0,self.key.decode())
        keytext.configure(height=100)
        #button 
        keybutton=tk.Button(keybox)
        keybutton.configure(activebackground="#3f49d8")
        keybutton.configure(activeforeground="white")
        keybutton.configure(background="#ffffff")
        keybutton.configure(borderwidth="0")
        keybutton.configure(foreground="#4785ff")
        keybutton.configure(relief='flat')
        keybutton.configure(text='''Ok''')
        keybutton.configure(width=49)
        keybutton.configure(command=lambda:keybox.destroy())
        keybutton.pack(side="bottom")
        tk.Label(keybox,text="Encryption Key In the box",font=10,background="#4785ff",foreground="#ffffff").pack(side="top")    
    def key_ask(self,text):
        self.keybox=tk.Tk()
        self.keybox.geometry("400x230")
        self.keybox.title("Decryption Key!")
        self.keybox.configure(background="#4785ff")
        #text box
        self.keytext=tk.Text(self.keybox)
        self.keytext.place(relx=0.100, rely=0.1, relheight=0.600, relwidth=0.800)
        self.keytext.configure(background="#f7f7f7")
        self.keytext.configure(font=self.font12)
        self.keytext.configure(foreground="#4785ff")
        self.keytext.configure(insertborderwidth="5")
        self.keytext.configure(selectbackground="#c4c4c4")
        self.keytext.configure(width=236)
        self.keytext.configure(wrap='word')
        # self.keytext.insert(1.0,self.key.decode())
        self.keytext.configure(height=100)
        #button 
        keybutton=tk.Button(self.keybox)
        keybutton.configure(activebackground="#3f49d8")
        keybutton.configure(activeforeground="white")
        keybutton.configure(background="#ffffff")
        keybutton.configure(borderwidth="0")
        keybutton.configure(foreground="#4785ff")
        keybutton.configure(relief='flat')
        keybutton.configure(text='''Cancel''')
        keybutton.configure(width=49)
        keybutton.configure(command=lambda:self.keybox.destroy())
        keybutton.pack(side="bottom")

        keybutton1=tk.Button(self.keybox)
        keybutton1.configure(activebackground="#3f49d8")
        keybutton1.configure(activeforeground="white")
        keybutton1.configure(background="#ffffff")
        keybutton1.configure(borderwidth="0")
        keybutton1.configure(foreground="#4785ff")
        keybutton1.configure(relief='flat')
        keybutton1.configure(text='''OK''')
        keybutton1.configure(width=49)
        keybutton1.configure(command=lambda:self.OK(text))
        keybutton1.pack(side="bottom")

        tk.Label(self.keybox,text="Put Encryption Key In the box",font=10,background="#4785ff",foreground="#ffffff").pack(side="top")
    def OK(self,text):
        key=self.keytext.get("0.0","end")
        if key=="\n":
            self.error_msg_box("Please put encryption key The box")
        else:
            try:
                self.Text4.delete("0.0","end")
                de=self.decrypt(key,text)
                self.Text4.insert("0.0",de)
                self.keybox.destroy()
            except Exception as ex:
                self.error_msg_box(ex)
    def button_click_en(self):
        self.key=Fernet.generate_key()
        text=self.Text1.get("0.0","end")
        check=self.Text2.get("0.0","end")
        if text=="\n":
            self.error_msg_box("Please Write Something In The box")
        else:
            try:
                self.Text2.delete("0.0", "end")
                self.show_key(self.key)
                en_text=self.encrypt(text)
                self.Text2.insert(0.0,en_text)
            except Exception as ex:
                self.error_msg_box(ex)
    def button_click_de(self):
        text=self.Text3.get("0.0","end")
        if text=="\n":
            self.error_msg_box("Please Write Something In The box")
        else:
            self.key_ask(text)
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#4785ff'  # X11 color: 'liteblue'
        _fgcolor = '#ffffff'  # X11 color: 'white'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.font10 = "-family Ani -size 16 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        self.font11 = "-family Chilanka -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.font12 = "-family AnjaliOldLipi -size 19 -weight normal -slant"  \
            " italic -underline 0 -overstrike 0"

        top.geometry("607x600")
        top.title("Encryptho")
        top.configure(borderwidth="20")
        top.configure(relief="sunken")
        top.configure(background="#3f49d8")
        top.configure(height="200")
        top.configure(takefocus="1")
        top.configure(width="500")

        self.menubar = tk.Menu(top,font=self.font10,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.049, rely=0.217, relheight=0.223, relwidth=0.389)

        self.Text1.configure(background="#4785ff")
        self.Text1.configure(borderwidth="0")
        self.Text1.configure(font=self.font11)
        self.Text1.configure(foreground="#f7f7f7")
        self.Text1.configure(insertborderwidth="5")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=236)
        self.Text1.configure(wrap='word')

        self.Text2 = tk.Text(top)
        self.Text2.place(relx=0.56, rely=0.217, relheight=0.223, relwidth=0.389)
        self.Text2.configure(background="#4785ff")
        self.Text2.configure(borderwidth="0")
        self.Text2.configure(font=self.font11)
        self.Text2.configure(foreground="#f7f7f7")
        self.Text2.configure(insertborderwidth="5")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(width=236)
        self.Text2.configure(wrap='word')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.049, rely=0.133, height=31, width=229)
        self.Label2.configure(activebackground="#3f49d8")
        self.Label2.configure(activeforeground="white")
        self.Label2.configure(background="#3f49d8")
        self.Label2.configure(font=self.font10)
        self.Label2.configure(foreground="#50b9d3")
        self.Label2.configure(text='''Orginal Text''')
        self.Label2.configure(width=229)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.56, rely=0.133, height=41, width=239)
        self.Label3.configure(activebackground="#3f49d8")
        self.Label3.configure(activeforeground="white")
        self.Label3.configure(background="#3f49d8")
        self.Label3.configure(font=self.font10)
        self.Label3.configure(foreground="#50b9d3")
        self.Label3.configure(text='''Encrypt Text''')
        self.Label3.configure(width=229)



        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.049, rely=0.617, height=41, width=229)
        self.Label4.configure(activebackground="#3f49d8")
        self.Label4.configure(activeforeground="white")
        self.Label4.configure(background="#3f49d8")
        self.Label4.configure(font=self.font10)
        self.Label4.configure(foreground="#50b9d3")
        self.Label4.configure(text='''Encrypted Text''')
        self.Label4.configure(width=229)


        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.56, rely=0.617, height=41, width=229)
        self.Label5.configure(activebackground="#3f49d8")
        self.Label5.configure(activeforeground="white")
        self.Label5.configure(background="#3f49d8")
        self.Label5.configure(font=self.font10)
        self.Label5.configure(foreground="#50b9d3")
        self.Label5.configure(text='''Orginal Text''')
        self.Label5.configure(width=229)


        self.Text3 = tk.Text(top)
        self.Text3.place(relx=0.049, rely=0.7, relheight=0.223, relwidth=0.389)
        self.Text3.configure(background="#4785ff")
        self.Text3.configure(borderwidth="0")
        self.Text3.configure(font=self.font11)
        self.Text3.configure(foreground="#f7f7f7")
        self.Text3.configure(insertborderwidth="5")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(width=236)
        self.Text3.configure(wrap='word')

        self.Text4 = tk.Text(top)
        self.Text4.place(relx=0.56, rely=0.7, relheight=0.223, relwidth=0.389)
        self.Text4.configure(background="#4785ff")
        self.Text4.configure(borderwidth="0")
        self.Text4.configure(font=self.font11)
        self.Text4.configure(foreground="#f7f7f7")
        self.Text4.configure(insertborderwidth="5")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(width=236)
        self.Text4.configure(wrap='word')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.461, rely=0.3, height=29, width=49)
        self.Button1.configure(activebackground="#3f49d8")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(background="#3f49d8")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(relief='flat')
        self.Button1.configure(text='''---->''')
        self.Button1.configure(width=49)
        self.Button1.configure(command=self.button_click_en)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.461, rely=0.783, height=29, width=49)
        self.Button2.configure(activebackground="#3f49d8")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(background="#3f49d8")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(relief='flat')
        self.Button2.configure(text='''---->''')
        self.Button2.configure(width=49)
        self.Button2.configure(command=self.button_click_de)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.115, rely=0.05, height=51, width=449)
        self.Label1.configure(activebackground="#3f49d8")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(background="#3f49d8")
        self.Label1.configure(font=self.font12)
        self.Label1.configure(foreground="#00f7ff")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''Encryption''')
        self.Label1.configure(width=449)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.115, rely=0.483, height=51, width=449)
        self.Label6.configure(activebackground="#3f49d8")
        self.Label6.configure(activeforeground="white")
        self.Label6.configure(background="#3f49d8")
        self.Label6.configure(font=self.font12)
        self.Label6.configure(foreground="#00f7ff")
        self.Label6.configure(justify='left')
        self.Label6.configure(text='''Decryption''')
        self.Label6.configure(width=449)

if __name__ == '__main__':
    start_gui()