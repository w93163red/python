from PIL import Image,ImageDraw,ImageSequence

img = Image.open("e:\\white.gif")
new = Image.new('RGB',(200,200),'black') 
newimg = ImageDraw.Draw(new)
x = 0
y = 0
for s in ImageSequence.Iterator(img):
    a,b,c,d = img.getbbox()
    dx = a-100
    dy = b-100
    x += dx
    y += dy
    if dx==dy==0:
        x += 30
        y += 30
    newimg.point((x,y))

new.save("e:\\ans.png")
