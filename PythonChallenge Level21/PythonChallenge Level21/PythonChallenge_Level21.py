
import zlib,bz2

package = open("e:\\ans\\package.pack","rb").read()
string = ""
while True:
    if package.startswith('x\x9c'):
        package = zlib.decompress(package)
        string += ' '
    elif package.startswith('BZh'):
        package = bz2.decompress(package)
        string += '#'
    elif package.endswith('\x9cx') or package.endswith('hZB'):
        package = package[::-1]
        string += '\n'
    else:
        break
print string
open('e:\\ans.txt',"wb").write(package)