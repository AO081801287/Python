fh=open('sample.txt')
#fh=input('enter the data')
lines = [line.split(' ') for line in fh]
output = open("sample(sorted).txt", 'w')
for line in sorted(lines[0]):
    output.write(' '.join(line))
output.close()
