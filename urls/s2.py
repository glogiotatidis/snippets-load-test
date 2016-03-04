import sys

with open(sys.argv[1]) as f:
    LINES = f.read().splitlines()

urls = []
for line in LINES:
    weight, url = line.split()
    urls += [url for i in range(int(weight))]
print len(urls)
