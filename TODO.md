# TODO

## 1) Kill pygtk replace with pygobject

D-Rats is being removed from main Linux distributions because
of pygtk (unmaintaned) dependency. pygobject is the new way!

* https://pygobject.readthedocs.io/en/latest/getting_started.html

#### More information:

##### RIP package removal

* https://tracker.debian.org/pkg/d-rats
* https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=885270

##### Supporting documentation

* https://wiki.gnome.org/Projects/GObjectIntrospection
* https://wiki.gnome.org/Projects/PyGObject
* https://wiki.gnome.org/Projects/PyGObject/PyGTKCompat

## 2) Replace gtk2 glade methods with the gtk3+ method

#### More information:

Get started with the new way:

* https://python-gtk-3-tutorial.readthedocs.io/en/latest/builder.html

Files involved:

    ui/addport.glade
    2:<glade-interface>
    675:</glade-interface>

    ui/mainwindow.gladep
    2:<!DOCTYPE glade-project SYSTEM "http://glade.gnome.org/glade-project-2.0.dtd">
    4:<glade-project>
    8:</glade-project>

    ui/mainwindow.glade
    2:<glade-interface>
    1406:</glade-interface>

    d_rats.egg-info/SOURCES.txt
    126:ui/addport.glade
    127:ui/mainwindow.glade

    MANIFEST.in
    7:include ui/*.glade

    d_rats/mainapp.py
    458:            Gtk.glade.bindtextdomain("D-RATS", localedir)
    459:            Gtk.glade.textdomain("D-RATS")

    d_rats/config.py
    24:import Gtk.glade
    227:    p = os.path.join(platform.get_platform().source_dir(), "ui/addport.glade")
    228:    wtree = Gtk.glade.XML(p, "addport", "D-RATS")

    d_rats/map_source_editor.py
    92:        fn = config.ship_obj_fn("ui/mainwindow.glade")
    96:        wtree = Gtk.glade.XML(fn, "srcs_dialog", "D-RATS")
    135:        fn = config.ship_obj_fn("ui/mainwindow.glade")
    139:        self._wtree = Gtk.glade.XML(fn, "src_dialog", "D-RATS")

    d_rats/mainwindow.py
    36:import gtk.glade
    153:            wtree = gtk.glade.XML(c.ship_obj_fn("ui/mainwindow.glade"),
    253:        wtree = gtk.glade.XML(config.ship_obj_fn("ui/mainwindow.glade"),
    324:    wtree = gtk.glade.XML("ui/mainwindow.glade", "mainwindow")

    build/lib/d_rats/mainapp.py
    458:            Gtk.glade.bindtextdomain("D-RATS", localedir)
    459:            Gtk.glade.textdomain("D-RATS")

    build/lib/d_rats/config.py
    24:import Gtk.glade
    227:    p = os.path.join(platform.get_platform().source_dir(), "ui/addport.glade")
    228:    wtree = Gtk.glade.XML(p, "addport", "D-RATS")

    build/lib/d_rats/map_source_editor.py
    92:        fn = config.ship_obj_fn("ui/mainwindow.glade")
    96:        wtree = Gtk.glade.XML(fn, "srcs_dialog", "D-RATS")
    135:        fn = config.ship_obj_fn("ui/mainwindow.glade")
    139:        self._wtree = Gtk.glade.XML(fn, "src_dialog", "D-RATS")

    build/lib/d_rats/mainwindow.py
    157:            wtree = Gtk.glade.XML(c.ship_obj_fn("ui/mainwindow.glade"),
    257:        wtree = Gtk.glade.XML(config.ship_obj_fn("ui/mainwindow.glade"),
    328:    wtree = Gtk.glade.XML("ui/mainwindow.glade", "mainwindow")

    UNKNOWN.egg-info/SOURCES.txt
    63:ui/addport.glade
    64:ui/mainwindow.glade

    .eggs/py2app-0.18-py2.7.egg/EGG-INFO/PKG-INFO
    1580:.. _`wxGlade`: http://wxglade.sourceforge.net/

    .eggs/py2app-0.18-py3.6.egg/EGG-INFO/PKG-INFO
    1580:.. _`wxGlade`: http://wxglade.sourceforge.net/
