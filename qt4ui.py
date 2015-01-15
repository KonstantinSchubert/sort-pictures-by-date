#!/usr/bin/python
# -*- coding: utf-8 -*-



import sys
from PyQt4 import QtGui
import sortPictures


class SortPicturesUi(QtGui.QWidget):
    
    def __init__(self):
        super(SortPicturesUi, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        self.setGeometry(100, 100, 250, 150)
        self.center()
        self.setWindowTitle('Icon')


        sortButton.clicked.connect(sortNow)
        sortButton.clicked.connect(self.showDialog)
        sortButton.resize(sortButton.sizeHint())
        sortButton.move(50, 50)       
        
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        FOR OPENING A QFileDialog
        # someButtonp = QtGui.QPushButton("Sort",self)
    # def showDialog(self):

    #     fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
    #             '/home')




def sortNow():
    sortPictures.sort("/home/kon/sort-pictures-by-date/","/home/kon/sort-pictures-by-date/")
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = SortPicturesUi()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    