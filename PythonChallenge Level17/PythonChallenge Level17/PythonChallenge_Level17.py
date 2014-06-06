import requests,bz2,urllib

num = "12345"
bz2code = ""
while True:
    try:
        path = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s" % num
        url = requests.get(path)
        string = url.text 
        i = 0
        for i in xrange(len(string)-1,0,-1):
            if not string[i].isalnum():
                break
        num = string[i+1:] 
        bz2code += url.cookies['info']
        print string
        print bz2code
        print num
    except KeyError,e:
        break

bz2.decompress(urllib.unquote_plus(bz2code))
