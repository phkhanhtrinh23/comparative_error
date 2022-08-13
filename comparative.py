import re
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from pattern.en import comparative

class ComparativeError:
    def __init__(self):
        self.wnl = WordNetLemmatizer()

    # Regular expression
    def preprocess(self, text):
        text = text.split(' ')
        return text

    def run(self, sentence):
        new_string = ""
        tokens = self.preprocess(sentence)
        for i in range(len(tokens)-1,-1,-1):
            flag = False
            if tokens[i] == 'than':
                pos = i
                while pos >= 0:
                    real_token = self.wnl.lemmatize(tokens[pos], 'a')
                    for s in wn.synsets(real_token):
                        # Check if this word is an ADJECTIVE(a) or ADJECTIVE SATELLITE(s)
                        if s.name().split('.')[0] == real_token and s.pos() in ['a','s']: 
                            flag = True
                            tmp = comparative(real_token) # Convert to comparative form
                            if tokens[pos-1] == 'more':
                                if tokens[pos-1] + ' ' + tokens[pos] != tmp:
                                    tokens[pos-1] = ''
                                    tokens[pos] = tmp
                            elif tokens[pos] != tmp:
                                tokens[pos] = tmp
                            break
                    if flag == True:
                        break
                    pos -= 1
            if i == len(tokens)-1:
                new_string = tokens[i]
            else:
                new_string = tokens[i] + " " + new_string if tokens[i] != '' else new_string
        return new_string