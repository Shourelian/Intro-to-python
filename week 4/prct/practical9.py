correct_num = 5

for i in range(0,10):
    guess = int(input("Guess the correct number: "))
    if guess == correct_num:
        print("That was a good guess!")
        break

    