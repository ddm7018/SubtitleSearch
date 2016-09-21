import pygtk
pygtk.require('2.0')
import gtk
from time import sleep

def response(widget, response_id):
    if response_id != gtk.RESPONSE_APPLY:
        gtk.main_quit()
    else:
        i=0
        n=1000

        progress = dialog.get_data("progress")
        progress.set_text("Calculating....")
        progress.grab_add()

        while True:
            sleep(0.005)
            progress.set_fraction(i/(n - 1.0))
            i += 1
            print i
            

            while gtk.events_pending():
                gtk.main_iteration_do(False)
            
            if i == 500:
            	break

        progress.set_fraction(0.0)
        progress.set_text("")
        progress.grab_remove()

dialog = gtk.Dialog("Modal Trick", None, 0, (gtk.STOCK_EXECUTE,  gtk.RESPONSE_APPLY, 
                         gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE))

dialog.connect("response", response)
dialog.connect("destroy", gtk.main_quit)

box = dialog.get_child()

widget = gtk.CheckButton("Check me!")
box.pack_start(widget, False, False, 0)

widget = gtk.Entry()
box.pack_start(widget, False, False, 0)

adj = gtk.Adjustment(0.0, 0.0, 100.0, 1.0, 10.0, 0.0)
widget = gtk.HScale(adj)
box.pack_start(widget, False, False, 0)

widget = gtk.ProgressBar()
box.pack_start(widget, False, False, 0)

dialog.set_data("progress", widget)

dialog.show_all()
gtk.main()