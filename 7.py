s=input()
k=0
while len(s)>0:
	if s.find(' ')>0:
		s=s[s.find(' '):]
		k=k+1
	if s.find(' ')==0:
		s=s[1:]
	
print(k)
