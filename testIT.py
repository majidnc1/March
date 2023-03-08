import pyfiglet
from termcolor import colored

text = "Happy March 8"
ascii_art = pyfiglet.figlet_format(text, font='big')
colored_ascii_art = colored(ascii_art, 'red')
print(colored_ascii_art)
