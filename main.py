from kivy.app import App
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from plyer import battery,tts,vibrator
from kivymd.toast import toast
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import pyttsx3


root_kv = """
BoxLayout:
    orientation:'vertical'
    spacing:dp(20)
    MDRaisedButton:
        text:"Battery"
        on_release:
            app.show_battery_info()

    MDRaisedButton:
        text:"Vibrate"
        on_release:
            app.vibrate()

    MDTextField:
        id:field
        hint_text:"TEXT TO SPEECH"

    MDRaisedButton:
        text:"TTS"
        on_release:
            app.speak(field.text)
            
"""

class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        self.theme_cls.theme_style = "Dark"
        #theme_cls=ThemeManager()
        super().__init__(**kwargs)

    

    def say(self,words):
        engine = pyttsx3.init()
        engine.say(words)
        engine.runAndWait()

    def show_battery_info(self):
        print(battery.status)
        toast(str(battery.status))

    def vibrate(self):
        vibrator.vibrate(time=2)

    def speak(self,text_to_read):
        #print(text_to_read)
        self.say(text_to_read)


    def build(self):
        #return MainApp()
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MainApp().run()
