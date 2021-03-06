from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file("d2.kv")

class MyWidget(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__=="__main__":
    MyApp().run()