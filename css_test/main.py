import sys
import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk, Gio

from window import Window

APP_ID = 'dk.rasmil.CSSTester'

class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID,
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = Window(application=self)
        win.present()


def main():
    app = Application()
    return app.run(sys.argv)


if __name__ == '__main__':
    main()
