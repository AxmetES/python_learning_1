# Problem 1
# Use map() to create a function which finds the length of each word in the phrase (broken by spaces) and returns the values in a list.
#
# The function will have an input of a string, and output a list of integers.


def word_lengths(phrase):
    return len(phrase)


phrase = 'How long are the words in this phrase'
list_word_len = list(map(word_lengths, phrase.split()))

print(list_word_len)
