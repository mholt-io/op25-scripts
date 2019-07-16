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
import atexit
import sys
# import OP25Menu
from itertools import islice
from subprocess import Popen, PIPE
from textwrap import dedent
from queue import Queue, Empty
from threading import Thread
import re
# Menu Notes
'''
1) Global Variables should be created to define each menu with a prefix of "Menu_"
2) The type can either be "Play" or "Menu"
3) "Play" will generate a play command using the City and Group values in lowercase.  Do not use Spaces.  Format is <tsv_files_path>/city/group.tsv
4) "Menu" will generate another menu.  In order for this to work you have to define a Menu variable.  Do not use Spaces.  Format is Menu_city_group
5) If you want the button to be blank leave the all fields empty.  If you do not want the button to exist comment out or delete the entry.
6) Button Numbers read left to right.
'''

# Menu_Template (Menu_city_group)
Menu_Template = {
          1: {'name': '', 'type': '', 'city': '', 'group': ''},
          2: {'name': '', 'type': '', 'city': '', 'group': ''},
          3: {'name': '', 'type': '', 'city': '', 'group': ''},
          4: {'name': '', 'type': '', 'city': '', 'group': ''},
          5: {'name': '', 'type': '', 'city': '', 'group': ''},
          6: {'name': '', 'type': '', 'city': '', 'group': ''},
          7: {'name': '', 'type': '', 'city': '', 'group': ''},
          8: {'name': '', 'type': '', 'city': '', 'group': ''},
          9: {'name': '', 'type': '', 'city': '', 'group': ''},
          10: {'name': '', 'type': '', 'city': '', 'group': ''},
          11: {'name': '', 'type': '', 'city': '', 'group': ''},
          12: {'name': '', 'type': '', 'city': '', 'group': ''},
          13: {'name': '', 'type': '', 'city': '', 'group': ''},
          14: {'name': '', 'type': '', 'city': '', 'group': ''},
          15: {'name': '', 'type': '', 'city': '', 'group': ''},
         }

# Menu_Favorites
Menu_Favorites = {
           1: {'name': 'BRK - Verdugo', 'type': 'play', 'city': 'Burbank', 'group': 'Verdugo_All'},
           2: {'name': 'GLN - Verdugo', 'type': 'play', 'city': 'Glendale', 'group': 'Verdugo_All'},
           3: {'name': 'PSD - Verdugo', 'type': 'play', 'city': 'Pasdaenda', 'group': 'Verdugo_All'},
           4: {'name': 'BRK - BPD', 'type': 'play', 'city': 'Burbank', 'group': 'BPD'},
           5: {'name': 'GLN - BPD', 'type': 'play', 'city': 'Glendale', 'group': 'BPD'},
           6: {'name': 'PSD - BPD', 'type': 'play', 'city': 'Pasadena', 'group': 'BPD'},
           7: {'name': 'BRK - GPD', 'type': 'play', 'city': 'Burbank', 'group': 'GPD'},
           8: {'name': 'GLN - GPD', 'type': 'play', 'city': 'Glendale', 'group': 'GPD'},
           9: {'name': 'PSD - GPD', 'type': 'play', 'city': 'Pasadena', 'group': 'GPD'},
           10: {'name': 'BRK - ICI', 'type': 'play', 'city': 'Burbank', 'group': 'ICI'},
           11: {'name': 'GLN - ICI', 'type': 'play', 'city': 'Glendale', 'group': 'ICI'},
           12: {'name': 'PSD - ICI', 'type': 'play', 'city': 'Pasadena', 'group': 'ICI'},
           13: {'name': 'BRK - ALL EMCOM', 'type': 'play', 'city': 'Burbank', 'group': 'all_emcom'},
           14: {'name': 'GLN - ALL EMCOM', 'type': 'play', 'city': 'Glendale', 'group': 'all_emcom'},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }

