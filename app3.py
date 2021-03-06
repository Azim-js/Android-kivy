from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file("d3.kv")

class FloatLayoutApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    FloatLayoutApp().run()