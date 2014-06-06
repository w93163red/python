import difflib,gzip

zip = gzip.open("e:\\deltas.gz").readlines()
left, right = [], []
png = [[], [], []]

for line in zip:
    left.append(line[0:53])
    right.append(line[56:-1])


diff = difflib.ndiff(left,right)

for line in list(diff):
    
    if line[0] == '?':
        continue
    line_t = [chr(int(j, 16)) for j in line[2:].split()] 
    if line[0] == '+':
        png[0].extend(line_t)
    elif line[0] == '-':
        png[1].extend(line_t)
    else:
        png[2].extend(line_t) 
    


for i in xrange(3):
    open("e:\\%d.png" % i,"wb").write(''.join(png[i]))


    

