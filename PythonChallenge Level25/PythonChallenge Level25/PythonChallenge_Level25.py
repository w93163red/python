import requests,wave
from PIL import Image

for i in xrange(1,26):
    url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/lake%s.wav' % i
    r = requests.get(url)
    open("e:\\lake%s.wav" % i,"wb").write(r.content)

img = []

for i in xrange(1,26):
    wav = wave.open('e:\\lake%s.wav' % i,'rb')
    img.append(wav.readframes(wav.getnframes()))
    wav.close()

image = Image.new('RGB',(300,300))

for i in xrange(25):
    y,x = divmod(i,5)
    image.paste(Image.fromstring('RGB',(60,60),img[i]),(60*x,60*y))

image.save("e:\\ans.jpg")
