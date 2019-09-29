# Use filter to return the words from a list
# of words which start with a target
# letter.
def filter_words(word_list, letter):
    list_words_by_letter = list(filter(lambda x: x if x.startswith(letter) else None, word_list))
    return list_words_by_letter


l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
print(filter_words(l, 'h'))

# ['hello', 'ham', 'hi', 'heart']
