def sqrt2(x,debug=False):
	s=1.0
	kmax=100
	tol=1.0e-14
	for i in range(kmax):
		s0=s
		if(debug):
			print(f"At interation{i} the value of s={s:20.15f}")
		s=0.5*(s+x/s)
		if(abs(s-s0)/x<tol):
			break
	if(debug):
		print(f"finally, the value of s={s:20.15f}")
	return s




