from PIL import Image

im = Image.open("e:\\cave.jpg")
ans = Image.new(im.mode,(320,240))
w,h = im.size
pix = im.load()
ans1 = ans.load()

for i in xrange(w):
    for j in xrange(h):
        if i % 2 == 1 and j % 2 == 1: 
            ans1[i // 2, j // 2] = pix[i,j]
        
ans.save("e:\\ans.jpg")



