import os
import csv
import random
from sys import breakpointhook


words = []
position = 0
word_size = 5
word_list="10000_words.txt"

def load_words():
    words.clear()
    if os.access(word_list,os.F_OK):
        f = open(word_list)
        for row in csv.reader(f):
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

    
def menu_choice():
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   s) Show")
    print("   n) Set word size")
    print("   p) Play")
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in ['s','q','p','n']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None

def show_quiz():
    r_index = int(random.random()*len(words))
    answer = str(words[r_index][0])
   
    print("Enter your answer ")
    for i in range(0,word_size):
        while True:
            word = input("Word try number "+str(i+1)+" : ")
            if any(word in w for w in words):
                break
            else:
                print("Word not in list ")
       
        print(word)
        if(word == answer):
            print("answer is right ", answer)
            break
        else:
            for j in range(0,word_size):
                if(word[j]==answer[j]):
                    print("G", end ="")
                elif(word[j] in answer ):
                    print("Y", end ="")
                else:
                    print("N", end ="")
        print("")
    print("answer is ", answer)    


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