import os
import eel

from features import *
from command import *


eel.init("www")

playAssistantsound()


os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html',mode=None, host= 'localhost', block=True)

