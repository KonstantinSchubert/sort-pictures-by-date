# This is my attempt at using kivy for develpment

import kivy
import subprocess
kivy.require("1.8.0")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserIconView

import sortPictures


class SortPictures(App):


    def sortNow(self,instance):
        sortPictures.sort("/home/kon/sort-pictures-by-date/","/home/kon/sort-pictures-by-date/")

    def build(self):
        layout = GridLayout(cols=2, rows=3)

        label1 = Label(text='Source Directory')
        layout.add_widget(label1)
        
        sourceDirSelector = FileChooserIconView(dirselect=True)
        layout.add_widget(sourceDirSelector)
        
        label3 = Label(text='Target Directory')
        layout.add_widget(label3)
        
        targetDirSelector = FileChooserIconView(dirselect=True)
        layout.add_widget(targetDirSelector )

        label5 = Label(text='placeholder5')
        layout.add_widget(label5)
        
        button = Button(text='Sort Now')
        button.bind(on_press=self.sortNow)
        layout.add_widget(button)
        return layout


if __name__ == '__main__':
    SortPictures().run()