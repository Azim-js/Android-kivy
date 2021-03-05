from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("d1.kv")

class MyWidget(Widget):
    pass

class WidgetsApp(App):
    def build(self):
        return MyWidget()

if __name__=="__main__":
    WidgetsApp().run()