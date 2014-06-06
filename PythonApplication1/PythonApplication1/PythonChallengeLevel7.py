from PIL import Image
pic = Image.open("e:\oxygen.png","r")
ans = []
for x in xrange(0,629,7):
    (r,g,b,a) = pic.getpixel((x,46))
    if r == g == b and a == 255:
         ans.append(r)
string = ""
print ans
for i in xrange(len(ans)):
    string += chr(ans[i])
print string
lst = [105, 110, 116, 101, 103, 114, 105, 116, 121]
str1 = ""
for i in xrange(len(lst)):
    str1 += chr(lst[i])
print str1

