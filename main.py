# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# lower the alphabhet
first_name = name1.lower()
second_name = name2.lower()

# print(first_name)
# print(second_name)

# count TRUE for first_name
t1 = first_name.count("t")
r1 = first_name.count("r")
u1 = first_name.count("u")
e1 = first_name.count("e")

t2 = second_name.count("t")
r2 = second_name.count("r")
u2 = second_name.count("u")
e2 = second_name.count("e")
true = t1+r1+u1+e1+t2+r2+u2+e2
print(f"The total of true : {true}")

# count LOVE for second_name
l1 = first_name.count("l")
o1 = first_name.count("o")
v1 = first_name.count("v")
e1 = first_name.count("e")

l2 = second_name.count("l")
o2 = second_name.count("o")
v2 = second_name.count("v")
e2 = second_name.count("e")
love = l1+o1+v1+e1+l2+o2+v2+e2
print(f"The total of love : {love}")

# Concat
tl = str(true) + str(love)

#convert
true_love = int(tl)

if true_love < 10 or true_love > 90 :
  print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and  true_love <= 50:
  print(f"Your score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}.")