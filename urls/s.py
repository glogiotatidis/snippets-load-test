import sys

with open(sys.argv[1]) as f:
    LINES = f.read().splitlines()

for line in LINES:
    occur, url = line.split()
    weight = int((int(occur)/10) + 0.5)
    print weight, url