# Menu_Favorites2
Menu_Favorites2 = {
           1: {'name': 'BRK - Verdugo', 'type': 'play', 'city': 'Burbank', 'group': 'Verdugo_All'},
           2: {'name': 'GLN - Verdugo', 'type': 'play', 'city': 'Glendale', 'group': 'Verdugo_All'},
           3: {'name': 'PSD - Verdugo', 'type': 'play', 'city': 'Pasdaenda', 'group': 'Verdugo_All'},
           4: {'name': 'BRK - BPD', 'type': 'play', 'city': 'Burbank', 'group': 'BPD'},
           5: {'name': 'GLN - BPD', 'type': 'play', 'city': 'Glendale', 'group': 'BPD'},
           6: {'name': 'PSD - BPD', 'type': 'play', 'city': 'Pasadena', 'group': 'BPD'},
           7: {'name': 'BRK - GPD', 'type': 'play', 'city': 'Burbank', 'group': 'GPD'},
           8: {'name': 'GLN - GPD', 'type': 'play', 'city': 'Glendale', 'group': 'GPD'},
           9: {'name': 'PSD - GPD', 'type': 'play', 'city': 'Pasadena', 'group': 'GPD'},
           10: {'name': 'BRK - ICI', 'type': 'play', 'city': 'Burbank', 'group': 'ICI'},
           11: {'name': 'GLN - ICI', 'type': 'play', 'city': 'Glendale', 'group': 'ICI'},
           12: {'name': 'PSD - ICI', 'type': 'play', 'city': 'Pasadena', 'group': 'ICI'},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_ICI_Main
Menu_ICI_Main = {
            1: {'name': 'Burbank', 'type': 'menu', 'city': 'Burbank', 'group': 'Main'},
            2: {'name': 'Glendale', 'type': 'menu', 'city': 'Glendale', 'group': 'Main'},
            3: {'name': 'Pasadena', 'type': 'menu', 'city': 'Pasadena', 'group': 'Main'},
            4: {'name': 'SCV/SFV', 'type': 'menu', 'city': 'SCV', 'group': 'Main'},
            5: {'name': 'Montebello', 'type': 'menu', 'city': 'Montebello', 'group': 'Main'},
            6: {'name': 'Pomona', 'type': 'Menu', 'city': 'Pomona', 'group': 'Main'},
            7: {'name': 'Beverly Hills', 'type': 'menu', 'city': 'BeverlyHills', 'group': 'Main'},
            8: {'name': 'Culver City', 'type': 'menu', 'city': 'Culver', 'group': 'Main'},
            9: {'name': 'Palmdale', 'type': 'menu', 'city': 'Palmdale', 'group': 'Main'},
            10: {'name': 'Glendora', 'type': 'menu', 'city': 'Glendora', 'group': 'Main'},
            11: {'name': 'South Bay', 'type': 'menu', 'city': 'SouthBay', 'group': 'Main'},
            12: {'name': 'Santa Monica', 'type': 'menu', 'city': 'SantaMonica', 'group': 'Main'},
            13: {'name': '', 'type': '', 'city': '', 'group': ''},
            14: {'name': '', 'type': '', 'city': '', 'group': ''},
            15: {'name': '', 'type': '', 'city': '', 'group': ''},
         }

# Menu_Home
Menu_Home = {
           1: {'name': 'ICI System', 'type': 'menu', 'city': 'ICI', 'group': 'Main'},
           2: {'name': 'CWIRS', 'type': 'menu', 'city': 'LAC', 'group': 'CWIRS'},
           3: {'name': 'LA-RICS', 'type': 'menu', 'city': 'LAC', 'group': 'LARICS'},
           # 4: {'name': '', 'type': '', 'city': '', 'group': ''},
           5: {'name': 'Orange County', 'type': 'menu', 'city': 'OC', 'group': 'CCCS'},
           # 7: {'name': '', 'type': '', 'city': '', 'group': ''},
           # 8: {'name': '', 'type': '', 'city': '', 'group': ''},
           # 9: {'name': '', 'type': '', 'city': '', 'group': ''},
           # 10: {'name': '', 'type': '', 'city': '', 'group': ''},
           # 11: {'name': '', 'type': '', 'city': '', 'group': ''},
           # 12: {'name': '', 'type': '', 'city': '', 'group': ''},
           # 13: {'name': '', 'type': '', 'city': '', 'group': ''},
           # 14: {'name': '', 'type': '', 'city': '', 'group': ''},
           # 15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }

# Menu_Burbank_Main
Menu_Burbank_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'Burbank', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'Burbank', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'Burbank', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'Burbank', 'group': 'ICI'},
           5: {'name': 'EMCOM', 'type': 'play', 'city': 'Burbank', 'group': 'bur_emcom'},
           6: {'name': 'GLN EMCOM', 'type': 'play', 'city': 'Burbank', 'group': 'glen_emcom'},
           7: {'name': 'All EMCOM', 'type': 'play', 'city': 'Burbank', 'group': 'all_emcom'},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Burbank_Verdugo_All
Menu_Burbank_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'Burbank', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'Burbank', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'Burbank', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'Burbank', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'Burbank', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'Burbank', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'Burbank', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'Burbank', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'Burbank', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'Burbank', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Glendale_Main
Menu_Glendale_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'Glendale', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'Glendale', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'Glendale', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'Glendale', 'group': 'ICI'},
           5: {'name': 'EMCOM', 'type': 'play', 'city': 'Glendale', 'group': 'glen_emcom'},
           6: {'name': 'BUR EMCOM', 'type': 'play', 'city': 'Glendale', 'group': 'bur_emcom'},
           7: {'name': 'All EMCOM', 'type': 'play', 'city': 'Glendale', 'group': 'all_emcom'},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Glendale_Verdugo_All
