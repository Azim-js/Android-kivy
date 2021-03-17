from kivy.app import App
from kivy.lang import Builder
from kivy.uix.pagelayout import PageLayout

Builder.load_file("page_design.kv")

class MyPageLayout(PageLayout):
    pass

class PageLayoutApp(App):
    def build(self):
        return MyPageLayout()

if __name__=="__main__":
    PageLayoutApp().run()