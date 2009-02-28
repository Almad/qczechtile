from __future__ import absolute_import
import sys
from PyQt4 import QtCore, QtGui

from .app import CzechtileApplication

def start(argv=None):
    if not argv:
        argv = sys.argv
    app = CzechtileApplication(argv)
    sys.exit(app.execute())
