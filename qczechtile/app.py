# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from czechtile import parse, expand, register_map, expander_map

FORMAT_MAP = {
    "BB Code (phpBB)" : "bbcode",
    "XHTML 1.1" : "xhtml11",
}


class CzechtileApplication(object):
    def __init__(self, argv):
        self.application = QtGui.QApplication(argv)
        self.format = 'xhtml11'
    
    def create_main_layout(self, parent=None):
        if not parent:
            parent = self.main
        
        self.main_widget = QtGui.QWidget(parent)
        self.main.setCentralWidget(self.main_widget)
        
        self.czt_label = QtGui.QLabel(u"Czechtile text:")
        self.czt_text = QtGui.QTextEdit()
        self.converted_label = QtGui.QLabel(u"Zdrojový kód:")
        self.converted_text = QtGui.QTextEdit()

#        self.xhtml_convert_button = QtGui.QPushButton(u"Převeď do XHTML")
#        self.docbook5_convert_button = QtGui.QPushButton(u"Převeď do DocBooku5")

        self.format_label = QtGui.QLabel(u"Formát:")
        self.format_list = QtGui.QComboBox()
        
        self.preview_label = QtGui.QLabel(u"Náhled: ")
#        self.preview = QtGui.QLabel()
        self.preview = QtGui.QTextEdit()
        
        for i in FORMAT_MAP:
            self.format_list.addItem(i, QtCore.QVariant(FORMAT_MAP[i]))
        # set default to XHTML
        self.format_list.setCurrentIndex(0)
        
        self.layout = l= QtGui.QGridLayout(self.main_widget)
        l.setSpacing(10)
        
        l.addWidget(self.czt_label, 0, 0)
        l.addWidget(self.czt_text, 0, 1)
        
        l.addWidget(self.format_label, 3, 0)
        l.addWidget(self.format_list, 3, 1)
        #l.addWidget(self.docbook5_convert_button, 1, 1)
        
        l.addWidget(self.preview_label, 4, 0)
        l.addWidget(self.preview, 4, 1)
        
            
        l.addWidget(self.converted_label, 6, 0)
        l.addWidget(self.converted_text, 6, 1)
        
        self.main_widget.setLayout(self.layout)
        
        # signals
        # self.main.connect(self.xhtml_convert_button, QtCore.SIGNAL("clicked()"), self.xhtml_convert)
        # self.main.connect(self.docbook5_convert_button, QtCore.SIGNAL("clicked()"), self.docbook5_convert)
        self.main.connect(self.czt_text, QtCore.SIGNAL("textChanged()"), self.convert)
        self.main.connect(self.format_list, QtCore.SIGNAL("activated (int)"), self.format_changed)

    def execute(self):
        self.main = QtGui.QMainWindow()
        self.main.setWindowTitle(u"QCzechtile")
        self.create_main_layout()

        
        self.main.show()
        return self.application.exec_()

    
    def convert(self):
        tree = parse(unicode(self.czt_text.toPlainText()), register_map)
        result = expand(tree, self.format, expander_map)
        
        self.converted_text.setPlainText(result)
        self.preview.setText(result)
        
        #self.converted_text.setText(result)
    
    def format_changed(self, item):
        self.format = str(self.format_list.itemData(item).toString())
