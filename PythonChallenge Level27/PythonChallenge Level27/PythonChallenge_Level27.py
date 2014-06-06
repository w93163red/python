from PIL import Image
import string,bz2,keyword

zigzag = Image.open('e:\\zigzag.gif')
zig = zigzag.tostring()
fp = zigzag.palette.getdata()[1][::3]
trans = string.maketrans(''.join([chr(i) for i in xrange(256)]),fp)
ftrans = zig.translate(trans)

diff = ['','']
img = Image.new('1',zigzag.size,0)  
for i in xrange(1,len(zig)):
    if zig[i] != ftrans[i-1]:
        diff[0] += zig[i]
        diff[1] += ftrans[i-1]
        img.putpixel(((i-1) % zigzag.size[0], (i-1) / zigzag.size[0]),1)
        #img.putpixel(tuple(divmod(zigzag.size[0],i-1)),1)

img.save('e:\\ans.png')
text = bz2.decompress(diff[0])
ans = ''
for i in text.split():
    if not keyword.iskeyword(i):
        ans += i + ' '
print ans





