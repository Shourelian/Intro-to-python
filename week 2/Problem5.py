import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text",type=str)
args=parser.parse_args()

t = args.text

print("the given string",t)
print("all upper case",t.upper())
print("all lower case",t.upper())