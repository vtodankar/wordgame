import os
import csv
import random
import flask



words = []
position = 0
word_size = 9

word_list="conundrum.txt"

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

#return json object with answer and conundrum
def getConundrum():
    r_index = int(random.random()*len(words))
    answer = str(words[r_index][0])
    conundrum = ''.join(random.sample(answer, word_size))
    return flask.jsonify(answer=answer, conundrum=conundrum)

def get_filecontents(filename):
    with open(filename, 'r') as f:
        return f.read()


#start rest flask service here
def main():
    app = flask.Flask(__name__)
    load_words()
    
    @app.route('/')
    def index():
        return get_filecontents('index.html')

    @app.route('/conundrum')
    def conundrum():
        return getConundrum()
    
    app.run(host='localhost', port=4000)

if __name__ == '__main__':
    main()
    
