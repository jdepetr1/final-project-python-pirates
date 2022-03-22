#import pygame
#import your controller

def main():

  mylist = []

  for i in range(4):
    num = int(input("Input an integer: "))
    mylist.append(num)

  for i in range(4):
    print("mylist[" + str(i) + "] = " + str(mylist[i]))

  mylist[0],mylist[3] = mylist[3],mylist[0]
  print(mylist)
    #pygame.init() #uncomment this line later
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
