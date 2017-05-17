def gcd(a,b):
	if b==0 :
		return a
	else:
		return gcd(b,a%b)

a=int(raw_input("enter value for a\n"))
b=int(raw_input("enter value for b\n"))
print gcd(a,b)
