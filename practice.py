# from typing import List, Any
#
# import numpy as np
#
# # identity matrix
# print(np.eye(3))
#
# # zeroes matrix
# print(np.zeros((3, 4)))
#
# # ones matrix
# print(np.ones((2, 2), dtype=np.float64))
#
# Narr = np.array([np.random.rand(6)], dtype=int)
# print(Narr)
#
# Narr.astype(complex)
# print(Narr)
#
# arr1 = [25, 56, 12, 85, 34, 75]
#
# print(arr1)
# arr2 = [42, 3, 86, 32, 856, 46]
# arr1 = np.array(arr1)
# arr1 = arr1.astype('complex')
# print(arr1)
# print(arr1.dtype)
# arr1 = arr1.reshape(2, 3)
# arr2 = np.array(arr2)
# arr2 = arr2.reshape(2, 3)
# eq = (arr1 * arr1 - arr2 * arr2) / (arr1 - arr2)
# print(eq)
#
# print('%.2f' % (21 / 4))
# print(((3 + 5) // 2 * 2 ** 3) % 7)
#
# counter = 0
# while (counter * counter < 60):
#     print(counter)
#     counter += 3
#
# # factorial of a number using while
# num = int(input())
# fact = 1
# while (num > 1):
#     fact = fact * num
#     num = num - 1
#     print("fact", fact)
#     print("num", num)
# print(fact)
#
# num = int(input())
# counter = 0
# while (num >= 0):
#     char = str(counter)
#     print(char + " !")
#     counter = counter + 1
#     num = num - 1
#
#
# def captain_adder(name):
#     print("captain " + name)
#
#
# captain_adder("jack")
#
# num1 = int(input())
# num2 = int(input())
# if(num1>=num2):
#     print(num1)
#     print(num2)
# else:
#     print(num2)
#     print(num1)

"""
Ann watched a TV program about health and learned that it is recommended to sleep at least A hours per day,
but oversleeping is also not healthy, and you should not sleep more than B hours.
Now Ann sleeps H hours per day. If Ann's sleep schedule complies with the requirements of that TV program –
print "Normal". If Ann sleeps less than A hours, output “Deficiency”, and if she sleeps more than B hours,
output “Excess”.

Input to this program are the three strings with variables in the following order:
A , B , H . A  is always less than or equal to B .
"""
# A = int(input())
# B = int(input())
# H = int(input())
# if (A<=H):
#     if(H<=B):
#         print("Normal")
#     else:
#         print("Excess")
# elif(H<A):
#     print("Deficiency")

def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    option = int(input())
    op = True
    while(op):
        if option == 2:
            print("Completed, have a nice day!")
            op = False
            break
        if option != 2:
            print("Please, try again.")
            option = int(input())
            continue
       #print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
# ...
test()
end()
