from kivy.app import App
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout

Builder.load_file("stack_design.kv")

class MyStackLayout(StackLayout):
    pass

class MylayoutApp(App):
    def build(self):
        return MyStackLayout()

if __name__=="__main__":
    MylayoutApp().run()        