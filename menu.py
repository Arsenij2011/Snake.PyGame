import pygame_menu 
from settings import HEIGHT,WIDHT
class Menu:
    def main_menu(self):
        self.mainmenu = pygame_menu.Menu('Змейка', WIDHT, HEIGHT, theme = pygame_menu.themes.THEME_DARK)
        self.mainmenu.add.button('Играть',self.mainmenu.disable)  
        self.mainmenu.add.button('Выход', quit)    
        return self.mainmenu

    def loase_menu():
        self.loasemenu = pygame_menu.Menu('Игра окончена', WIDHT, HEIGHT, theme = pygame_menu.themes.THEME_DARK)
        self.loasemenu.add.button('Начать заново',self.loasemenu.disable)  
        self.loasemenu.add.button('Выход', quit)    
        return self.loase_menu


menu = Menu()


