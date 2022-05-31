print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined = name1 + name2
lower_combined = combined.lower()

t = lower_combined.count("t")
r = lower_combined.count("r")
u = lower_combined.count("u")
e = lower_combined.count("e")

true = t + r + u + e

l = lower_combined.count("l")
o = lower_combined.count("o")
v = lower_combined.count("v")
e = lower_combined.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")