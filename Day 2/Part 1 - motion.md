# Input
	forward 5
	down 5
	forward 8
	up 3
	down 8
	forward 2
	
# Converting to vectors
	f = open('input.txt')
	lines = f.readlines()
	f.close()
	lines2 = [line.strip() for line in lines if line != '']
	dirs = [line for line in map(lambda line: line.split(' '), lines2)]
	print(dirs)

	hs=[]
	ds=[]
	def convert(d):
	  (direction, value) = d
	  if direction == 'forward':
		hs.append(value)
	  elif direction == 'down':
		ds.append(value)
	  elif direction == 'up':
		ds.append('¯'+value)

	for dir in dirs:
	  convert(dir)

	print('hs ← ' + ' '.join(hs))
	print('ds ← ' + ' '.join(ds))
	
# Input Vectors
	hs ← 5 8 2
	ds ← 5 ¯3 8
	
# Addition Fold
		+/ hs
	15
		
		+/ ds
	10
	
# Multiply Parts
		(+/ds) × (+/hs)
	150
	
# Final Program
		hs ← 5 8 2
		ds ← 5 ¯3 8
		(+/ds) × (+/hs)
	150

# Answer
	150