import os.path
from gi.repository import Gtk, GLib, Gio


class Window(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.css_provider = self.load_css()
        self.set_title("CSS Tester")
        self.set_default_size(800, 800)
        self.content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.content)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.set_spacing(20)
        box.set_css_classes(['theme-box'])
        box.set_halign(Gtk.Align.START)
        box.set_hexpand(False)
        btn_dark = get_button(['dark','radio'])
        btn_dark.set_active(True)
        btn_light = get_button(['light','radio'])
        btn_light.set_group(btn_dark)
        box.append(btn_dark)
        box.append(btn_light)
        self.content.append(box)
        self.add_custom_styling(self.content)

    def load_css(self):
        """create a provider for custom styling"""
        css_provider = None
        css_provider = Gtk.CssProvider()
        css_path = 'main.css'
        try:
            css_provider.load_from_path(css_path)
        except GLib.Error as e:
            print(f"Error loading CSS : {e} ")
            return None
        print(f'loading custom styling from resource: {css_path}')
        return css_provider

    def _add_widget_styling(self, widget):
        if self.css_provider:
            context = widget.get_style_context()
            context.add_provider(
                self.css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def add_custom_styling(self, widget):
        self._add_widget_styling(widget)
        # iterate children recursive
        for child in widget:
            self.add_custom_styling(child)

    def create_action(self, name, callback):
        """ Add an Action and connect to a callback """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)


def get_button(css_classes):
    button = Gtk.CheckButton()
    button.set_css_classes(css_classes)
    return button
