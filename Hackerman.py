# Setup
from pynput.keyboard import Key, Controller, KeyCode, Listener
import time 
import threading
from random import randint

keyboard = Controller() 
delay =  0.1
keyzzz = "wasd"
start_stop_key = KeyCode(char='x')
exit_key = KeyCode(char='z')
# End of Setup

# Making sure things stop and start at times when they should
class PressKey(threading.Thread):
	def __init__(self, delay):
		super(PressKey, self).__init__()
		self.delay = delay # Delay
		self.running = False # These two are for starting and stopping
		self.program_running = True

	def start_stuff(self):
		self.running = True # Improving an intuitive "interface"
	def stop_stuff(self): 
		self.running = False
	def exit(self):
		self.stop_stuff()
		self.program_running = False

	def run(self): # When it actually runs
		while self.program_running:
			while self.running:
				keyboard.press("w") # Presses a key
				keyboard.press("a") # Presses a key
				keyboard.press("s") # Presses a key
				keyboard.press("d") # Presses a key
				time.sleep(self.delay)

				'''
				keyboard.release(keyzzz) # Release the key...?
				time.sleep(self.delay)
				'''

			time.sleep(0.1) # Important thing here...

# Setting a PressKey instance
PressKey_instance = PressKey(delay)
PressKey_instance.start()


# Listener that signals and controls stuff
def on_press(key):
	if key == start_stop_key:
			if PressKey_instance.running:
			    PressKey_instance.stop_stuff()
			else:
			    PressKey_instance.start_stuff()
	elif key == exit_key: # Getting out of the program
		PressKey_instance.exit()
		listener.stop()

# Intelligent stuff
with Listener(on_press=on_press) as listener:
	listener.join()