Menu_Glendale_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'Glendale', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'Glendale', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'Glendale', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'Glendale', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'Glendale', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'Glendale', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'Glendale', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'Glendale', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'Glendale', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'Glendale', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Pasadena_Main
Menu_Pasadena_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'Pasadena', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'Pasdaenda', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'Pasdaenda', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'Pasadena', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Pasadena_Verdugo_All
Menu_Pasadena_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'Pasadena', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'Pasadena', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'Pasadena', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'Pasadena', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'Pasadena', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'Pasadena', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'Pasadena', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'Pasadena', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'Pasadena', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'Pasadena', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_LAC_CWIRS
Menu_LAC_CWIRS = {
           1: {'name': 'Basin', 'type': 'play', 'city': 'CWIRS', 'group': 'basin'},
           2: {'name': 'East', 'type': 'play', 'city': 'CWIRS', 'group': 'east'},
           3: {'name': 'Northwest', 'type': 'play', 'city': 'CWIRS', 'group': 'northwest'},
           4: {'name': 'West', 'type': '', 'city': 'CWIRS', 'group': 'west'},
           5: {'name': 'Thousand Oaks', 'type': 'play', 'city': 'CWIRS', 'group': 'thousand_oaks'},
           6: {'name': 'Palmdale', 'type': 'play', 'city': 'CWIRS', 'group': 'palmdale'},
           7: {'name': 'Catalina', 'type': 'play', 'city': 'CWIRS', 'group': 'catalina'},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_LAC_LARICS
Menu_LAC_LARICS = {
          1: {'name': 'Verdugo Peak', 'type': 'play', 'city': 'LARICS', 'group': 'verdugo'},
          2: {'name': 'West Covina', 'type': 'play', 'city': 'LARICS', 'group': 'westcovina'},
          3: {'name': 'Torrence', 'type': 'play', 'city': 'LARICS', 'group': 'torrence'},
          4: {'name': 'SCV/Granada', 'type': 'play', 'city': 'LARICS', 'group': 'scv_granada'},
          5: {'name': 'Palmdale', 'type': 'play', 'city': 'LARICS', 'group': 'palmdale'},
          6: {'name': 'Downtown LA', 'type': 'play', 'city': 'LARICS', 'group': 'downtownla'},
          7: {'name': 'Azusa', 'type': 'play', 'city': 'LARICS', 'group': 'azusa'},
          8: {'name': '', 'type': '', 'city': '', 'group': ''},
          9: {'name': '', 'type': '', 'city': '', 'group': ''},
          10: {'name': '', 'type': '', 'city': '', 'group': ''},
          11: {'name': '', 'type': '', 'city': '', 'group': ''},
          12: {'name': '', 'type': '', 'city': '', 'group': ''},
          13: {'name': '', 'type': '', 'city': '', 'group': ''},
          14: {'name': '', 'type': '', 'city': '', 'group': ''},
          15: {'name': '', 'type': '', 'city': '', 'group': ''},
         }

# Menu_Template (Menu_city_group)
Menu_OC_CCCS = {
          1: {'name': 'CountyWide', 'type': 'play', 'city': 'CCCS', 'group': 'CountyWide'},
          2: {'name': 'North', 'type': 'play', 'city': 'CCCS', 'group': 'North'},
          3: {'name': 'South', 'type': 'play', 'city': 'CCCS', 'group': 'South'},
          4: {'name': '', 'type': '', 'city': '', 'group': ''},
          5: {'name': '', 'type': '', 'city': '', 'group': ''},
          6: {'name': '', 'type': '', 'city': '', 'group': ''},
          7: {'name': '', 'type': '', 'city': '', 'group': ''},
          8: {'name': '', 'type': '', 'city': '', 'group': ''},
          9: {'name': '', 'type': '', 'city': '', 'group': ''},
          10: {'name': '', 'type': '', 'city': '', 'group': ''},
          11: {'name': '', 'type': '', 'city': '', 'group': ''},
          12: {'name': '', 'type': '', 'city': '', 'group': ''},
          13: {'name': '', 'type': '', 'city': '', 'group': ''},
          14: {'name': '', 'type': '', 'city': '', 'group': ''},
          15: {'name': '', 'type': '', 'city': '', 'group': ''},
         }

# Menu_SCV_Main
Menu_SCV_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'SCV', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'SCV', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'SCV', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'SCV', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_SCV_Verdugo_All
Menu_SCV_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'SCV', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'SCV', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'SCV', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'SCV', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'SCV', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'SCV', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'SCV', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'SCV', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'SCV', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'SCV', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Montebello_Main
Menu_Montebello_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'Montebello', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'Montebello', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'Montebello', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'Montebello', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Montebello_Verdugo_All
Menu_Montebello_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'Montebello', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'Montebello', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'Montebello', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'Montebello', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'Montebello', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'Montebello', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'Montebello', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'Montebello', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'Montebello', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'Montebello', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Pomona_Main
Menu_Pomona_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'Pomona', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'Pomona', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'Pomona', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'Pomona', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Pomona_Verdugo_All
Menu_Pomona_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'Pomona', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'Pomona', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'Pomona', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'Pomona', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'Pomona', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'Pomona', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'Pomona', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'Pomona', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'Pomona', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'Pomona', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_BeverlyHills_Main
Menu_BeverlyHills_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'BeverlyHills', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'BeverlyHills', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_BeverlyHills_Verdugo_All
Menu_BeverlyHills_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'BeverlyHills', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'BeverlyHills', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Culver_Main
Menu_Culver_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'Culver', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'Culver', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'Culver', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'Culver', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Culver_Verdugo_All
Menu_Culver_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'Culver', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'Culver', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'Culver', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'Culver', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'Culver', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'Culver', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'Culver', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'Culver', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'Culver', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'Culver', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Palmdale_Main
Menu_Palmdale_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'Palmdale', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'Palmdale', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'Palmdale', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'Palmdale', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Palmdale_Verdugo_All
Menu_Palmdale_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'Palmdale', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'Palmdale', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'Palmdale', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'Palmdale', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'Palmdale', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'Palmdale', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'Palmdale', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'Palmdale', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'Palmdale', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'Palmdale', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Glendora_Main
Menu_Glendora_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'Glendora', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'Glendora', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'Glendora', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'Glendora', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_Glendora_Verdugo_All
Menu_Glendora_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'Glendora', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'Glendora', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'Glendora', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'Glendora', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'Glendora', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'Glendora', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'Glendora', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'Glendora', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'Glendora', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'Glendora', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_SouthBay_Main
Menu_SouthBay_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'SouthBay', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'SouthBay', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'SouthBay', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'SouthBay', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_SouthBay_Verdugo_All
Menu_SouthBay_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'SouthBay', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'SouthBay', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'SouthBay', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'SouthBay', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'SouthBay', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'SouthBay', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'SouthBay', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'SouthBay', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'SouthBay', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'SouthBay', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_SantaMonica_Main
Menu_SantaMonica_Main = {
           1: {'name': 'Verdugo Fire', 'type': 'menu', 'city': 'SantaMonica', 'group': 'Verdugo'},
           2: {'name': 'Bubank PD', 'type': 'play', 'city': 'SantaMonica', 'group': 'Verdugo_All'},
           3: {'name': 'Glendale PD', 'type': 'play', 'city': 'SantaMonica', 'group': 'Verdugo_All'},
           4: {'name': 'ICI', 'type': 'play', 'city': 'SantaMonica', 'group': 'ICI'},
           5: {'name': '', 'type': '', 'city': '', 'group': ''},
           6: {'name': '', 'type': '', 'city': '', 'group': ''},
           7: {'name': '', 'type': '', 'city': '', 'group': ''},
           8: {'name': '', 'type': '', 'city': '', 'group': ''},
           9: {'name': '', 'type': '', 'city': '', 'group': ''},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': '', 'type': '', 'city': '', 'group': ''},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }
# Menu_SantaMonica_Verdugo_All
Menu_SantaMonica_Verdugo = {
           1: {'name': 'Red 1', 'type': 'play', 'city': 'SantaMonica', 'group': 'Red1'},
           2: {'name': 'Red 2', 'type': 'menu', 'city': 'SantaMonica', 'group': 'Red2'},
           3: {'name': 'Red 3', 'type': 'play', 'city': 'SantaMonica', 'group': 'Red3'},
           4: {'name': 'Red 4', 'type': 'play', 'city': 'SantaMonica', 'group': 'Red4'},
           5: {'name': 'Red 5', 'type': 'play', 'city': 'SantaMonica', 'group': 'Red5'},
           6: {'name': 'Red 6', 'type': 'play', 'city': 'SantaMonica', 'group': 'Red6'},
           7: {'name': 'Red 7', 'type': 'play', 'city': 'SantaMonica', 'group': 'Red7'},
           8: {'name': 'Red 8', 'type': 'play', 'city': 'SantaMonica', 'group': 'Red8'},
           9: {'name': 'Red 9', 'type': 'play', 'city': 'SantaMonica', 'group': 'Red9'},
           10: {'name': '', 'type': '', 'city': '', 'group': ''},
           11: {'name': 'All', 'type': 'play', 'city': 'SantaMonica', 'group': 'Verdugo_All'},
           12: {'name': '', 'type': '', 'city': '', 'group': ''},
           13: {'name': '', 'type': '', 'city': '', 'group': ''},
           14: {'name': '', 'type': '', 'city': '', 'group': ''},
           15: {'name': '', 'type': '', 'city': '', 'group': ''},
          }


# Define path to TSV Files
TSV_Files_Path = "/home/pi/op25-scripts/tsv_files"

# Define path to OP25
OP25_Path = "/home/pi/op25/op25/gr-op25_repeater/apps"

# Define path to OP25 Log Output
OP25_Log_Path = "/tmp"

NowPlaying = ""


def stopall():
    os.system("pkill -f ./rx.py")
    global NowPlaying
    NowPlaying = ""

def closeall(self):
    stopall
    try:
        self.mw
        self.mw.destroy()
    except:
        self.process.kill() # exit subprocess if GUI is closed (zombie!)
        self.root.destroy()
def iter_except(function, exception):
    """Works like builtin 2-argument `iter()`, but stops on `exception`."""
    try:
        while True:
            yield function()
    except exception:
        return
class OP25_GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mw = tk.Tk()
        self.Menu_Favorites()
        atexit.register(stopall)

    def OP25Player(self):
        # print("Open Player")
        self.mw.destroy()
        self.mw = tk.Tk()
        app = DisplayPlayer(self.mw)
        self.mw.protocol("WM_DELETE_WINDOW", app.quit)
        self.mw.mainloop()

    def OP25CMD(self, type, city, group, playing):
        if type is 'menu':
            buttons = 'Menu_'+city+'_'+group
            title = city+' '+group
            print(buttons)
            print(title)
            self.Menu(title, globals().get(buttons,None))

        if type is 'play':
            global NowPlaying
            if re.match(r'^GLN|^BRK|^PSD',playing):
                NowPlaying = playing
            else:
                NowPlaying = city+" "+playing
            # print("cd "+OP25_Path+"; ./rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -q -1 -T "+TSV_Files_Path+"/"+city.lower()+"/"+group.lower()+".tsv -V -2 -U 2> "+OP25_Log_Path+"/stderr.2 -l 'http:0.0.0.0:8080'&")
            os.system("pkill -f ./rx.py")
            os.system("cd "+OP25_Path+"; ./rx.py -n --args 'rtl' -N 'LNA:47' -S 96000 -o 1.25e3 -q -1 -T "+TSV_Files_Path+"/"+city.lower()+"/"+group.lower()+".tsv -V -2 -U -v 5 2> "+OP25_Log_Path+"/stderr.2 -l 'http:0.0.0.0:8080'&")

    def Menu_Favorites(self):
        title = "Favorites"
        self.Menu(title, Menu_Favorites)

    def Menu_Favorites2(self):
        title = "Favorites #2"
        self.Menu(title, Menu_Favorites2)


    def Menu_Home(self):
        title = "Home"
        self.Menu(title, Menu_Home)

    def Menu(self, title, buttons):

            self.mw.destroy()
            self.mw = tk.Tk()
            #Specify the attributes for all widgets simply like this.
            self.mw.option_add("*Button.Background", "Teal")
            self.mw.option_add("*Button.Foreground", "White")
            self.mw.title('OP25 - '+title)
            #You can set the geometry attribute to change the root windows size
            # self.mw.geometry("480x360") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
            self.mw.overrideredirect(True)
            self.mw.geometry("{0}x{1}+0+0".format(self.mw.winfo_screenwidth(), self.mw.winfo_screenheight()))
            self.mw.focus_set()  # <-- move focus to this widget
            self.mw.resizable(0, 0) #Don't allow resizing in the x or y direction
            # self.mw.config(cursor="none")
            back = tk.Frame(master=self.mw,bg='Grey')
            back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
            back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
            #Buttons
            Stop_OP25 = tk.Button(master=back, text='Stop OP25', command=stopall, width=8, height=2)
            Stop_OP25.grid(row=0, column=2, padx=9, pady=3)
            if "Favorites" is title:
                GoToFavorites_OP25 = tk.Button(master=back, text='Favorites #2', command=self.Menu_Favorites2, width=8, height=2)
            else:
                GoToFavorites_OP25 = tk.Button(master=back, text='Favorites', command=self.Menu_Favorites, width=8, height=2)
            GoToFavorites_OP25.grid(row=0, column=1, padx=9, pady=3)
            if "Home" in title:
                OP25Player = tk.Button(master=back, text='Monitor', command=lambda: self.OP25Player(), width=8, height=2)
                OP25Player.grid(row=0, column=3, padx=9, pady=3)
                Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=2)
            else:
                GoToMainMenu_OP25 = tk.Button(master=back, text='Main Menu', command=self.Menu_Home, width=8, height=2)
                GoToMainMenu_OP25.grid(row=0, column=3, padx=9, pady=3)
                Button_close = tk.Button(master=back, text='Quit', command=self.mw.destroy, width=5,height=1)

            if 1 in buttons:
                Button_1 = tk.Button(master=back, text=buttons[1]['name'], command=lambda: self.OP25CMD(buttons[1]['type'],buttons[1]['city'],buttons[1]['group'],buttons[1]['name']), width=14, height=2)
                Button_1.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 2 in buttons:
                Button_2 = tk.Button(master=back, text=buttons[2]['name'], command=lambda: self.OP25CMD(buttons[2]['type'],buttons[2]['city'],buttons[2]['group'],buttons[2]['name']), width=14, height=2)
                Button_2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 3 in buttons:
                Button_3 = tk.Button(master=back, text=buttons[3]['name'], command=lambda: self.OP25CMD(buttons[3]['type'],buttons[3]['city'],buttons[3]['group'],buttons[3]['name']), width=14, height=2)
                Button_3.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 4 in buttons:
                Button_4 = tk.Button(master=back, text=buttons[4]['name'], command=lambda: self.OP25CMD(buttons[4]['type'],buttons[4]['city'],buttons[4]['group'],buttons[4]['name']), width=14, height=2)
                Button_4.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 5 in buttons:
                Button_5 = tk.Button(master=back, text=buttons[5]['name'], command=lambda: self.OP25CMD(buttons[5]['type'],buttons[5]['city'],buttons[5]['group'],buttons[5]['name']), width=14, height=2)
                Button_5.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 6 in buttons:
                Button_6 = tk.Button(master=back, text=buttons[6]['name'], command=lambda: self.OP25CMD(buttons[6]['type'],buttons[6]['city'],buttons[6]['group'],buttons[6]['name']), width=14, height=2)
                Button_6.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 7 in buttons:
                Button_7 = tk.Button(master=back, text=buttons[7]['name'], command=lambda: self.OP25CMD(buttons[7]['type'],buttons[7]['city'],buttons[7]['group'],buttons[7]['name']), width=14, height=2)
                Button_7.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 8 in buttons:
                Button_8 = tk.Button(master=back, text=buttons[8]['name'], command=lambda: self.OP25CMD(buttons[8]['type'],buttons[8]['city'],buttons[8]['group'],buttons[8]['name']), width=14, height=2)
                Button_8.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 9 in buttons:
                Button_9 = tk.Button(master=back, text=buttons[9]['name'], command=lambda: self.OP25CMD(buttons[9]['type'],buttons[9]['city'],buttons[9]['group'],buttons[9]['name']), width=14, height=2)
                Button_9.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 10 in buttons:
                Button_10 = tk.Button(master=back, text=buttons[10]['name'], command=lambda: self.OP25CMD(buttons[10]['type'],buttons[10]['city'],buttons[10]['group'],buttons[10]['name']), width=14, height=2)
                Button_10.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 11 in buttons:
                Button_11 = tk.Button(master=back, text=buttons[11]['name'], command=lambda: self.OP25CMD(buttons[11]['type'],buttons[11]['city'],buttons[11]['group'],buttons[11]['name']), width=14, height=2)
                Button_11.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 12 in buttons:
                Button_12 = tk.Button(master=back, text=buttons[12]['name'], command=lambda: self.OP25CMD(buttons[12]['type'],buttons[12]['city'],buttons[12]['group'],buttons[12]['name']), width=14, height=2)
                Button_12.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 13 in buttons:
                Button_13 = tk.Button(master=back, text=buttons[13]['name'], command=lambda: self.OP25CMD(buttons[13]['type'],buttons[13]['city'],buttons[13]['group'],buttons[13]['name']), width=14, height=2)
                Button_13.grid(row=5, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 14 in buttons:
                Button_14 = tk.Button(master=back, text=buttons[14]['name'], command=lambda: self.OP25CMD(buttons[14]['type'],buttons[14]['city'],buttons[14]['group'],buttons[14]['name']), width=14, height=2)
                Button_14.grid(row=5, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)
            if 15 in buttons:
                Button_15 = tk.Button(master=back, text=buttons[15]['name'], command=lambda: self.OP25CMD(buttons[15]['type'],buttons[15]['city'],buttons[15]['group'],buttons[15]['name']), width=14, height=2)
                Button_15.grid(row=5, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=9, pady=3)


            Button_close.grid(row=6, column=2, padx=9, pady=3)


class DisplayPlayer:
    def __init__(self, root):
        self.root = root

        # start dummy subprocess to generate some output

        self.process = Popen(['tail','-n','0','-f',OP25_Log_Path+'/stderr.2'], stdout=PIPE)
        global NowPlaying
        # NowPlaying = "Test"
        # launch thread to read the subprocess output
        #   (put the subprocess output into the queue in a background thread,
        #    get output from the queue in the GUI thread.
        #    Output chain: process.readline -> queue -> label)
        q = Queue(maxsize=1024)  # limit output buffering (may stall subprocess)
        t = Thread(target=self.reader_thread, args=[q])
        t.daemon = True # close pipe if GUI process exits
        t.start()

        # show subprocess' stdout in GUI
        self.root.option_add("*Button.Background", "Teal")
        self.root.option_add("*Button.Foreground", "White")
        # center window
        self.root.title('OP25 - Monitor')
        #You can set the geometry attribute to change the root windows size
        # self.root.geometry("480x360") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
        self.root.overrideredirect(True)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.focus_set()  # <-- move focus to this widget
        self.root.resizable(0, 0) #Don't allow resizing in the x or y direction
        # self.root.config(cursor="none")
        back = tk.Frame(master=self.root,bg='Grey')
        back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
        back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
        close = tk.Button(master=back, height=3, text='Close Monitor', command=lambda:[self.process.kill(),self.root.destroy(),OP25_GUI().Menu_Home()])
        close.pack(side='bottom')
        self.title = tk.Label(master=back, text=" TalkGroup Monitor  ", font=(None, 36), fg='White', bg="Teal")
        self.title.grid(row=0, column=0)
        self.title = tk.Label(master=back, text=NowPlaying, font=(None, 30), fg='White', bg="Grey")
        self.title.grid(row=1, column=0)
        self.label = tk.Label(master=back, text="Idle", font=(None, 22), fg='White', bg="Grey")
        self.label.grid(row=2, pady=20, column=0, sticky='we')
        self.update(q) # start update loop

    def reader_thread(self, q):
        """Read subprocess output and put it into the queue."""
        try:
            with self.process.stdout as pipe:
                for line in iter(pipe.readline, b''):
                    if b'do_metadata' in line:
                        q.put(line)
        finally:
            q.put(None)

    def update(self, q):
        """Update GUI with items from the queue."""
        for line in iter_except(q.get_nowait, Empty): # display all content
            if line is None:
                self.quit()
                return
            else:
                text = line.split(b': ',1)[1]
                self.label['text'] = text.split(b'] ',1)[1] # update GUI
                break # display no more than one line per 40 milliseconds
        self.root.after(40, self.update, q) # schedule next update

    def quit(self):
        self.process.kill() # exit subprocess if GUI is closed (zombie!)
        self.root.destroy()
        OP25_GUI().Menu_Home()
if __name__ == '__main__':
    OP25_GUI().mw.mainloop()
