'''
Created on Nov 17, 2014

@author: alejandro
'''

from gi.repository import Gtk

import UserInterface


window = UserInterface.MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()