from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_file("grid_design.kv")

class MyGridLayout(GridLayout):
    pass

class MyLayoutApp(App):
    def build(self):
        return MyGridLayout()

if __name__ =="__main__":
    MyLayoutApp().run()        