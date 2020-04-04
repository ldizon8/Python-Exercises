'''Character Input Exercise

Create a program that asks the user to enter their name and age. Print out the message that would tell them the year when they turn 100 years old.

'''
import datetime

name = input("Hi, please enter your name: ")

age = int(input("Please enter your age: "))

today = datetime.datetime.now()

print("Hi " + name + ", you will be 100 in the year " + str((int(today.year) - age) + 100) + ".")




