from kivymd.app import MDApp
from kivy.uix.button import Button

class GigataskApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"

if __name__ == "__main__":
    app = GigataskApp()
    app.run()

