import xml.etree.ElementTree as ET
import time


tree=ET.parse("nodedetails1.xml")

root=tree.getroot()

for elem in root:
	smalllist=[]
	for elems in elem:
		smalllist.append(elems)
	x=len(smalllist)
	
		
	if (elem[x-1].text!=elem[x-2].text):
		print ("Sybil detected: IP address:",elem[0].text)
		time.sleep(1)
	
