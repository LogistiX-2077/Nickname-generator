import time
import random

print("(Use only 'yes' or 'no' for the answer)")
nickname = ""
firstname = ""
inch = ""
choice = False
list_of_prps = ["Unknown","Solo","NoScope","360","Death","Dead","#freeNavalny","123","228","666","Just","Not","Losted","Cute","Shadow","Ghost","2077","Hunter","Anonimus","Imposter","InLoveWith","Super","President","Holy","Cool","Cold","Stupid"]
#function of choice (yes or no)
def inchoice (inch):
  global choice
  while inch != "yes" or inch != "no":
    inch = input()
    if inch == "Yes" or inch == "yes":
      inch = inch.lower()
      choice = True
      break
    if inch == "No" or inch == "no":
      inch = inch.lower()
      choice = False
      break
    else:
      print("Incorrect input, try again.")
  return 0
#function ends
firstname = input("Enter your name: ")
nickname = firstname
print("Do u want to use your last name?")
inchoice(inch)
if choice == True:
  lastname = input("Enter last name: ")
  print("Do you want to use the first two letters of the first and last name as the beginning of the nickname (example: AA (Alex Alexandrov))")
  inchoice(inch)
  if choice == True:
    nickname = firstname[0] + lastname[0]
#all digits replaces
print("Do u wanna replace all 'i' on 1?")
inchoice(inch)
if choice == True:
  nickname = nickname.replace("i","1")
print("Do u wanna replace all 'o' on 1 or 0 (amswer only on the qustion 'Do u want to replace all 'o' on digits)?")
inchoice(inch)
if choice == True:
  print("Which digits do u like more, '1' or '0' ? ")
  digitsch = int(input())
  if digitsch == 1:
    nickname = nickname.replace("o","1")
  if digitsch == 0:
    nickname = nickname.replace("o","0")
print("Do u want to replace all 'ei' on 8?")
inchoice(inch)
if choice == True:
  nickname = nickname.replace("ei","8")
print("Do u want to replace all 'to' on 2?")
inchoice(inch)
if choice == True:
  nickname = nickname.replace("to","2")
print("Do u want to replace all 'for' on 4?")
inchoice(inch)
if choice == True:
  nickname = nickname.replace("for","4")
#all about postscrips
print("Do u wanna use postscrips?")
inchoice(inch)
if choice == True:
  pripiska = ""
  print("I have the list of postscrips, I will show u it in..")
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  counter = 0
  for element in list_of_prps:
    counter += 1
    print(f"{counter}. {element}")
    time.sleep(0.5)
  print("Choose the number of postscrip which do u want to use, or enter '9999' to enter your own postscrip.")
  counter = -25
  while counter != 9999 or 0 < counter < 28:
    counter = int(input())
    if counter == 9999:
      break
    if 0 < counter < 28:
      break
    else:
      print("Incorrect input, try again.")
  if counter == 9999:
    prepiska = input("Enter your postscrip: ")
    nickname = prepiska + " " + nickname
  else:
    counter -= 1
    prepiska = list_of_prps[counter]
    nickname = prepiska + " " + nickname
#number in the end of nickname
print("Do u want to add number in the end of nickname?")
inchoice(inch)
if choice == True:
  print("Do u want to enter your own number or use random?(enter 1 to write your own number and enter 2 to add random number)")
  counter = -25
  while counter != 1 or counter != 2:
    counter = int(input())
    if counter == 1:
      break
    if counter == 2:
      break
    else:
      print("Incorrect input, try again.")
  if counter == 1:
    numbr = int(input("Enter your number: "))
    print("Do you want to make space between your nickname and number?")
    inchoice(inch)
    if choice == True:
      nickname = nickname + " " + str(numbr)
    if choice == False:
      nickname = nickname + str(numbr)
  if counter == 2:
    print("How many digits will be in your number? (choose from one to five)")
    hmd = int(input())
    if hmd == 1:
      numbr = random.randint(0,9)
    if hmd == 2:
      numbr = random.randint(10,99)
    if hmd == 3:
      numbr = random.randint(100,999)
    if hmd == 4:
      numbr = random.randint(1000,9999)
    if hmd == 5:
      numbr = random.randint(10000,99999)
    print("Do u want to make a space between your nickname and number?")
    inchoice(inch)
    if choice == True:
      nickname = nickname + " " + str(numbr)
    if choice == False:
      nickname = nickname + str(numbr)
#space replaces
print("Do u want to replace all spaces on '._.' or '_'?")
inchoice(inch)
if choice == True:
  print("What do u wanna use to replace, '._.' or '_' ? Enter 1 to replace all spaces on '._.' or enter 2 to replace all spaces on '_' .")
  counter = int(input())
  if counter == 1:
    nickname = nickname.replace(" ","._.")
  if counter == 2:
    nickname = nickname.replace(" ","_")
time.sleep(0.38)
#end of the program and result
print("Generating your nickname...")
time.sleep(2)
print(f"Your nickname: {nickname}")