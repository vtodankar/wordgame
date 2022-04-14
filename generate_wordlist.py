import os
import csv
import random
from sys import breakpointhook


words = []
position = 0
word_size = 9
#word_list="words_alpha.txt"
word_list="norvig_full.txt"
output_file="conundrum.txt"

def load_words():
    words.clear()
    if os.access(word_list,os.F_OK):
        f = open(word_list)
        for row in csv.reader(f, delimiter='\t'):
            if len(row[position]) == word_size:
                words.append(row)
        f.close()


# Save the words list to file
def save_words():
    f = open(output_file, 'w')
    for word in words:
        f.write(word[0] + '\t' + word[1] + '\n')
    f.close()


 
def main_loop():
    global word_size
    load_words()
    save_words()
    
 

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()