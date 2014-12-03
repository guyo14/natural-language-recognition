'''
Created on Nov 17, 2014

@author: alejandro
'''

from gi.repository import Gtk

class MainWindow(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self, title="Reconocimiento basico del lenguaje")
		
		self.set_default_size(500, 350)
		
		self.grid = Gtk.Grid()
		self.add(self.grid)
		
		self.create_textview()
		self.create_toolbar()
		
		self.modified = False;
		self.file = "";
	
	
	def create_toolbar(self):
		toolbar = Gtk.Toolbar()
		self.grid.attach(toolbar, 0, 0, 3, 1)
		
		button_new = Gtk.ToolButton.new_from_stock(Gtk.STOCK_NEW)
		toolbar.insert(button_new, 0)
		
		button_open = Gtk.ToolButton.new_from_stock(Gtk.STOCK_OPEN)
		toolbar.insert(button_open, 1)
		
		button_save = Gtk.ToolButton.new_from_stock(Gtk.STOCK_SAVE)
		toolbar.insert(button_save, 2)
		
		button_saveas = Gtk.ToolButton.new_from_stock(Gtk.STOCK_SAVE_AS)
		toolbar.insert(button_saveas, 3)
		
		button_analyse = Gtk.ToolButton.new_from_stock(Gtk.STOCK_EXECUTE)
		toolbar.insert(button_analyse, 4)
		
		button_new.connect("clicked", self.on_button_new_clicked)
		button_open.connect("clicked", self.on_button_open_clicked)
		button_save.connect("clicked", self.on_button_save_clicked)
		button_saveas.connect("clicked", self.on_button_saveas_clicked)
	
	
	def create_textview(self):
		scrolledwindow = Gtk.ScrolledWindow()
		scrolledwindow.set_hexpand(True)
		scrolledwindow.set_vexpand(True)
		self.grid.attach(scrolledwindow, 0, 1, 3, 1)
		
		self.textview = Gtk.TextView()
		self.textbuffer = self.textview.get_buffer()
		scrolledwindow.add(self.textview)
		
		self.textbuffer.connect("changed", self.on_textbuffer_changed)
	
	
	def on_button_new_clicked(self, widget):
		execute = True
		if self.modified:
			dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, "Desea guardar los cambios?")
			dialog.format_secondary_text("Si no guarda los cambios, estos se perderan.")
			response = dialog.run()
			if response == Gtk.ResponseType.YES:
				if self.file == "":
					execute = self.save_as()
				else:
					self.save()
			dialog.destroy()
		if execute:
			self.textbuffer.set_text("")
			self.modified = False
	
	
	def on_button_open_clicked(self, widget):
		execute = True
		if self.modified:
			dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, "Desea guardar los cambios?")
			dialog.format_secondary_text("Si no guarda los cambios, estos se perderan.")
			response = dialog.run()
			if response == Gtk.ResponseType.YES:
				if self.file == "":
					execute = self.save_as()
				else:
					self.save()
			dialog.destroy()
		if execute:
			self.open()
			self.modified = False
	
	
	def on_button_save_clicked(self, widget):
		if self.file == "":
			self.save_as()
		else:
			self.save()
	
	
	def on_button_saveas_clicked(self, widget):
		self.save_as()
	
	
	def on_textbuffer_changed(self, widget):
		self.modified = True
	
	
	def open(self):
		dialog = Gtk.FileChooserDialog("Abrir", self, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		self.add_filters(dialog)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			self.file = dialog.get_filename()
			f = open(self.file, 'r')
			self.textbuffer.set_text(f.read())
			self.modified = False
		dialog.destroy()
	
	
	def save(self):
		f = open(self.file, 'w')
		f.write(self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), False))
		self.modified = False
		return True
	
	
	def save_as(self):
		dialog = Gtk.FileChooserDialog("Guardar", self, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
		self.add_filters(dialog)
		response = dialog.run()
		result = False
		if response == Gtk.ResponseType.OK:
			self.file = dialog.get_filename()
			result = self.save()
		dialog.destroy()
		return result
	
	
	def add_filters(self, dialog):
		filter_text = Gtk.FileFilter()
		filter_text.set_name("Text files")
		filter_text.add_mime_type("text/plain")
		dialog.add_filter(filter_text)
		
		filter_any = Gtk.FileFilter()
		filter_any.set_name("Any files")
		filter_any.add_pattern("*")
		dialog.add_filter(filter_any)