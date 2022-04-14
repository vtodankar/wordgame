import os
import csv
import random
from sys import breakpointhook


words = []
position = 0
word_size = 9
#word_list="words_alpha.txt"
word_list="norvig_100000.txt"

def load_words():
    words.clear()
    if os.access(word_list,os.F_OK):
        f = open(word_list)
        for row in csv.reader(f, delimiter='\t'):
            if len(row[position]) == word_size:
                words.append(row)
        f.close()

def show_words():
    index = 1
    for word in words:
        show_word(word, index)
        index = index + 1
    print()

def show_word(word, index):
    outputstr = "{0:>3}  {1:<200}  "
    print(outputstr.format(index, word[position]))

def show_quiz():
    r_index = int(random.random()*len(words))
    answer = str(words[r_index][0])


    print("Conundrum is : " + ''.join(random.sample(answer, word_size)))
    print("Enter your answer ")


    print("Enter your answer ")
    word = input("Answer  "+" : ")
    print(word)

    if(word == answer):
        print("answer is right ", answer)
    else:
        print("answer is wrong ", answer)

    
def menu_choice():
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   s) Show")
    print("   n) Set word size")
    print("   p) Play Conundrum")
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in ['s','q','p','n']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None

def main_loop():
    global word_size
    load_words()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == 's':
            show_words()
        elif choice == 'p':
            show_quiz()
        elif choice == 'n':
            print("Enter word length ")
            word_size = int(input())
            load_words()    
        else:
            print("Invalid choice.")

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()