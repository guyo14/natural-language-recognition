'''
Created on Nov 17, 2014

@author: alejandro
'''

import UserInterface
from gi.repository import Gtk

window = UserInterface.MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()