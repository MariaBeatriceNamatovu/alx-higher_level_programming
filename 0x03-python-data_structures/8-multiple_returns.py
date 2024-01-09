#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    print(len(sentence))
    print(sentence[0])


sentence = "At school, I learnt C!"
length = len(sentence)
first = sentence[0]
print("Length: {:d} - First character: {}".format(length, first))
