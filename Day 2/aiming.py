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

print(sub.horiz)
print(sub.depth)
print(sub.horiz * sub.depth)
