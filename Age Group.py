age = int(input("Enter your age: "))
if age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")