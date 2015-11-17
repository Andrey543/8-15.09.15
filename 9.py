s=input()
n=int(input())
b=''
while s.find(' ')==0:
	s=s[1:]
while s.find(' ')==len(s)-1:
	s=s[:-1]
while len(s)>0:
	if s.find(' ')>=n:
		b=b+s[0:s.find(' ')]+' '	
	s=s[s.find(' '):]
	while s.find(' ')==0:
		s=s[1:]
	if s.find(' ')==-1:
		if len(s)>=n:
			b=b+s
		s=''
print(b)
	
