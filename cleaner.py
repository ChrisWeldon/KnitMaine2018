import random

def valCount(lst):
	res = {}
	for i in range(len(lst)):
		if i+1 not in lst:
			res[i+1]=0
		try:
			res[lst[i]] += 1
		except KeyError:
			res[lst[i]] = 1
	#del res[0]

	return res

def findIndexofNum(num, vals, topdown):
	if num > len(vals):
		raise Exception("The end of the list has been reached")
	try:
		inds = []
		for i, v in enumerate(vals):
			if v == num:
				inds.append(i)
		if len(inds)>1:
			return random.choice(inds)
		else:
			return inds[0]
	except IndexError:
		if topdown:
			return findIndexofNum(num+1, vals, topdown)
		else:
			return findIndexofNum(num-1, vals, topdown)

def cleanList(list):
	vals = list
	print(vals)
	topdown = True
	while 0 in valCount(vals).values():
		valcount = valCount(vals)
		if topdown:
			for i in range(len(vals)):
				if(valcount[i+1]) == 0:
					try:
						vals[findIndexofNum(i+2, vals,topdown)] -=1
					except Exception:
						#print("setting topdown False")
						topdown = False
					break
		else:
			for i in range(len(vals)):
				j = len(vals)-(i+1)
				if(valcount[j+1]) == 0:
					try:
						vals[findIndexofNum(j, vals,topdown)] +=1
					except Exception:
						#print("setting topdown True")
						topdown = True
					break

		print(vals)
	return vals

def main():
	vals = [1,1,1,1,1,1,1,1,1,1]
	cleanList(vals)


if __name__ == "__main__":
	main()
