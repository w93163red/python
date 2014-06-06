from PIL import Image,ImageDraw

def find(a):
    x = a // img.size[1]
    y = a % img.size[1]
    return [x,y]

img = Image.open('e:\\maze.png')
new = Image.new('RGBA',img.size,'black')
newimg = ImageDraw.Draw(new)  

for i in range(img.size[1]):  
    if img.getpixel((i,0))[0]==0:  
        pos = (i,0)  
    if img.getpixel((i,img.size[0]-1))[0]==0:  
        endpos = (i,img.size[0]-1)   

d = [(1,0),(-1,0),(0,1),(0,-1)]
prev = [0]*(img.size[0]*img.size[1])
way = []
queue = [list(pos)]
string = ""
wall = (255,255,255,255)

print "Stage I..."
while queue != []:
    current = queue.pop()
    for i in d:
        x = current[0]+i[0]
        y = current[1]+i[1]
        if tuple([x,y]) == pos:
            break
        try:
            if prev[x*img.size[1]+y] == 0 and img.getpixel((x,y)) != wall:
                queue.append([x,y])
                prev[x*img.size[1]+y] = current[0]*img.size[1]+current[1]
        except:
            pass

tpos = list(endpos)

print "Stage II..."
while prev[tpos[0]*img.size[1]+tpos[1]] != 0:
    r,g,b,a = img.getpixel(tuple(tpos))
    string += chr(r)
    tpos = find(prev[tpos[0]*img.size[1]+tpos[1]])
    newimg.point(tpos)
print "Stage III..."
string = string[::-1]
string1 = string[0::2]
out = open('e:\\ans.zip','wb')
out.write(string1)  
out.close()