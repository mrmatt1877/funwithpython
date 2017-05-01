import re
from collections import Counter

def spellCheck(word):
    
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

    #correctWord = 'abc'
    
    deletes = [L + R[1:] for L, R in splits if R]
   
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    
    inserts = [L + c + R for L, R in splits for c in letters]
    
    #WORDS = Counter(words(open('big.txt').read()))

    
    #def words(text): return re.findall(r'\w+', text.lower())
    
    
   # def P(word, N=sum(WORDS.values())): 
    #    "Probability of `word`."
     #   return WORDS[word] / N

    #max(candidates(word), key=P)
    
    
    
    
    possibleErrors = deletes + transposes + inserts + replaces
    print(possibleErrors)
    #for errors in possibleErrors:
    #    if word == correctWord:
    #        return word + " is spelt correct"
    #    if word == errors:
    #        return word + " should be spelt " + correctWord
    #    else:
    #        return "Did not find a match"
    

print(spellCheck("mississippi"))
#print(spellCheck("abgggefr"))
#print(spellCheck("abfc"))
#print(spellCheck("abfc"))