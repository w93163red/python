import requests

url = "http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg"

headers = {'Range':'bytes=1152983631-1153223363'}
r = requests.post(url,headers = headers)
open("e:\\ans.zip","wb").write(r.content)