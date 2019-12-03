f = open("input.txt", 'r')
line = f.readline()
words = line.split()
print(type(words[0]))
print(int(words[0]) + int(words[1]))
f.close()

while 1:
    data = input()
    if not data: break
    print(data)