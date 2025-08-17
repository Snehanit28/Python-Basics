age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("You are an adult.")
    print("You can vote.")
elif age < 18 and age > 3:
    print("You are a minor.")
    print("You cannot vote.")
else:
    print("You are a child.")
    print("You cannot vote.")


numbers = range(5) #0,1,2,3,4
print(numbers)

# While loop example

i = 1
while i <= 50:
    print(i)
    i+=1

for item in range(5):
    print(item+1)