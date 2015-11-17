s=input()
print(s[2],s[-2],s[0:5],s[:-2],s[::2],s[1::2],s[::-1],s[::-2],len(s),sep='\n')
print(input().count(' ')+1)
s=input()
print(s[0:s.find('h')+1],s[s.find('h')+1:s.rfind('h')].replace('h','H'),s[s.rfind('h'):], sep='')


