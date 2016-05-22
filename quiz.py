

def main():

    print("Author: David Silveiro                  \n \
    
    print("Would you like to start from the start? \n \
          Or perhaps an exact level?               \n")
           
    print("1) From the beginning     \n \
           2) Level 1: Operations    \n \
           3) Level 2:               \n \
           4)                        \n \
           5)                        \n")
    
    answer = int(raw_input("Answer: "))
    
    if answer == 1:
        from modules import operators
    elif answer == 2:
        from modules import memory
    elif answer == 3:
        
    elif answer == 4:
        
    elif answer == 5:
    
    else:


if __name__ == "__main__":
    main()
