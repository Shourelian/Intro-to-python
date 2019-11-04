import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type= str)
parser.add_argument("first_word", type= str)
parser.add_argument("second_word", type= str)

args = parser.parse_args()

print ("enter a text: ",args.text)
print ("type a word from the text: ", args.first_word)
print ("type a new word", args.second_word)

args.first_word = args.second_word
args.text.replace(args.first_word, "%s")

print(args.text % (args.first_word, args.second_word))
