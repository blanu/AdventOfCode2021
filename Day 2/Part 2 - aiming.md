# Python Solution

Adding some complexity to the solution:
- provide an input file instead of hardcoded input so we can switch between test cases.
- Make a class to track state variables

You could do this with array programming or recursion, but once you have multiple mutating state variables to track then it's cleaner to make a data structure such as a class rather than having a bunch of variables.

		import sys

		f = open(sys.argv[1])
		lines = f.readlines()
		f.close()
		lines2 = [line.strip() for line in lines if line != '']
		dirs = [line for line in map(lambda line: line.split(' '), lines2)]
		print(dirs)

		class Submarine:
		  def __init__(self):
			self.horiz = 0
			self.depth = 0
			self.aim = 0

		  def compute(self, d):
			(direction, value) = d
			if direction == 'forward':
			  self.horiz = self.horiz + int(value)
			  self.depth = self.depth + (self.aim * int(value))
			elif direction == 'down':
			  self.aim = self.aim + int(value)
			elif direction == 'up':
			  self.aim = self.aim - int(value)

		sub=Submarine()
		for dir in dirs:
		  sub.compute(dir)

		print(sub.horiz * sub.depth)
	
		900
		
		