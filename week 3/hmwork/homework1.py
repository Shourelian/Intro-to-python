a = [1, 4, 5, 7, 8, -2, 0, -1]  #1
print(a[3],a[5])   #2

a_sorted=a.copy()  #3
a_sorted.sort(reverse = True)
#print(a) #a is not changed
print(a_sorted)

print(a_sorted[1:4],a_sorted[2:7])  #4

del a_sorted [2:4]  #5
print(a_sorted)  #6

b = ["grapes","Potatoes","tomatoes","Orange","Lemon","Broccoli","Carrot","Sausages"]  #7

b_sorted=b.copy()  #8
b_sorted.sort()
print(b)
print(b_sorted)

c = a[1:4]+b[4:7]  #9

print(c)  #10