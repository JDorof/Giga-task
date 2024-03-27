from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime

class TaskCreationMenu(MDBoxLayout):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

class GigataskApp(MDApp):

    task_list_menu = None

    # Methods

    def build(self):
        self.theme_cls.primary_palette = "Blue"
    
    def show_task_menu(self):
        if not self.task_list_menu:
            self.task_list_menu = MDDialog(
                title = "Create a new task",
                type = "custom",
                content_cls = TaskCreationMenu(),
            )
        self.task_list_menu.open()

    def close_task_menu(self, *args):
        self.task_list_menu.dismiss()

    def add_task(self, task_text, task_date):
        print(task_text.text, task_date)
        task_text.text = ""


if __name__ == "__main__":
    app = GigataskApp()
    app.run()

