import base64,wave

music = open('e:\\music1.wav','wb')
file = open("e:\\a.txt","r")
string = file.read()
wav = base64.b64decode(string)
music.write(wav)
music.close()

music = wave.open('e:\\music1.wav','rb')
new_music = wave.open('e:\\music2.wav','wb')
params = music.getparams()
new_music.setparams(params)
for i in xrange(music.getnframes()):
    new_music.writeframes(music.readframes(1)[::-1])
new_music.close()

