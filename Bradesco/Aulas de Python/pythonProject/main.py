from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        Label= Label(text='Fala galera!'
            size_hint={.5, .5},
            pos_hint={'center_x': .5, 'center_y': .5})


