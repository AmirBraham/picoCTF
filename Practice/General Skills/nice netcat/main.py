
with open("readme.md","r") as f:
	data = f.read()
	data = data.split("\n")
	res = ""	
	print(data)
	for n in data:
		print(n)
		if(n != ""):
			res += chr(int(float(n)))	
	print(res)	
