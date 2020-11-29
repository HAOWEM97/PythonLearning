data = input('input a data: ')
try:
    istr = int(data)
except:
    istr = -1

if istr > 0 :
    print('Nice work')
else:
    print('Not a number')
