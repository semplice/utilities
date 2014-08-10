#!/usr/bin/env python
# semplice-utilities setup (using distutils)
# Copyright (C) 2011 Eugenio "g7" Paolantonio. All rights reserved.
# Work released under the GNU GPL license, version 3.

from distutils.core import setup

setup(name='semplice-utilities',
      version='6.21.0',
      description='Semplice Linux Utilities',
      author='Eugenio Paolantonio and the Semplice Team',
      author_email='me@medesimo.eu',
      url='http://launchpad.net/semplice',
      scripts=['semplice-about', 'semplice-change-face', 'semplice-logout', 'semplice-upgrade', 'xdg-autostart',],
      data_files=[("/usr/bin", ["semplice-help-irc", "mirrorselect", "open-mixer"]), ("/usr/share/semplice-utilities", ["semplicelogo.png"]), ("/usr/share/semplice-utilities/mirrorselect", ["semplice.list"]), ("/usr/share/semplice-utilities/logout", ["logout.glade"]), ("/usr/share/semplice-utilities/change-face", ["avatar.glade"])],
      requires=['os', 'sys', 'time', 'glob', 'pygtk', 'gtk', 'gtk.gdk', 'dbus', 'threading', 'xdg', 'xdg.DesktopEntry', 'xdg.Exceptions'],
     )
