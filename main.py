#regular expressions good for 
 
import re
pattern = re.compile(	
r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") #for email validation
string = 'b@b.com'


a = pattern.search(string)
b = pattern.findall(string) # gives instances of this 
c = pattern.fullmatch(string) #none it has to be the exact string. 
d = pattern.match(string) 
print(a)

r""