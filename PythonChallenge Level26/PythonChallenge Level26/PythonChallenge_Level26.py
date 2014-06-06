import md5,difflib

f = open('e:\\mybroken.zip','rb')
data = f.read()
new = ""

for i in xrange(len(data)):
    for j in xrange(256):
        new = data[:i] + chr(j) + data[i+1:]
        if md5.md5(new).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
           open('e:\\mybroken_fix.zip','wb').write(new)
           break
           


