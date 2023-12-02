from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

centerx = 0.05
centery = 0.4
curx = centerx
cury = centery
switch = True

KV = '''
MDScreen:
    Image:
        id: blokje_state
        size_hint_y: 0.4
        size_hint_x: 0.4
        pos_hint: {'center_x': 0.05, 'center_y': 0.4}
        source: "assets/blokje_rood.png"
    MDRoundFlatIconButton:
        id: 'knop'
        icon: 'android'
        text: 'Dit is Amons eerste knop'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_release: app.verplaats()
    MDBoxLayout: 
        id: 'box'
        orientation: 'vertical'
        spacing: '12dp'
        pos_hint: {'top': 1}
        MDTopAppBar:
            title: 'Blokje'
            icon: 'android'
            left_action_items: [['menu', lambda x: x]]

        
'''

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen
    
    def verplaats(self):
        global curx
        global cury
        global switch
        if curx > 0.9 and switch == True:
            switch = False
            curx -= 0.1
        elif curx < 0.9 and switch == True: 
            curx += 0.1
        elif curx < 0.1 and switch == False:
            switch = True
            curx += 0.1    
        else: 
            curx -= 0.1
        #print(curx)
        self.kvs.ids.blokje_state.pos_hint = {'center_x': curx, 'center_y': cury}
        

ma = MainApp()
ma.run()