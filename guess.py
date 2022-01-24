# """total no of guess 9
# take the input
# reduce the chances left """
# import random

# def Guess_the_number():
#     guess= random.randint(1,100)
#     for i in range(1,10):
#         num = int(input("Enter Guess Number ")) 
#         if(num == guess):
#             print("Correct Answer!! Good luck... ",guess)
#             break
#         elif (num < guess):
#             print("Wrong Answer Too Low")
#         elif (num > guess):
#             print("Wrong Answer!! Too  high")
#         if(i==9):
#             print("No More Guess Left")
#             break
#         else:
#             print(f"No. of Guesses Left = {9-i}")

# if __name__ == '__main__':
#     Guess_the_number()

import random

def Guess_the_number():
    guess= 18
    for i in range(1,10):
        num = int(input("Enter Guess Number ")) 
        if(num == guess):
            print("Correct Answer!! Good luck... ",guess)
            break
        elif (num < guess):
            print("Wrong Answer Too Low")
        elif (num > guess):
            print("Wrong Answer!! Too  high")
        if(i==9):
            print("No More Guess Left")
            break
        else:
            print(f"No. of Guesses Left = {9-i}")

if __name__ == '__main__':
    Guess_the_number()


