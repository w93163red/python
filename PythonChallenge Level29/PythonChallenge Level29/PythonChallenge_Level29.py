import requests,bz2

url = 'http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html'
r = requests.get(url)
string = r.content
string_lines = string.split('\n')
string_lines = string_lines[12:]
ans = ''
for i in string_lines:
    ans += chr(len(i))

print bz2.decompress(ans)
