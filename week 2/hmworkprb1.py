import argparse
import datetime
import time
import dateutil


parser = argparse.ArgumentParser()

parser.add_argument("--num_y", type= int)
parser.add_argument("--num_d", type= int)

args = parser.parse_args()

tdy= datetime.datetime.today()
tdeltaday= datetime.timedelta(days=0)
tdeltasec= datetime.timedelta(seconds=0)

tdeltaday_new= tdeltaday + args.num_y
tdeltasec_new= tdeltasec + args.num_y

x=tdeltaday_new + tdeltasec_new

print("Current date : ", tdy)
if args.num_y:    
    print("Given years :", args.num_y)
if args.num_d:
    print("Given days :", args.num_d)

print("Final date :", tdy + x )