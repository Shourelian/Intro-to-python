import argparse
parser = argparse.ArgumentParser()

parser.add_argument("text", type= str,help="type an odd number of characters")

args = parser.parse_args()

if len(args.text)%2!=0 and len(args.text) > 7 :
    
    x=middle_letter=len(args.text) / 2
    y=first_letter = int(middle_letter - 1)
    z=third_letter = int(middle_letter + 2)

    w=args.text[first_letter:third_letter]

    print("The old string: ", args.text)
    print("Middle 3 characters: ",w )
    print("The new string: ",args.text.replace(w,w.upper()))
else:
    print("enter a text which is 7 or more characters long and has an odd number of characters")
