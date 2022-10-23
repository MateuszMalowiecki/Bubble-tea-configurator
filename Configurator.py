from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class ConfigurationWindow(Screen):
    base_selection = ObjectProperty(None)
    price_label = ObjectProperty(None)
    size_selection = ObjectProperty(None)
    have_cup = False
    def count_prize(self):
        price = 16
        if self.size_selection.text == "Big":
            price += 4
        if self.base_selection.text == "With milk":
            price += 2
        if self.have_cup:
            price *= 0.9
        self.price_label.text = f"Price: {price}"
    def change_info_about_cap(self, instance, value):
       self.have_cup = value

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("Configurator.kv")

class ConfiguratorApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    ConfiguratorApp().run()
