import os.path

def readfile(name, index, period):
	lines = []
	len_file = 0
	if not os.path.isfile(name):
		print('"{}"don''t exist'.format(name))
		return None
	with open(name, 'r') as file:
		for line in file:
			if line is not "":
				lines.append(float(line.replace('\n', '')))
				len_file += 1
		if not lines:
			return None
	if index > len_file or index < 0:
		print("Error index")
		return None
	lines = lines[:int(index) + 2]
	return lines[(-int(period) - 1):-1]

def moy(lines):
	moy = 0
	if len(lines) is 0:
		return None
	for nb in lines:
		moy += nb
	moy /= len(lines)
	return moy

def standard(lines):
    return variance(lines)**0.5

def variance(lines):
    moyen = moy(lines)
    return moy([(x-moyen)**2 for x in lines])