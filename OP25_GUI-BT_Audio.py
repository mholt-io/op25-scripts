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


import Tkinter as tk
import subprocess
import os
import threading

#Commands

def stopall():
    os.system("pkill -f ./rx.py")
def CMD_OP25_01():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-All.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_02():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red1.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_03():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red2.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_04():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red3.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_05():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red4.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_06():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red5.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_07():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red6.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_08():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red7.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_09():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red8.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_10():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/burbank/Burbank-Red9.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_11():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-All.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_12():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red1.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_13():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red2.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_14():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red3.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_15():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red4.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_16():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red5.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_17():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red6.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_18():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red7.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_19():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red8.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_20():
    os.system("pkill -f ./rx.py")
    os.system("cd /home/pi/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T /home/pi/op25-scripts/ici/verdugo/glendale/Glendale-Red9.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")


def main():
    mw = tk.Tk()

    #Specify the attributes for all widgets simply like this.
    mw.option_add("*Button.Background", "Teal")
    mw.option_add("*Button.Foreground", "White")

    mw.title('OP25 Repeater Selector GUI')
    #You can set the geometry attribute to change the root windows size
    mw.geometry("480x320") #800x420 You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
    mw.resizable(0, 0) #Don't allow resizing in the x or y direction

    back = tk.Frame(master=mw,bg='Grey')
    back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
    back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window

    #Buttons

    Stop_OP25 = tk.Button(wraplength=80, master=back, text='Stop OP25 Instances', command=stopall, width=9, height=3)
    Stop_OP25.grid(row=0, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=6, pady=3)
    OP25_01 = tk.Button(wraplength=80, master=back, text='All', command=CMD_OP25_01, width=9, height=3)
    OP25_01.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=6, pady=3)
    OP25_02 = tk.Button(wraplength=80, master=back, text='Red1', command=CMD_OP25_02, width=9, height=3)
    OP25_02.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=6, pady=3)
    OP25_03 = tk.Button(wraplength=80, master=back, text='Red2', command=CMD_OP25_03, width=9, height=3)
    OP25_03.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=6, pady=3)
    OP25_04 = tk.Button(wraplength=80, master=back, text='Red3', command=CMD_OP25_04, width=9, height=3)
    OP25_04.grid(row=1, column=4, sticky=tk.W+tk.E+tk.N+tk.S, padx=6, pady=3)
    OP25_06 = tk.Button(wraplength=80, master=back, text='Red5', command=CMD_OP25_06, width=9, height=3)
    OP25_06.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_07 = tk.Button(wraplength=80, master=back, text='Red6', command=CMD_OP25_07, width=9, height=3)
    OP25_07.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_08 = tk.Button(wraplength=80, master=back, text='Red7', command=CMD_OP25_08, width=9, height=3)
    OP25_08.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_09 = tk.Button(wraplength=80, master=back, text='Red8', command=CMD_OP25_09, width=9, height=3)
    OP25_09.grid(row=2, column=4, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_11 = tk.Button(wraplength=80, master=back, text='All', command=CMD_OP25_11, width=9, height=3)
    OP25_11.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_12 = tk.Button(wraplength=80, master=back, text='Red1', command=CMD_OP25_12, width=9, height=3)
    OP25_12.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_13 = tk.Button(wraplength=80, master=back, text='Red2', command=CMD_OP25_13, width=9, height=3)
    OP25_13.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_14 = tk.Button(wraplength=80, master=back, text='Red3.', command=CMD_OP25_14, width=9, height=3)
    OP25_14.grid(row=3, column=4, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_16 = tk.Button(wraplength=80, master=back, text='Red5', command=CMD_OP25_16, width=9, height=3)
    OP25_16.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_17 = tk.Button(wraplength=80, master=back, text='Red6', command=CMD_OP25_17, width=9, height=3)
    OP25_17.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_18 = tk.Button(wraplength=80, master=back, text='Red7', command=CMD_OP25_18, width=9, height=3)
    OP25_18.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    OP25_19 = tk.Button(wraplength=80, master=back, text='Red8', command=CMD_OP25_19, width=9, height=3)
    OP25_19.grid(row=4, column=4, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=5)
    close = tk.Button(wraplength=80, master=back, text='Quit', command=mw.destroy)
    close.pack(side='bottom')

    mw.mainloop()

if __name__ == '__main__':
    main()
