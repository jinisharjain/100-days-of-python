import random

def play_game(num, attempt, a, b, score):
    c = attempt
    i = 1
    for i in range(attempt):
        guess = int(input("Guess a number: "))
        if guess == num:
            print("You guessed correctly in ")
            score.append(i+1)
            print("Guessed in", i+1 , "attempt")
            return score
        elif guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
        print("Number of attempts left: ", (attempt - i - 1))
        print("Guess again")
    print("Attempts over")
    print("You lost")
    print("The number is : ", num)


def show_best_score(score):
    min = score[0]
    for i in range(1, len(score)):
        if score[i] < min:
            min  = score[i]
    print("Best score: ", min)

print("===== Number Guessing Game ======")
score = []
s2 = score
while True:
    print("1. Play Game")
    print("2. Show Best Score")
    print("3. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        while True:
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            ch = int(input("Choose a level: "))
            if ch == 1:
               num = random.randint(1,10)
               attempt =  5
               a = 1
               b = 10
            elif ch == 2:
               num = random.randint(1,50)
               a = 1
               b = 50
               attempt = 7
            elif ch == 3:
               num = random.randint(1,100)
               a = 1
               b = 100
               attempt = 10
            score = play_game(num, attempt, a, b, score)
            if score == s2:
                break
            else:
                s2 = score


    elif choice == 2:
        show_best_score(score)
    elif choice == 3:
        print("Thank you for playing")
        break

