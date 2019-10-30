import argparse

parse=argparse.ArgumentParser()
parse.add_argument("name",type=str)
args = parse.parse_args()

print ("welcome,",args.name,"!")