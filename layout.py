from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_file("layout_desgin.kv")

class MyGridLayout(GridLayout):
    pass

class LayoutsApp(App):
    def build(self):
        return MyGridLayout()


if __name__=="__main__":
    LayoutsApp().run()