"""
Wrapper for colorama color text
"""
from colorama import Fore, Style
from collections import UserString

class ColorString(UserString):
    def __init__(self, string, color):
        self.data = color + string + Style.RESET_ALL

class RedString(ColorString):
    def __init__(self, string):
        super().__init__(string, Fore.RED)

class YellowString(ColorString):
    def __init__(self, string):
        super().__init__(string, Fore.RED)

class GreenString(ColorString):
    def __init__(self, string):
        super().__init__(string, Fore.GREEN)   

class YellowString(ColorString):
    def __init__(self, string):
        super().__init__(string, Fore.YELLOW)         