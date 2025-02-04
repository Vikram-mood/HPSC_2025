x=2.0
s=1.0

for i in range(10):
	print(f"At interation{i} the value of s={s}")
	s=0.5*(s+x/s)

print(f"finally, the value of s={s}")



