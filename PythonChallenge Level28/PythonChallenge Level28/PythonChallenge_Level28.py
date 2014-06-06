from PIL import Image

img = Image.open("e:\\bell.png")
img.load
r,g,b = img.split()

glist = list(g.getdata())
glist_new = [(glist[i]-glist[i-1]) for i in xrange(1,len(glist),2)]
s = ''
for i in glist_new:
    if abs(i) != 42:
        s += chr(abs(i))
print s
 

