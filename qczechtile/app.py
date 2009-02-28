# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from czechtile import parse, expand, register_map, expander_map


class CzechtileApplication(object):
    def __init__(self, argv):
        self.application = QtGui.QApplication(argv)
    
    def create_main_layout(self, parent=None):
        if not parent:
            parent = self.main
        
        self.main_widget = QtGui.QWidget(parent)
        self.main.setCentralWidget(self.main_widget)
        
        self.czt_label = QtGui.QLabel(u"Czechtile text:")
        self.czt_text = QtGui.QTextEdit()
        self.converted_label = QtGui.QLabel(u"Zkonvertovaný text")
        self.converted_text = QtGui.QTextEdit()

        self.xhtml_convert_button = QtGui.QPushButton(u"Převeď do XHTML")
        self.docbook5_convert_button = QtGui.QPushButton(u"Převeď do DocBooku5")
        
        self.layout = l= QtGui.QGridLayout(self.main_widget)
        
        l.addWidget(self.czt_label, 0, 0)
        l.addWidget(self.czt_text, 0, 1)
        
        l.addWidget(self.xhtml_convert_button, 1, 1)
        #l.addWidget(self.docbook5_convert_button, 1, 1)
        
        l.addWidget(self.converted_label, 2, 0)
        l.addWidget(self.converted_text, 2, 1)
        
        self.main_widget.setLayout(self.layout)
        
        # signals
        self.main.connect(self.xhtml_convert_button, QtCore.SIGNAL("clicked()"), self.xhtml_convert)
        #self.main.connect(self.docbook5_convert_button, QtCore.SIGNAL("clicked()"), self.docbook5_convert)
    
    def execute(self):
        self.main = QtGui.QMainWindow()
        self.main.setWindowTitle(u"QCzechtile")
        self.create_main_layout()

        
        self.main.show()
        return self.application.exec_()

    
    def xhtml_convert(self):
        tree = parse(unicode(self.czt_text.toPlainText()), register_map)
        result = expand(tree, 'xhtml11', expander_map)
        
        self.converted_text.setText(result)
