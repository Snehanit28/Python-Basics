name ="Tony Stark"
print(name.upper())
print(name.lower())
print(name.find('S'))
print(name.find('s'))
print(name.find('z'))
print(name.find('a'))
print(name.find(' '))

print(name.replace('Tony Stark', 'Ironman'))
print(name.replace('Stark', 'Ironman'))
print(name.replace('T', 'I'))
print(name.replace(' ', ''))

print('m' in name) #False
print('S' in name) #True
print('Tony' in name) #True