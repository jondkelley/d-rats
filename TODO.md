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

#### Work required

Possible files involved:

    debian/control
    12:Depends: ${misc:Depends}, ${python:Depends}, python-libxslt1, python-gtk2, python-libxml2, python-serial

    d-rats_repeater
    428:        gtk.main_quit()
    434:        gtk.main_quit()
    437:        vbox = gtk.VBox(False, 2)
    439:        but_add = gtk.Button("Add")
    445:        but_remove = gtk.Button("Remove")
    464:        frame = gtk.Frame("Paths")
    466:        vbox = gtk.VBox(False, 2)
    469:        hbox = gtk.HBox(False, 2)
    476:        sw = gtk.ScrolledWindow()
    492:        frame = gtk.Frame("Network")
    494:        vbox = gtk.VBox(False, 2)
    496:        hbox = gtk.HBox(False, 2)
    499:        self.net_enabled = gtk.CheckButton("Accept incoming connections")
    510:        self.entry_port = gtk.Entry()
    516:        self.entry_gpsport = gtk.Entry()
    527:        lab = gtk.Label("GPS Port:")
    536:        lab = gtk.Label("Port:")
    549:        hbox = gtk.HBox(False, 2)
    551:        self.but_on = gtk.Button("On")
    557:        self.but_off = gtk.Button("Off")
    569:        frame = gtk.Frame("Repeater Callsign")
    571:        hbox = gtk.HBox(False, 2)
    573:        self.entry_id = gtk.Entry()
    603:        frame = gtk.Frame("Authentication")
    605:        hbox = gtk.HBox(False, 20)
    610:        self.req_auth = gtk.CheckButton("Require Authentication")
    617:        self.trust_local = gtk.CheckButton("Trust localhost")
    628:        edit_users = gtk.Button("Edit Users")
    640:        vbox = gtk.VBox(False, 5)
    642:        hbox = gtk.HBox(False, 5)
    658:        frame = gtk.Frame("Connected Paths")
    663:        self.conn_list = gtk.ScrolledWindow()
    673:        frame = gtk.Frame("Traffic Monitor")
    675:        self.traffic_buffer = gtk.TextBuffer()
    676:        self.traffic_view = gtk.TextView(buffer=self.traffic_buffer)
    677:        self.traffic_view.set_wrap_mode(gtk.WRAP_WORD)
    684:        sw = gtk.ScrolledWindow()
    685:        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    695:        vbox = gtk.VBox(False, 5)
    810:        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    816:        vbox = gtk.VBox(False, 5)
    818:        self.tabs = gtk.Notebook()
    819:        self.tabs.append_page(self.make_settings(), gtk.Label("Settings"))
    821:        # self.tabs.append_page(self.make_monitor(), gtk.Label("Monitor"))
    897:        gtk.main()

    TODO
    4:of pygtk (unmaintaned) dependency.

    README.md
    26:Once you have homebrew, install gtk3
    28:    brew install pygobject3 --with-python@2 gtk+3

    setup.py
    59:    OPTIONS = {'argv_emulation': True, "includes" : "gtk,atk,pangocairo,cairo"}

    d-rats_mapdownloader
    27:class MapDownloader(gtk.Window):
    32:        l = gtk.Label(text)
    39:        box = gtk.HBox(True, 2)
    41:        l = gtk.Label(label)
    61:        box = gtk.HBox(True, 2)
    63:        l = gtk.Label(label)
    86:        frame = gtk.Frame("Bounds")
    88:        box = gtk.VBox(True, 2)
    186:        d = gtk.MessageDialog(buttons=gtk.BUTTONS_OK, parent=self)
    193:        d = gtk.MessageDialog(buttons=gtk.BUTTONS_OK, parent=self)
    231:        box = gtk.HBox(True, 2)
    233:        self.start_button = gtk.Button(_("Start"))
    238:        self.stop_button = gtk.Button(_("Stop"))
    252:        frame = gtk.Frame(_("Controls"))
    254:        box = gtk.VBox(False, 2)
    256:        self.progbar = gtk.ProgressBar()
    259:        self.status = gtk.Label("")
    274:        box = gtk.VBox(False, 2)
    285:        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
    300:        gtk.main_quit()
    308:    gtk.main()

    devboneyard/search_replace.py
    25:findReplace(".", "import gtk", ".", "*.py")

    d_rats/mainapp.py
    76:from .utils import hexprint,filter_to_ascii,NetFile,log_exception,run_gtk_locked
    595:        @run_gtk_locked

    d_rats/ui/main_events.py
    316:    @utils.run_gtk_locked
    359:        @utils.run_gtk_locked
    362:        @utils.run_gtk_locked

    d_rats/ui/conntest.py
    26:    from gtk import Assistant as baseclass

    d_rats/geocode_ui.py
    32:    from gtk import Assistant as baseclass

    d_rats/mapdisplay.py
    495:    @utils.run_gtk_locked
    1481:        @utils.run_gtk_locked

    d_rats/session_coordinator.py
    31:from .utils import run_safe, run_gtk_locked
    399:    @run_gtk_locked

    d_rats/mainwindow.py
    36:import gtk.glade
    78:        gtk.main_quit()
    86:            d = gtk.AboutDialog()
    90:                ".".join([str(x) for x in gtk.gtk_version]),
    91:                ".".join([str(x) for x in gtk.pygtk_version]),
    111:                d = gtk.MessageDialog(buttons=gtk.BUTTONS_OK,
    153:            wtree = gtk.glade.XML(c.ship_obj_fn("ui/mainwindow.glade"),
    162:            if r == gtk.RESPONSE_OK:
    191:        img = gtk.Image()
    200:        img = gtk.Image()
    253:        wtree = gtk.glade.XML(config.ship_obj_fn("ui/mainwindow.glade"),
    324:    wtree = gtk.glade.XML("ui/mainwindow.glade", "mainwindow")
    337:    gtk.main()

    d_rats/platform.py
    27:def import_gtk():
    88:        Gtk = import_gtk()
    109:        Gtk = import_gtk()
    132:        Gtk = import_gtk()

    d_rats/sessions/rpc.py
    514:            result["pygtkver"] = ".".join([str(x) for x in Gtk.pygtk_version])
    515:            result["gtkver"] = ".".join([str(x) for x in Gtk.gtk_version])
    517:            result["pygtkver"] = result["gtkver"] = "Unknown"

    d_rats/utils.py
    26:def import_gtk():
    35:    Gtk = import_gtk()
    121:def run_gtk_locked(f):
    122:    Gtk = import_gtk()
    137:    Gtk = import_gtk()
    155:    Gtk = import_gtk()
    265:    Gtk = import_gtk()
    290:    Gtk = import_gtk()

    build/scripts-3.7/d-rats_repeater
    428:        gtk.main_quit()
    434:        gtk.main_quit()
    437:        vbox = gtk.VBox(False, 2)
    439:        but_add = gtk.Button("Add")
    445:        but_remove = gtk.Button("Remove")
    464:        frame = gtk.Frame("Paths")
    466:        vbox = gtk.VBox(False, 2)
    469:        hbox = gtk.HBox(False, 2)
    476:        sw = gtk.ScrolledWindow()
    492:        frame = gtk.Frame("Network")
    494:        vbox = gtk.VBox(False, 2)
    496:        hbox = gtk.HBox(False, 2)
    499:        self.net_enabled = gtk.CheckButton("Accept incoming connections")
    510:        self.entry_port = gtk.Entry()
    516:        self.entry_gpsport = gtk.Entry()
    527:        lab = gtk.Label("GPS Port:")
    536:        lab = gtk.Label("Port:")
    549:        hbox = gtk.HBox(False, 2)
    551:        self.but_on = gtk.Button("On")
    557:        self.but_off = gtk.Button("Off")
    569:        frame = gtk.Frame("Repeater Callsign")
    571:        hbox = gtk.HBox(False, 2)
    573:        self.entry_id = gtk.Entry()
    603:        frame = gtk.Frame("Authentication")
    605:        hbox = gtk.HBox(False, 20)
    610:        self.req_auth = gtk.CheckButton("Require Authentication")
    617:        self.trust_local = gtk.CheckButton("Trust localhost")
    628:        edit_users = gtk.Button("Edit Users")
    640:        vbox = gtk.VBox(False, 5)
    642:        hbox = gtk.HBox(False, 5)
    658:        frame = gtk.Frame("Connected Paths")
    663:        self.conn_list = gtk.ScrolledWindow()
    673:        frame = gtk.Frame("Traffic Monitor")
    675:        self.traffic_buffer = gtk.TextBuffer()
    676:        self.traffic_view = gtk.TextView(buffer=self.traffic_buffer)
    677:        self.traffic_view.set_wrap_mode(gtk.WRAP_WORD)
    684:        sw = gtk.ScrolledWindow()
    685:        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    695:        vbox = gtk.VBox(False, 5)
    810:        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    816:        vbox = gtk.VBox(False, 5)
    818:        self.tabs = gtk.Notebook()
    819:        self.tabs.append_page(self.make_settings(), gtk.Label("Settings"))
    821:        # self.tabs.append_page(self.make_monitor(), gtk.Label("Monitor"))
    897:        gtk.main()

    build/scripts-3.7/d-rats_mapdownloader
    27:class MapDownloader(gtk.Window):
    32:        l = gtk.Label(text)
    39:        box = gtk.HBox(True, 2)
    41:        l = gtk.Label(label)
    61:        box = gtk.HBox(True, 2)
    63:        l = gtk.Label(label)
    86:        frame = gtk.Frame("Bounds")
    88:        box = gtk.VBox(True, 2)
    186:        d = gtk.MessageDialog(buttons=gtk.BUTTONS_OK, parent=self)
    193:        d = gtk.MessageDialog(buttons=gtk.BUTTONS_OK, parent=self)
    231:        box = gtk.HBox(True, 2)
    233:        self.start_button = gtk.Button(_("Start"))
    238:        self.stop_button = gtk.Button(_("Stop"))
    252:        frame = gtk.Frame(_("Controls"))
    254:        box = gtk.VBox(False, 2)
    256:        self.progbar = gtk.ProgressBar()
    259:        self.status = gtk.Label("")
    274:        box = gtk.VBox(False, 2)
    285:        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
    300:        gtk.main_quit()
    308:    gtk.main()

    build/scripts-3.6/d-rats_repeater
    428:        gtk.main_quit()
    434:        gtk.main_quit()
    437:        vbox = gtk.VBox(False, 2)
    439:        but_add = gtk.Button("Add")
    445:        but_remove = gtk.Button("Remove")
    464:        frame = gtk.Frame("Paths")
    466:        vbox = gtk.VBox(False, 2)
    469:        hbox = gtk.HBox(False, 2)
    476:        sw = gtk.ScrolledWindow()
    492:        frame = gtk.Frame("Network")
    494:        vbox = gtk.VBox(False, 2)
    496:        hbox = gtk.HBox(False, 2)
    499:        self.net_enabled = gtk.CheckButton("Accept incoming connections")
    510:        self.entry_port = gtk.Entry()
    516:        self.entry_gpsport = gtk.Entry()
    527:        lab = gtk.Label("GPS Port:")
    536:        lab = gtk.Label("Port:")
    549:        hbox = gtk.HBox(False, 2)
    551:        self.but_on = gtk.Button("On")
    557:        self.but_off = gtk.Button("Off")
    569:        frame = gtk.Frame("Repeater Callsign")
    571:        hbox = gtk.HBox(False, 2)
    573:        self.entry_id = gtk.Entry()
    603:        frame = gtk.Frame("Authentication")
    605:        hbox = gtk.HBox(False, 20)
    610:        self.req_auth = gtk.CheckButton("Require Authentication")
    617:        self.trust_local = gtk.CheckButton("Trust localhost")
    628:        edit_users = gtk.Button("Edit Users")
    640:        vbox = gtk.VBox(False, 5)
    642:        hbox = gtk.HBox(False, 5)
    658:        frame = gtk.Frame("Connected Paths")
    663:        self.conn_list = gtk.ScrolledWindow()
    673:        frame = gtk.Frame("Traffic Monitor")
    675:        self.traffic_buffer = gtk.TextBuffer()
    676:        self.traffic_view = gtk.TextView(buffer=self.traffic_buffer)
    677:        self.traffic_view.set_wrap_mode(gtk.WRAP_WORD)
    684:        sw = gtk.ScrolledWindow()
    685:        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    695:        vbox = gtk.VBox(False, 5)
    810:        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    816:        vbox = gtk.VBox(False, 5)
    818:        self.tabs = gtk.Notebook()
    819:        self.tabs.append_page(self.make_settings(), gtk.Label("Settings"))
    821:        # self.tabs.append_page(self.make_monitor(), gtk.Label("Monitor"))
    897:        gtk.main()

    build/scripts-3.6/d-rats
    38:    gtk.gdk.pointer_ungrab()
    39:    gtk.gdk.keyboard_ungrab()
    55:        dialog.add_button(_("Debug Log"), gtk.RESPONSE_HELP);
    56:        dialog.add_button(_("Ignore"), gtk.RESPONSE_CLOSE);
    58:        dialog.add_button(gtk.STOCK_QUIT, gtk.RESPONSE_CANCEL);
    59:        dialog.set_default_response(gtk.RESPONSE_CANCEL)
    63:                                    gtk.BUTTONS_NONE,
    64:                                    gtk.MESSAGE_ERROR,
    66:        if r == gtk.RESPONSE_CANCEL:
    68:        elif r == gtk.RESPONSE_CLOSE:
    73:        elif r == gtk.RESPONSE_HELP:

    build/scripts-3.6/d-rats_mapdownloader
    27:class MapDownloader(gtk.Window):
    32:        l = gtk.Label(text)
    39:        box = gtk.HBox(True, 2)
    41:        l = gtk.Label(label)
    61:        box = gtk.HBox(True, 2)
    63:        l = gtk.Label(label)
    86:        frame = gtk.Frame("Bounds")
    88:        box = gtk.VBox(True, 2)
    186:        d = gtk.MessageDialog(buttons=gtk.BUTTONS_OK, parent=self)
    193:        d = gtk.MessageDialog(buttons=gtk.BUTTONS_OK, parent=self)
    231:        box = gtk.HBox(True, 2)
    233:        self.start_button = gtk.Button(_("Start"))
    238:        self.stop_button = gtk.Button(_("Stop"))
    252:        frame = gtk.Frame(_("Controls"))
    254:        box = gtk.VBox(False, 2)
    256:        self.progbar = gtk.ProgressBar()
    259:        self.status = gtk.Label("")
    274:        box = gtk.VBox(False, 2)
    285:        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
    300:        gtk.main_quit()
    308:    gtk.main()

    build/lib/d_rats/mainapp.py
    76:from .utils import hexprint,filter_to_ascii,NetFile,log_exception,run_gtk_locked
    595:        @run_gtk_locked

    build/lib/d_rats/ui/main_events.py
    316:    @utils.run_gtk_locked
    359:        @utils.run_gtk_locked
    362:        @utils.run_gtk_locked

    build/lib/d_rats/ui/conntest.py
    26:    from gtk import Assistant as baseclass

    build/lib/d_rats/geocode_ui.py
    32:    from gtk import Assistant as baseclass

    build/lib/d_rats/mapdisplay.py
    495:    @utils.run_gtk_locked
    1481:        @utils.run_gtk_locked

    build/lib/d_rats/session_coordinator.py
    31:from .utils import run_safe, run_gtk_locked
    399:    @run_gtk_locked

    build/lib/d_rats/mainwindow.py
    94:                ".".join([str(x) for x in Gtk.gtk_version]),
    95:                ".".join([str(x) for x in Gtk.pygtk_version]),

    build/lib/d_rats/platform.py
    27:def import_gtk():
    88:        Gtk = import_gtk()
    109:        Gtk = import_gtk()
    132:        Gtk = import_gtk()

    build/lib/d_rats/sessions/rpc.py
    514:            result["pygtkver"] = ".".join([str(x) for x in Gtk.pygtk_version])
    515:            result["gtkver"] = ".".join([str(x) for x in Gtk.gtk_version])
    517:            result["pygtkver"] = result["gtkver"] = "Unknown"

    build/lib/d_rats/utils.py
    26:def import_gtk():
    35:    Gtk = import_gtk()
    121:def run_gtk_locked(f):
    122:    Gtk = import_gtk()
    137:    Gtk = import_gtk()
    155:    Gtk = import_gtk()
    265:    Gtk = import_gtk()
    290:    Gtk = import_gtk()

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
