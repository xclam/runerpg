import pygtk
pygtk.require("2.0")
import gtk

class Game:
    def __init__(self):
        interface = gtk.Builder()
        interface.add_from_file('runerpg.glade')

        self.ddmenu = interface.get_object('ddmenu')
        interface.connect_signals(self)

    def on_mainWindow_destroy(self, widget):
        gtk.main_quit()

    def on_menu_clicked(self, widget):
        self.ddmenu.set_visible(True)

    def on_ddmenu_leave_notify_event(self, widget):
        self.ddmenu.set_visible(False)
    
    def on_new_clicked(self,widget):
        pass

    def on_continue_clicked(self,widget):
        pass

if __name__ == "__main__":
    Game()
    gtk.main()
