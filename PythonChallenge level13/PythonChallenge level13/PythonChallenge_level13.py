import xmlrpclib

url = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print url.system.listMethods()
print url.system.methodHelp("phone")
print url.phone("Bert")

