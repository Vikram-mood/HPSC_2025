x=10000.0
s=1.0
kmax=100
tol=1.0e-14
for i in range(kmax):
	s0=s
	print(f"At interation{i} the value of s={s}")
	s=0.5*(s+x/s)
	if(abs(s-s0)/x<tol):
		break

print(f"finally, the value of s={s}")



