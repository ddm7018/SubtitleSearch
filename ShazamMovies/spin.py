#!/usr/bin/env python

# example spinbutton.py

import pygtk
pygtk.require('2.0')
import gtk


class SpinnerAnimation(gtk.Window):

    def __init__(self):

        gtk.Window.__init__(self)
        self.set_border_width(3)
        self.connect("delete-event", gtk.main_quit)

        self.button = gtk.ToggleButton("Start Spinning")
        self.button.connect("toggled", self.on_button_toggled)
        self.button.set_active(False)

        self.spinner = gtk.Spinner()

        self.table = gtk.Table(3, 2, True)
        self.table.attach(self.button, 0, 2, 0, 1)
        self.table.attach(self.spinner, 0, 2, 2, 3)

        self.add(self.table)
        self.show_all()

    def on_button_toggled(self, button):

        if button.get_active():
            self.spinner.start()
            self.button.set_label("Stop Spinning")

        else:
            self.spinner.stop()
            self.button.set_label("Start Spinning")


myspinner = SpinnerAnimation()

gtk.main()