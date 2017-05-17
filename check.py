def check_fermat(a,b,c,n):
	if n<=2:
		print "No, that doesn't work"
		return
	else :
		sums=(a**n)+(b**n)
		if sums==(c**n):
			print 'Holy smokes, Fermat was wrong!'
			return
		print n
		check_fermat(a,b,c,n-1)
a=int(raw_input("enter value for a\n"))
b=int(raw_input("enter value for b\n"))
c=int(raw_input("enter value for c\n"))
n=int(raw_input("enter value for n\n"))
check_fermat(a,b,c,n)
