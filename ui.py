import kivy
import subprocess
kivy.require("1.8.0")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

import sortPictures


class SortPictures(App):


    def sortNow(self,instance):
        print "test"
        sortPictures.sort("/home/kon/sort-pictures-by-date/","/home/kon/sort-pictures-by-date/")

    def build(self):
        layout = GridLayout(cols=2, rows=3)
        button = Button(text='Sort Now')
        button.bind(on_press=self.sortNow)
        label1 = Label(text='Source Directory')
        label2 = Label(text='placeholder2')
        label3 = Label(text='Target Directory')
        label4 = Label(text='placeholder4')
        label5 = Label(text='placeholder5')
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(label4)
        layout.add_widget(label5)
        layout.add_widget(button)
        return layout


if __name__ == '__main__':
    SortPictures().run()