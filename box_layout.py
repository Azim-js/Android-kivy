from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("box_design.kv")

class MyBoxLayout(BoxLayout):
    pass

class MyLayoutApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ =="__main__":
    MyLayoutApp().run()        