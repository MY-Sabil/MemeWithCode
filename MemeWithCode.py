from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

class MemeWithCode(App):
    def build(self):
        self.icon = 'yes.png'
        Window.size = (600, 600)
        Window.clearcolor = (1, 1, 1, 1)
        self.window = GridLayout(cols=2, rows=2)
        self.window.add_widget(Image(source="no.jpg"))
        self.window.add_widget(Label(text="[color=000000][size=30px]Making memes\nwith Photoshop[/size][/color]", markup = True, halign="center"))
        self.window.add_widget(Image(source="yes.png"))
        self.window.add_widget(Label(text="[color=000000][size=30px]Making memes\nwith code[/size][/color]", markup = True, halign="center"))
        return self.window

if __name__ == "__main__":
    MemeWithCode().run()