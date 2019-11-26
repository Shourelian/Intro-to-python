a1 = ["Cookies", "Chocolate", 8, True, -3, -5, "Chocolate", 8, False, 8]  #1

b1 = [8, True, 10, 14, "Chocolate", "Milk", "Jelly", True, False, True]  #2

set_a = set(a1)  #3
set_b = set(b1)  #4

union_ab = set_a.union(set_b)  #5

intersection_ab = set_a.intersection(set_b)  #6

union_ab.add("Kit Kat")  #7
union_ab.add("Oreo")
print(union_ab)

new_set = union_ab | intersection_ab  #8
print(new_set)

print("chocolate" in new_set)

new_set.remove("Oreo")
print(new_set)