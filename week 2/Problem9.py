import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text",type=str)
parser.add_argument("start_index",type=int)
parser.add_argument("end_index",type=int)
args=parser.parse_args()

t=args

print("The given text: ", t.text)
print("Start index: ", t.start_index)
print("End index: ", t.end_index)

print("Output string: ", t.text[t.start_index:t.end_index])