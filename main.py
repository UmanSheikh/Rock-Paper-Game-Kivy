import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
import time
from pygame import mixer

mixer.init()
mixer.music.load("play.wav")
mixer.music.set_volume(0.7)
class Function(BoxLayout):
    def __init__(self):
        super(Function, self).__init__()

    def rock(self):
        self.Check('r')
    def paper(self):
        self.Check('p')
    def scissors(self):
        self.Check('s')

    def Check(self, user_input):
        cpu = ['r', 'p', 's']
        choice = random.choice(cpu)
        if choice == 'r':
            time.sleep(0.4)
            self.cpu_id.text = '[b]CPU selected Rock[/b]'
        elif choice == 'p':
            time.sleep(0.4)
            self.cpu_id.text = '[b]CPU selected Paper[/b]'
        elif choice == 's':
            time.sleep(0.4)
            self.cpu_id.text = '[b]CPU selected Scissors[/b]'
    

        if user_input == choice:
            time.sleep(0.4)
            label = '[b]Draw[/b]'
            mixer.init()
            mixer.music.load("play.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif user_input == 'r' and choice == 'p':
            time.sleep(0.4)
            label = '[b]You Lose[/b]'
            mixer.init()
            mixer.music.load("play.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif user_input == 'r' and choice == 's':
            time.sleep(0.4)
            label = '[b]You Win[/b]'
            mixer.init()
            mixer.music.load("win.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif user_input == 'p' and choice == 'r':
            time.sleep(0.4)
            label = '[b]You Win[/b]'
            mixer.init()
            mixer.music.load("win.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif user_input == 'p' and choice == 's':
            time.sleep(0.4)
            label = '[b]You Lose[/b]'
            mixer.init()
            mixer.music.load("play.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif user_input == 's' and choice == 'r':
            time.sleep(0.4)
            label = '[b]You Lose[/b]'
            mixer.init()
            mixer.music.load("play.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        elif user_input == 's' and choice == 'p':
            time.sleep(0.4)
            label = '[b]You Win[/b]'
            mixer.init()
            mixer.music.load("win.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
        self.check.text = label
        
class SWcodes(App):
    def build(self):
        return Function()


if __name__ == '__main__':
    SWcodes().run()