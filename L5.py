marks = [90, 83, 95, "math"]
print(marks)
print(marks[0])
print(marks[2])
print(marks[-1])       # Last element
print(marks[-2])       # Second last element
print(marks[-3])       # First element
print(marks[0:2])      # First two elements
print(marks[1:])       # From second element to the end
print(marks[:2])       # From start to second element
print(marks[1:3])      # From second to third element

for score in marks:
    print(score) 

marks.append(88)       # Add a new element
print(marks)

marks.insert(1, 85)   # Insert at index 1
print(marks)

marks.remove(83)      # Remove the first occurrence of 83
print(marks)

print(len(marks))     # Length of the list

marks.pop()           # Remove the last element
print(marks)

i=0
while i < len(marks):
    print(marks[i])
    i += 1

marks.clear()          # Clear the list
print(marks)