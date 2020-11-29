print('this project named Echo')
print('# will eat your voice')
print('Done will end this project')
while True :
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'Done':
        break
    print(line)
print('Done!')
