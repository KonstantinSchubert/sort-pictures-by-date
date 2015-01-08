#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
import sortPictures


class SortPicturesUi(QtGui.QWidget):
    
    def __init__(self):
        super(SortPicturesUi, self).__init__()
        
        self.initUI()
        
    def initUI(self):

    	sortButton = QtGui.QPushButton('Sort', self)
    	sortButton.clicked.connect(sortNow)
        sortButton.resize(sortButton.sizeHint())
        sortButton.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
    
        self.show()

def sortNow():
    sortPictures.sort("/home/kon/sort-pictures-by-date/","/home/kon/sort-pictures-by-date/")
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = SortPicturesUi()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    