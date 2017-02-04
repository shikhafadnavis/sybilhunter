import xml.etree.ElementTree as ET
import string
import random

def randfingerprint(size=10, chars=string.ascii_lowercase+string.digits):
	return ''.join(random.choice(chars) for _ in range(10))
str1=""
tree=ET.parse("nodedetails1.xml")

root=tree.getroot()

f=open("nodedetails1.xml","w")
#child=ET.Element("fingerprint")
#root.append(child)

for elem in root:
	print elem
	smalllist=[]
	for elems in elem:
		
		smalllist.append(elems)
	x=len(smalllist)
	ET.SubElement(elem,'fingerprint')
	if elem[1].text=='1443':
		str1=randfingerprint()
		elem[x].text=str1
		print elem[x]
		
	else:
		elem[x].text=elem[x-1].text
	

ET.ElementTree(root).write(f)
f.close()
