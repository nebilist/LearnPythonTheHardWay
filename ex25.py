def break_words(stuff):
    """This function will break up words for us(just like the function name says)."""
    words = stuff.split(' ')
    return words
    
def sort_words(words):
    """Sorts the words(duh)."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off(-facepalm-)."""
    word = words.pop(0)#I'm assuming that 0 means the first
    print word

def print_last_word(words):
    """Prints last word after popping it off(haha)."""
    #Oooh! Popping means separating.
    #When used, it is removed.
    word = words.pop(-1)#meaning last
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    #I'll assume that this sorts them alphabetically. I may be wrong.
    #It 'is'. But why did I come before A?
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence.(lol)"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    #the word sentence looks weird sometimes. Is it just me?
    print_first_word(words)
    print_last_word(words)
