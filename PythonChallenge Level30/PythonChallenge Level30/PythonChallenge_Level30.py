import re
from PIL import Image

f = open("e:\\yankeedoodle.csv","rb")
data = re.findall(r'(0.\d*)',f.read()) 
img = Image.new('F',(53,139))
img.putdata(map(float,data))
img = img.transpose(Image.ROTATE_90)
img = img.transpose(Image.FLIP_TOP_BOTTOM)

s = [chr(int(data[i][5]+data[i+1][5]+data[i+2][6])) for i in xrange(0,len(data)-2,3)]
img.save('e:\\ans.tiff')
print ''.join(s)



