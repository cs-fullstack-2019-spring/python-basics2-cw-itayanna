def main():
    #problem1()
    #problem2()
    #problem3()
    #problem4()


def problem1():
    import random
    ranNum = random.randint(0,15)
    print(ranNum)

def problem2():
    userInput= input("Enter a color.Enter q to quit")
    while userInput!="q":
        userInput= input("Enter a color.Enter q to quit")


def problem3():
    uI= ""
    while uI!="0":
        uI= input('Enter va positive number. Enter a 0 to quit ')
        print(uI+str(0))

def problem4():
    import random
    ranNum= random.randint(0,20)
    uI= ""
    while ranNum!=uI:
        uI= int(input("Guess a number between 0 and 20."))
        if uI>ranNum:
            print("Lower")
        else:
            print("Higher")
    print("taht's correct")
























if __name__ == '__main__':
    main()