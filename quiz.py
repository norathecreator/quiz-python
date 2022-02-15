score = 0

q_1 = "Who is the president of the united states?"
q_2 = "Which is the fastest penguin breed in the world?"
q_3 = "Which actor played Jimmy Hoffa in Martin Scorsese’s 2019 film The Irishman?"
q_4 = "What is the smallest planet in our solar system?"
q_5 = "What is the name of Kate Flannery's character in sitcom The Office?"

#Question 1
print(q_1)
answer = "b"
print("a: {}, b: {}, c: {}, or d: {}?: ".format("Barack Obama", "Donald Trump", "Hilary Clinton", "Joe Biden"))
guess = input("Type a/b/c/d to answer: ")
guess = guess.lower()
if guess == answer:
    correct = True
    score += 1
    print("Correct! ", "Current score: {}/5".format(score))
    print("\n")
else:
    correct = False
    print("Incorrect! ", "Current score: {}/5.".format(score))
    print("\n")

#Question 2
print(q_2)
answer = "d"
print("a: {}, b: {}, c: {}, or d: {}?: ".format("Emperor Penguin", "Rockhopper Penguin", "African Penguin", "Gentoo Penguin"))
guess = input("Type a/b/c/d to answer: ")
guess = guess.lower()
if guess == answer:
    correct = True
    score += 1
    print("Correct! ", "Current score: {}/5".format(score))
    print("\n")
else:
    correct = False
    print("Incorrect! ", "Current score: {}/5.".format(score))
    print("\n")

#Question 3
print(q_3)
answer = "a"
print("a: {}, b: {}, c: {}, or d: {}?: ".format("Al Pacino", "Joe Pesci", "Robert De Niro", "Danny DeVito"))
guess = input("Type a/b/c/d to answer: ")
guess = guess.lower()
if guess == answer:
    correct = True
    score += 1
    print("Correct! ", "Current score: {}/5".format(score))
    print("\n")
else:
    correct = False
    print("Incorrect! ", "Current score: {}/5.".format(score))
    print("\n")

#Question 4
print(q_4)
answer = "b"
print("a: {}, b: {}, c: {}, or d: {}?: ".format("Venus", "Mercury", "Jupiter", "Mars"))
guess = input("Type a/b/c/d to answer: ")
guess = guess.lower()
if guess == answer:
    correct = True
    score += 1
    print("Correct! ", "Current score: {}/5".format(score))
    print("\n")
else:
    correct = False
    print("Incorrect! ", "Current score: {}/5.".format(score))
    print("\n")

#Question 5
print(q_5)
answer = "c"
print("a: {}, b: {}, c: {}, or d: {}?: ".format("Pam", "Angela", "Meredith", "Phyllis"))
guess = input("Type a/b/c/d to answer: ")
guess = guess.lower()
if guess == answer:
    correct = True
    score += 1
    print("Correct! ", "Current score: {}/5".format(score))
    print("\n")
else:
    correct = False
    print("Incorrect! ", "Current score: {}/5.".format(score))
    print("\n")

if score < 5:
    print("THE END. Your score: {}/5. You'll get them all next time!".format(score))
elif score == 5:
    print("THE END. You scored 5/5. You're a quiz master!")