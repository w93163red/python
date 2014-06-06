from PIL import Image, ImageDraw

lst = [[i, i-1, i-1, i-2] for i in xrange(100,0,-2)]
lst = reduce(lambda x,y:x+y, lst)

ori = Image.open("e:\\wire.png")
ori_load = ori.load()
ans = Image.new(ori.mode,(110,110))
ans_load = ans.load()

dir = [[0,1], [1,0], [0,-1], [-1,0]]
x = y = 0
count = 0

for index in xrange(len(lst)):
    t = index % 4
    for i in xrange(lst[index]):
        x += dir[t][0]
        y += dir[t][1]
        ans_load[x,y] = ori_load[count,0]
        count += 1

ans.save("e:\\ans.jpg")





