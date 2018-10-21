#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gtk, Gdk
import os

import cairo

class Foo(object):
    def __init__(self):

       #(...)
        self.image = cairo.ImageSurface.create_from_png('../images/d-rats-logo-lg.png')
       #(...)

    def draw(self, widget, context):
        if self.image is not None:
            context.set_source_surface(self.image, 0.0, 0.0)
            context.paint()
        else:
            print('Invalid image')
        return False


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="My First Wihndow")

        #
        # self.button1 = Gtk.Button(label="Click Here 1")
        # self.button1.connect("clicked", self.about)
        # self.add(self.button1)

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        img = Gtk.Image.new_from_file('/path/to/my_file.png')

        #self.add(self.button)
        self.add(img)

    def on_button_clicked(self, widget):
        print("Hello World")
    def about(self, widget):
        Gtk.AboutDialog(website="http://www.google.com")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
