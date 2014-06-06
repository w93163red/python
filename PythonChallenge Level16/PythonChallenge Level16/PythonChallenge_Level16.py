from PIL import Image

img = Image.open("e:\\mozart.gif")
w,h = img.size

for i in xrange(h):
    line = [img.getpixel((j,i)) for j in xrange(w-1)]
    pink = line.index(195)
    line = line[pink:] + line[:pink]
    for j,pix in enumerate(line):
        img.putpixel((j,i),pix)

img.save("e:\\ans.gif")


