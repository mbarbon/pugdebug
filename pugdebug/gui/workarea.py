# -*- coding: utf-8 -*-

"""
    pugdebug - a standalone PHP debugger
    =========================
    copyright: (c) 2015 Robert Basic
    license: GNU GPL v3, see LICENSE for more details
"""

__author__="robertbasic"

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from pugdebug.gui.files import PugdebugFileViewer
from pugdebug.gui.variables import PugdebugVariableViewer
from pugdebug.gui.stacktraces import PugdebugStacktraceViewer
from pugdebug.gui.breakpoints import PugdebugBreakpointViewer

class PugdebugWorkareaWindow(QWidget):

    def __init__(self, parent):
        super(PugdebugWorkareaWindow, self).__init__(parent)

        self.file_viewer = PugdebugFileViewer()
        self.variable_viewer = PugdebugVariableViewer()
        self.stacktrace_viewer = PugdebugStacktraceViewer()
        self.breakpoint_viewer = PugdebugBreakpointViewer()

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.file_viewer, 0, 0, 1, 1)
        layout.addWidget(self.variable_viewer, 0, 1, 1, 1)
        layout.addWidget(self.stacktrace_viewer, 1, 0, 1, 1)
        layout.addWidget(self.breakpoint_viewer, 1, 1, 1, 1)
