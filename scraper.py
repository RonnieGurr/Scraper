import sys
import scraperEngine

def menu():    
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Get links"
    print "2. Get images"
    print "3. Define save location"
    print "4. Exit"
    print 67 * "-"
  
loop = True      
  
while loop:         
    menu()  
    choice = input("Enter your choice [1-4]: ")
     
    if choice==1:     
        link = raw_input("Please enter the URL of the page: ")
        element = raw_input("Please enter the class name which holds the A elements: ")
        scraperEngine.getLinks(link, element)
    elif choice==2:
        print "Menu 2 has been selected"
    elif choice==3:
        print "Menu 3 has been selected"
    elif choice==4:
        print('Goodbye!')
        loop=False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")