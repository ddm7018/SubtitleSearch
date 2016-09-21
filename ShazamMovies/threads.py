import threading
import time
import gobject
import pygtk
pygtk.require('2.0')
import gtk

gobject.threads_init()

class MyThread(threading.Thread):
    def __init__(self, label):
        super(MyThread, self).__init__()
        self.label = label
        self.quit = False

    def update_label(self, counter):
        self.label.start()
        return False

    def run(self):
    	counter = 0
        while True:
            counter += 1
            gobject.idle_add(self.update_label, counter)
            time.sleep(5)
            print 'done'
            self.label.stop()
            break

w = gtk.Window()
#l = gtk.Label()
h = gtk.Spinner()
#w.add(l)
w.add(h)
w.show_all()
w.connect("destroy", lambda _: gtk.main_quit())
t = MyThread(h)
t.start()

gtk.main()
t.quit = True