import argparse

parse=argparse.ArgumentParser()
parse.add_argument("key",type=str)
parse.add_argument("value",type=int)
args = parse.parse_args()

dict1 = {'key1': "hello", 2: "bye" , "key3" : "John" }
print(dict1)

dict1[args.key]=args.value

print(dict1)
