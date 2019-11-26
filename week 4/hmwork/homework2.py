d = {"name": "Armen", "age": 15, "grades": [10, 8, 8, 4, 6, 7] }  #2

avg_grades=sum(d["grades"])/len(d["grades"])
if avg_grades>7:
    print("good job")
else:
    print("Yoo need to work more")