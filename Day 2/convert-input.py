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
