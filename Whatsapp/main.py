import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

mouse = Controller()

#instruciones para el bot de whatsapp
class WhatsApp:
    
    #Defines the starting values
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.lastmessage = ''

    #Navegar por nuevos mensajes
    def  nav_green_dot(self):
        try:
            position = pt.locateOnScreen(r'C:\Users\Leonel\hello\Whatsapp/green_dot.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100,0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot: ', e)


wa_bot = WhatsApp(speed=.5, click_speed=.4)
sleep(2)
wa_bot.nav_green_dot()        
            