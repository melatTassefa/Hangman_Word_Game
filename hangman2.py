import random
word_library = ['python', 'science', 'code', 'algorithm']
def hangman():
    ch = input("This is the hangman Game. Insert 1 if you want to proceed.\n ")
    if ch == '1':
        word = random.choice(word_library)
        print("We have got a word for you. The word has ", len(word), "letters. Please start guessing! You have 10 tries")
        i=1
        answer = [0] * len(word)
        for x in range(10):
            guess = input("Enter guess: ")
            for z in word:
                if guess == z:
                    ind = word.index(z)
                    answer[ind] = z
                    print("You got the", ind+1, " letter!")
                    break
            answerstr = ''.join([str(item) for item in answer])
            if answerstr == word:
                break
        answerstr = ''.join([str(item) for item in answer])
        if answerstr == word:
            print("Won! Word is: ", word)
        else:
            print("Try again")

hangman()


