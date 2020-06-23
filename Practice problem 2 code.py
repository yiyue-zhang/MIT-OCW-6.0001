# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True

# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(is_word_guessed(secret_word, letters_guessed) )


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    L = []
    for char in secret_word:
        if char in letters_guessed:
            L.append(char)
        else:
            L.append('_ ')
    Guess = ''.join(L)
    return Guess

# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed) )


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    allword = string.ascii_lowercase
    L2 = []
    for char in allword:
        if char not in letters_guessed:
            L2.append(char)
    left = ''.join(L2)
    return left  

# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_available_letters(letters_guessed))

def get_unique_letter(secret_word):
    '''
    get the number of unique letters in secret word
    '''
    unique = []
    for char in secret_word:
        if char not in unique:
            unique.append(char)
    return len(unique)

# secret_word = 'facemask'
# print(get_unique_letter(secret_word))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    guesses_remain = 6
    warning_remain = 3
    vowel = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warning_remain, 'warnings left.')
    print('--------------------------------------------')
    print('You have', guesses_remain, 'guesses left.')
    print('Available letters:', string.ascii_lowercase)
    enter_letter = str.lower(input('Please guess a letter:'))
    
    while is_word_guessed(secret_word, letters_guessed) == False:
        if guesses_remain > 0:
            if str.isalpha(enter_letter) == True:
                if enter_letter in secret_word and enter_letter not in letters_guessed:
                    letters_guessed.append(enter_letter)
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                    print('--------------------------------------------')
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print('Congratulations, you won!')
                        print('Your total score for this game is:', guesses_remain * get_unique_letter(secret_word))
                        break
                    else:
                        print('You have', guesses_remain, 'guesses left.')
                        print('Available Letters:', get_available_letters(letters_guessed))
                        enter_letter = str.lower(input('Please guess a letter:'))
                elif enter_letter in letters_guessed:
                    warning_remain -= 1
                    if warning_remain >= 0:
                        print('Oops! You have already guessed that letter. You have', warning_remain, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                        print('--------------------------------------------')
                        print('You have', guesses_remain, 'guesses left.')
                        print('Available Letters:', get_available_letters(letters_guessed))
                        enter_letter = str.lower(input('Please guess a letter:'))
                    else:
                        guesses_remain -= 1
                        print('Oops! You have already guessed that letter. You have no warnings left, so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
                        print('--------------------------------------------')
                        if guesses_remain <= 0:
                            print('Sorry, you ran out of guesses.The word was', secret_word, '.')
                            break
                        else:
                            print('You have', guesses_remain, 'guesses left.')
                            print('Available Letters:', get_available_letters(letters_guessed))
                            enter_letter = str.lower(input('Please guess a letter:'))
                elif enter_letter not in secret_word and enter_letter in vowel:
                    guesses_remain -= 2
                    letters_guessed.append(enter_letter)
                    print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                    print('--------------------------------------------')
                    if guesses_remain <= 0:
                        print('Sorry, you ran out of guesses.The word was', secret_word, '.')
                        break
                    else:
                        print('You have', guesses_remain, 'guesses left.')
                        print('Available Letters:', get_available_letters(letters_guessed))
                        enter_letter = str.lower(input('Please guess a letter:'))
                elif enter_letter not in secret_word and enter_letter not in vowel:
                    guesses_remain -= 1
                    letters_guessed.append(enter_letter)
                    print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                    print('--------------------------------------------')
                    if guesses_remain <= 0:
                        print('Sorry, you ran out of guesses.The word was', secret_word, '.')
                        break
                    else:
                        print('You have', guesses_remain, 'guesses left.')
                        print('Available Letters:', get_available_letters(letters_guessed))
                        enter_letter = str.lower(input('Please guess a letter:'))
            elif warning_remain > 0:
                warning_remain -= 1
                print('Oops! That is not a valid letter. You have', warning_remain, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                print('--------------------------------------------')
                print('You have', guesses_remain, 'guesses left.')
                print('Available Letters:', get_available_letters(letters_guessed))
                enter_letter = str.lower(input('Please guess a letter:'))
            else:
                guesses_remain -= 1
                print('Oops! That is not a valid letter. You have no warnings left, so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
                print('--------------------------------------------')
                if guesses_remain <= 0:
                    print('Sorry, you ran out of guesses.The word was', secret_word, '.')
                    break
                else:
                    print('You have', guesses_remain, 'guesses left.')
                    print('Available Letters:', get_available_letters(letters_guessed))
                    enter_letter = str.lower(input('Please guess a letter:'))
    return


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    a = my_word.replace(' ', '')
    b = other_word.replace(' ', '')
    
    if len(a) != len(b):
        return False

    i = 0
    for char in a:
        if char != '_':
            if a.count(char) != b.count(char):
                return False
            if char != b[i]:
                return False
        i += 1
    
    return True

# print(match_with_gaps("te_ t", "tact"))
# print(match_with_gaps("a_ _ le", "banana"))
# print(match_with_gaps("a_ _ le", "apple"))
# print(match_with_gaps("a_ ple", "apple"))
   

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    L = []
    Match = False
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            L.append(word)
            Match = True
    
    if Match:
        matchlist = ' '.join(L)
        return print(matchlist)
    else:
        return print('No matches found')


# show_possible_matches("t_ _ t")
# show_possible_matches("abbbb_ ")
# show_possible_matches("a_ pl_ ")

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remain = 6
    warning_remain = 3
    vowel = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    okletter = ['*', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warning_remain, 'warnings left.')
    print('--------------------------------------------')
    print('You have', guesses_remain, 'guesses left.')
    print('Available letters:', string.ascii_lowercase)
    enter_letter = str.lower(input('Please guess a letter:'))
    
    while is_word_guessed(secret_word, letters_guessed) == False:
        if enter_letter == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            if guesses_remain > 0:
                if str.isalpha(enter_letter) == True:
                    if enter_letter in secret_word and enter_letter not in letters_guessed:
                        letters_guessed.append(enter_letter)
                        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                        print('--------------------------------------------')
                        if is_word_guessed(secret_word, letters_guessed) == True:
                            print('Congratulations, you won!')
                            print('Your total score for this game is:', guesses_remain * get_unique_letter(secret_word))
                            break
                        else:
                            print('You have', guesses_remain, 'guesses left.')
                            print('Available Letters:', get_available_letters(letters_guessed))
                            enter_letter = str.lower(input('Please guess a letter:'))
                    elif enter_letter in letters_guessed:
                        warning_remain -= 1
                        if warning_remain >= 0:
                            print('Oops! You have already guessed that letter. You have', warning_remain, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                            print('--------------------------------------------')
                            print('You have', guesses_remain, 'guesses left.')
                            print('Available Letters:', get_available_letters(letters_guessed))
                            enter_letter = str.lower(input('Please guess a letter:'))
                        else:
                            guesses_remain -= 1
                            print('Oops! You have already guessed that letter. You have no warnings left, so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
                            print('--------------------------------------------')
                            if guesses_remain <= 0:
                                print('Sorry, you ran out of guesses.The word was', secret_word, '.')
                                break
                            else:
                                print('You have', guesses_remain, 'guesses left.')
                                print('Available Letters:', get_available_letters(letters_guessed))
                                enter_letter = str.lower(input('Please guess a letter:'))
                    elif enter_letter not in secret_word and enter_letter in vowel:
                        guesses_remain -= 2
                        letters_guessed.append(enter_letter)
                        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                        print('--------------------------------------------')
                        if guesses_remain <= 0:
                            print('Sorry, you ran out of guesses.The word was', secret_word, '.')
                            break
                        else:
                            print('You have', guesses_remain, 'guesses left.')
                            print('Available Letters:', get_available_letters(letters_guessed))
                            enter_letter = str.lower(input('Please guess a letter:'))
                    elif enter_letter not in secret_word and enter_letter not in vowel:
                        guesses_remain -= 1
                        letters_guessed.append(enter_letter)
                        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                        print('--------------------------------------------')
                        if guesses_remain <= 0:
                            print('Sorry, you ran out of guesses.The word was', secret_word, '.')
                            break
                        else:
                            print('You have', guesses_remain, 'guesses left.')
                            print('Available Letters:', get_available_letters(letters_guessed))
                            enter_letter = str.lower(input('Please guess a letter:'))
                elif warning_remain > 0:
                    warning_remain -= 1
                    print('Oops! That is not a valid letter. You have', warning_remain, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                    print('--------------------------------------------')
                    print('You have', guesses_remain, 'guesses left.')
                    print('Available Letters:', get_available_letters(letters_guessed))
                    enter_letter = str.lower(input('Please guess a letter:'))
                else:
                    guesses_remain -= 1
                    print('Oops! That is not a valid letter. You have no warnings left, so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
                    print('--------------------------------------------')
                    if guesses_remain <= 0:
                        print('Sorry, you ran out of guesses.The word was', secret_word, '.')
                        break
                    else:
                        print('You have', guesses_remain, 'guesses left.')
                        print('Available Letters:', get_available_letters(letters_guessed))
                        enter_letter = str.lower(input('Please guess a letter:'))
    return



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
