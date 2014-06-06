a = ["1","11","21","1211"]
b = ["1"]

for i in xrange(40):
    string = b[i]
    t = string[0]
    count = 0
    temp = ""
    for index in xrange(len(string)):
        if string[index] == t:
            count += 1
        else:
            temp += str(count)
            temp += t
            count = 1
            t = string[index]
    temp += str(count)
    temp += t
    b.append(temp)


print len(b[30])



