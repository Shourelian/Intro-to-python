name = "Batman"
age = 15
password = "lalasasa23"

if name == "Batman":
    print("welcome Mr. %s!" % name)
if age < 16:
    print("Dear %s, you are too young to register" % name)
if "*" not in password and "&" not in password:
    print("Please enter a different password")