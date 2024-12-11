import gi
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class WelcomeWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Astian_OS Utilities")
        self.set_border_width(100)
        self.set_decorated(False)
        self.set_resizable(False)
        self.set_default_size(900, 500)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.apply_css()

        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        self.add(main_box)

        left_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        main_box.pack_start(left_box, False, False, 0)

        main_icon = Gtk.Image.new_from_icon_name("applications-development", Gtk.IconSize.DIALOG)
        main_icon.set_pixel_size(32)
        main_icon.set_halign(Gtk.Align.START)
        
        header_label = Gtk.Label(label="Welcome")
        header_label.get_style_context().add_class("header")
        left_box.pack_start(main_icon, False, False, 0)
        left_box.pack_start(header_label, False, False, 0)
        left_box.set_margin_top(60)
        button_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        main_box.pack_start(button_box, True, True, 0)

        buttons = [
            [
                "astian-core",
                "Install Astian_OS",
                ["calamares"],
            ],
            [
                "web-browser",
                "Open Browser",
                ["midori"],
            ],
            [
                "disk-baob",
                "Disk Partitioning",
                ["gparted"],
            ],
            [
                "terminal",
                "Terminal",
                ["astian-terminal"],
            ],
        ]
        for i in buttons:
            button_box.pack_start(self.create_button(*i), True, True, 0)

        self.connect("delete-event", lambda widget, event: True)

    def apply_css(self):
        css_provider = Gtk.CssProvider()
        css = """
            window {
                background-color: #1f1f1f;
            }
            button {
                background-color: #282828;
                border: none;
                border-radius: 5px;
                padding: 10px;
                box-shadow: none;
            }
            button:hover {
                background-color: #535353;
            }
            label {
                font-family: Sans;
                font-size: 18px;
                color: #ffffff;
            }
            label.header {
                font-size: 35px;
                font-weight: bold;
                margin-bottom: 15px;
            }
            .custom-dropdown {
                background-color: #282828;
                color: #ffffff;
                border: none;
                padding: 5px;
                border-radius: 5px;
            }
        """
        css_provider.load_from_data(css.encode("utf-8"))

        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def create_button(self, icon_name, title, command):
        button = Gtk.Button()
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        button.add(box)

        icon = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.DIALOG)
        icon.set_pixel_size(32)

        box.pack_start(icon, False, False, 0)

        title_label = Gtk.Label(label=title)
        title_label.set_xalign(0)

        box.pack_start(title_label, True, True, 0)
        button.connect("clicked", lambda widget: subprocess.run(command))
        return button


if __name__ == "__main__":
    win = WelcomeWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
