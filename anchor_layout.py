from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file("anchor_design.kv")

class MyGridLayout(AnchorLayout):
    pass

class MyLayoutApp(App):
    def build(self):
        return MyGridLayout()

if __name__=="__main__":
    MyLayoutApp().run()       