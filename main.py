# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# find all letters(true love) in string
#  add strings together to create two digits
#example: name1 = 8 and name2 =6, total = 86
import re
first_name = len(re.findall('[truelove]',name1))
second_name = len(re.findall('[truelove]',name2))
total = (first_name*10 + second_name)

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")

