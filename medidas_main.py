#coding: utf-8
#from kivy import Config
#Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class RootWidget(FloatLayout):
    pass

class MedidaApp(App):

    def build(self):
        return RootWidget()

MedidaApp().run()
