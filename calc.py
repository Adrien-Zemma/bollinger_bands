def readfile(name, index, period):
	file = open(name, 'r')
	lines = []
	if file is None:
		return None
	for line in file:
		if line is not "":
			lines.append(float(line.replace('\n', '')))
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