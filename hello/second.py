# person = input("nationality? ").lower()

# if person == "french" or person == "francias":
#     name = input("comment tu t'appelle? ").title()
#     going_to_school = input("allez-vous a l'ecole? ")

#     if going_to_school == "yes":
#         print(f"bienvenue chez au univelcity, {name}.")
#     else:
#         print(f"Au revior, {name}. bonne journee.")

# elif person == "italian":
#     print("Preferisci parlare italiano.")
# else:
#     print("you are neither french nor italian.")
#     print("so let us speak english!")




# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))

import random as ofr

# name = [1, 2, 3, 6, 7]

# print(random.choice(name))

# my_list = [3,4,2,4,6,7,8]

# my_list[5]= 789

# print(my_list)

# num = list(range(50,7493))
# ofr.shuffle(num)

# print(min(num))
# print(max(num))

# print(sorted(num, reverse=True)[:5])

num = list(range(1,90))

ofr.shuffle(num)

print(num)
print("welcome player")

r = int(input("choose a number ="))
print("player chioce", r)

com_choice = ofr.choice(num)

print("computer choice", com_choice)

if r in num:
    if r == com_choice:
        print("great choice")


    if r > com_choice:
        print("Too high")

    if r > com_choice:
        print("Too low")

else:
    print("not found")


