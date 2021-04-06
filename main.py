# import local files
from classes.loader import *
from classes.game import *

# initialize loader
loader = Loader()
game = GameController()

# load console
console_active = True
while(console_active):
    command = input()
    if(command == "exit"):
        console_active = False
    else:
        parse_command(command, loader)

# command controller
def parse_command(command, loader):
    if(command == "start"):
        game.start();
    if(command == "load"):
        game.load();


