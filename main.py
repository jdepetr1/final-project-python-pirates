import pygame
from src import controller

def main():
  pygame.init() #uncomment this line later
    #Create an instance on your controller object
    #Call your mainloop
  cont = controller.Controller()
  cont.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
