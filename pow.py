def is_pow(a,b):
	if a%b==0 and is_pow(a/b,b):
		return True
	elif a/b==b:
		return True
	else:
		return False
a=raw_input("ENTER a")
b=raw_input("ENTER b")
print is_pow(a,b)
		
