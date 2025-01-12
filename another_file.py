from kivymd.app import MDApp
from kivy.uix.screenmanager import  Screen , ScreenManager
from kivy.lang import Builder

# Builder String 
builder_string = '''

ScreenManager:
    Hello:
    Bye:
    
<Hello>:
    name:'hello'
    MDLabel:
        text:'Hello! World'
        halign: 'center'
        font_style: 'H1'

    MDRectangleFlatIconButton:
        icon: 'android'
        text: 'Hello'
        user_font_size: '100sp'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release:
            root.manager.current = 'bye'
            root.manager.transition.direction = 'left'

<Bye>:
    name:'bye'
    MDLabel:
        text:'Hello'
        halign: 'center'
        font_style: 'H1'

    MDRectangleFlatIconButton:
        icon: 'android'
        text: 'Hello'
        user_font_size: '100sp'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release:
            root.manager.current = 'hello'
            root.manager.transition.direction = 'right'


'''

class Hello(Screen):
    pass

class Bye(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Hello(name = 'hello'))
sm.add_widget(Bye(name = 'bye'))

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.build_str = Builder.load_string(builder_string)
        screen.add_widget(self.build_str)
        return screen
DemoApp().run()