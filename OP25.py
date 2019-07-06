#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  OP25_GUI.py
#
#  2019; Alex Bowman
#
#  This is free and unencumbered software released into the public domain.
#
#  Anyone is free to copy, modify, publish, use, compile, sell, or
#  distribute this software, either in source code form or as a compiled
#  binary, for any purpose, commercial or non-commercial, and by any
#  means.
#
#  In jurisdictions that recognize copyright laws, the author or authors
#  of this software dedicate any and all copyright interest in the
#  software to the public domain. We make this dedication for the benefit
#  of the public at large and to the detriment of our heirs and
#  successors. We intend this dedication to be an overt act of
#  relinquishment in perpetuity of all present and future rights to this
#  software under copyright law.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#  OTHER DEALINGS IN THE SOFTWARE.
#
#  For more information, please refer to <http://unlicense.org/>
import tkinter as tk
import os
import threading
import OP25CMD
import atexit
#Commands
def stopall():
    os.system("pkill -f ./rx.py")

def closeall(self):
    stopall
    self.mw.destroy()

class OP25_GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mw = tk.Tk()
        self.Favorites()
        atexit.register(stopall)


    def Menu_Main(self):
            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - Main Menu')
            #You can set the geometry attribute to change the root windows size
            #self.mw.geometry("480x320") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.attributes('-fullscreen', True)
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=closeall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Main, width=8, height=2)
            GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
            Button_Burbank = tk.Button(master=back, text='Burbank', command=self.Burbank, width=14, height=2)
            Button_Burbank.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_Glendale = tk.Button(master=back, text='Glendale', command=self.Glendale, width=14, height=2)
            Button_Glendale.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_Pasadena = tk.Button(master=back, text='Pasadena', command=self.Pasadena, width=14, height=2)
            Button_Pasadena.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)
            Button_close.grid(row=5, column=2, padx=9, pady=8)
            #self.mw.mainloop()

    def Favorites(self):
            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - Favorites')
            #You can set the geometry attribute to change the root windows size
            #self.mw.geometry("480x320") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.attributes('-fullscreen', True)
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=closeall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Main, width=8, height=2)
            GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
            Button_1 = tk.Button(master=back, text='BRK - Verdugo All', command=OP25CMD.Burbank.Verdugo_All, width=14, height=2)
            Button_1.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_2 = tk.Button(master=back, text='GLN - Verdugo All', command=OP25CMD.Glendale.Verdugo_All, width=14, height=2)
            Button_2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_3 = tk.Button(master=back, text='PSD - Verdugo All', command=OP25CMD.Pasadena.Verdugo_All, width=14, height=2)
            Button_3.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_4 = tk.Button(master=back, text='BRK - Verdugo Red 1', command=OP25CMD.Burbank.Verdugo_Red1, width=14, height=2)
            Button_4.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_5 = tk.Button(master=back, text='GLN - Verdugo Red 1', command=OP25CMD.Glendale.Verdugo_Red1, width=14, height=2)
            Button_5.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_6 = tk.Button(master=back, text='PSD - Verdugo Red 1', command=OP25CMD.Pasadena.Verdugo_Red1, width=14, height=2)
            Button_6.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_7 = tk.Button(master=back, text='BUR - Burbank PD', command=OP25CMD.Burbank.BPD, width=14, height=2)
            Button_7.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_8 = tk.Button(master=back, text='GLN - Burbank PD', command=OP25CMD.Glendale.BPD, width=14, height=2)
            Button_8.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_9 = tk.Button(master=back, text='GLN - Burbank PD', command=OP25CMD.Pasadena.BPD, width=14, height=2)
            Button_9.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_10 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_10.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_11 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_11.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_12 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_12.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)
            Button_close.grid(row=5, column=2, padx=9, pady=8)
            #self.mw.mainloop()

    def Burbank(self):
            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - Burbank')
            #You can set the geometry attribute to change the root windows size
            #self.mw.geometry("480x320") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.attributes('-fullscreen', True)
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=closeall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Main, width=8, height=2)
            GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
            Button_1 = tk.Button(master=back, text='Verdugo Fire', command=self.Burbank_Verudgo, width=14, height=2)
            Button_1.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_2 = tk.Button(master=back, text='Burbank PD', command=OP25CMD.Burbank.BPD, width=14, height=2)
            Button_2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_3 = tk.Button(master=back, text='Glendale PD', command=OP25CMD.Burbank.GPD, width=14, height=2)
            Button_3.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_4 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_4.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_5 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_5.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_6 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_6.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_7 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_7.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_8 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_8.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_9 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_9.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_10 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_10.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_11 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_11.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_12 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_12.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)
            Button_close.grid(row=5, column=2, padx=9, pady=8)
            #self.mw.mainloop()

    def Burbank_Verudgo(self):
            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - Burbank Verdugo')
            #You can set the geometry attribute to change the root windows size
            #self.mw.geometry("480x320") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.attributes('-fullscreen', True)
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=closeall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Main, width=8, height=2)
            GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
            Button_1 = tk.Button(master=back, text='Red 1', command=OP25CMD.Burbank.Verdugo_Red1, width=14, height=2)
            Button_1.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_2 = tk.Button(master=back, text='Red 2', command=OP25CMD.Burbank.Verdugo_Red2, width=14, height=2)
            Button_2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_3 = tk.Button(master=back, text='Red 3', command=OP25CMD.Burbank.Verdugo_Red3, width=14, height=2)
            Button_3.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_4 = tk.Button(master=back, text='Red 4', command=OP25CMD.Burbank.Verdugo_Red4, width=14, height=2)
            Button_4.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_5 = tk.Button(master=back, text='Red 5', command=OP25CMD.Burbank.Verdugo_Red5, width=14, height=2)
            Button_5.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_6 = tk.Button(master=back, text='Red 6', command=OP25CMD.Burbank.Verdugo_Red6, width=14, height=2)
            Button_6.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_7 = tk.Button(master=back, text='Red 7', command=OP25CMD.Burbank.Verdugo_Red7, width=14, height=2)
            Button_7.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_8 = tk.Button(master=back, text='Red 8', command=OP25CMD.Burbank.Verdugo_Red8, width=14, height=2)
            Button_8.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_9 = tk.Button(master=back, text='Red 9', command=OP25CMD.Burbank.Verdugo_Red9, width=14, height=2)
            Button_9.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_10 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_10.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_11 = tk.Button(master=back, text='All', command=OP25CMD.Burbank.Verdugo_All, width=14, height=2)
            Button_11.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_12 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_12.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)
            Button_close.grid(row=5, column=2, padx=9, pady=8)
            #self.mw.mainloop()

    def Glendale(self):
            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - Glendale')
            #You can set the geometry attribute to change the root windows size
            #self.mw.geometry("480x320") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.attributes('-fullscreen', True)
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=closeall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Main, width=8, height=2)
            GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
            Button_1 = tk.Button(master=back, text='Verdugo Fire', command=self.Glendale_Verudgo, width=14, height=2)
            Button_1.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_2 = tk.Button(master=back, text='Burbank PD', command=self.Menu_Main, width=14, height=2)
            Button_2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_3 = tk.Button(master=back, text='Glendale PD', command=self.Menu_Main, width=14, height=2)
            Button_3.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_4 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_4.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_5 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_5.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_6 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_6.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_7 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_7.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_8 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_8.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_9 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_9.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_10 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_10.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_11 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_11.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_12 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_12.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)
            Button_close.grid(row=5, column=2, padx=9, pady=8)
            #self.mw.mainloop()

    def Glendale_Verudgo(self):
            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - Glendale Verdugo')
            #You can set the geometry attribute to change the root windows size
            #self.mw.geometry("480x320") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.attributes('-fullscreen', True)
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=closeall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Main, width=8, height=2)
            GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
            Button_1 = tk.Button(master=back, text='Red 1', command=OP25CMD.Glendale.Verdugo_Red1, width=14, height=2)
            Button_1.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_2 = tk.Button(master=back, text='Red 2', command=OP25CMD.Glendale.Verdugo_Red2, width=14, height=2)
            Button_2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_3 = tk.Button(master=back, text='Red 3', command=OP25CMD.Glendale.Verdugo_Red3, width=14, height=2)
            Button_3.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_4 = tk.Button(master=back, text='Red 4', command=OP25CMD.Glendale.Verdugo_Red4, width=14, height=2)
            Button_4.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_5 = tk.Button(master=back, text='Red 5', command=OP25CMD.Glendale.Verdugo_Red5, width=14, height=2)
            Button_5.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_6 = tk.Button(master=back, text='Red 6', command=OP25CMD.Glendale.Verdugo_Red6, width=14, height=2)
            Button_6.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_7 = tk.Button(master=back, text='Red 7', command=OP25CMD.Glendale.Verdugo_Red7, width=14, height=2)
            Button_7.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_8 = tk.Button(master=back, text='Red 8', command=OP25CMD.Glendale.Verdugo_Red8, width=14, height=2)
            Button_8.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_9 = tk.Button(master=back, text='Red 9', command=OP25CMD.Glendale.Verdugo_Red9, width=14, height=2)
            Button_9.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_10 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_10.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_11 = tk.Button(master=back, text='All', command=OP25CMD.Glendale.Verdugo_All, width=14, height=2)
            Button_11.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_12 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_12.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)
            Button_close.grid(row=5, column=2, padx=9, pady=8)
            #self.mw.mainloop()


    def Pasadena(self):
            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - Pasadena')
            #You can set the geometry attribute to change the root windows size
            #self.mw.geometry("480x320") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.attributes('-fullscreen', True)
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=closeall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Main, width=8, height=2)
            GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
            Button_1 = tk.Button(master=back, text='Verdugo Fire', command=self.Pasadena_Verdugo, width=14, height=2)
            Button_1.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_2 = tk.Button(master=back, text='Burbank PD', command=self.Menu_Main, width=14, height=2)
            Button_2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_3 = tk.Button(master=back, text='Glendale PD', command=self.Menu_Main, width=14, height=2)
            Button_3.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_4 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_4.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_5 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_5.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_6 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_6.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_7 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_7.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_8 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_8.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_9 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_9.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_10 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_10.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_11 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_11.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_12 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_12.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)
            Button_close.grid(row=5, column=2, padx=9, pady=8)
            #self.mw.mainloop()

    def Pasadena_Verdugo(self):
            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - Pasdaenda Verdugo')
            #You can set the geometry attribute to change the root windows size
            #self.mw.geometry("480x320") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.attributes('-fullscreen', True)
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=closeall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Main, width=8, height=2)
            GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
            Button_1 = tk.Button(master=back, text='Red 1', command=OP25CMD.Pasadena.Verdugo_Red1, width=14, height=2)
            Button_1.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_2 = tk.Button(master=back, text='Red 2', command=OP25CMD.Pasadena.Verdugo_Red2, width=14, height=2)
            Button_2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_3 = tk.Button(master=back, text='Red 3', command=OP25CMD.Pasadena.Verdugo_Red3, width=14, height=2)
            Button_3.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=6)
            Button_4 = tk.Button(master=back, text='Red 4', command=OP25CMD.Pasadena.Verdugo_Red4, width=14, height=2)
            Button_4.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_5 = tk.Button(master=back, text='Red 5', command=OP25CMD.Pasadena.Verdugo_Red5, width=14, height=2)
            Button_5.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_6 = tk.Button(master=back, text='Red 6', command=OP25CMD.Pasadena.Verdugo_Red6, width=14, height=2)
            Button_6.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_7 = tk.Button(master=back, text='Red 7', command=OP25CMD.Pasadena.Verdugo_Red7, width=14, height=2)
            Button_7.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_8 = tk.Button(master=back, text='Red 8', command=OP25CMD.Pasadena.Verdugo_Red8, width=14, height=2)
            Button_8.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_9 = tk.Button(master=back, text='Red 9', command=OP25CMD.Pasadena.Verdugo_Red9, width=14, height=2)
            Button_9.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_10 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_10.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_11 = tk.Button(master=back, text='All', command=OP25CMD.Pasadena.Verdugo_All, width=14, height=2)
            Button_11.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_12 = tk.Button(master=back, text='', command='', width=14, height=2)
            Button_12.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)
            Button_close.grid(row=5, column=2, padx=9, pady=8)
            #self.mw.mainloop()






# #self.mw.mainloop()
if __name__ == '__main__':
    OP25_GUI().mw.mainloop()
