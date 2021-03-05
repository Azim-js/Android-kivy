import kivy
# kivy.require('1.9.0 ')
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.button import Label

Builder.load_file("design.kv")

class HelloApp(App):
    def build(Self):
        return Label()

if __name__=="__main__":
    HelloApp().run()
