
import xml.etree.ElementTree as ET

def levenshtein_distance(first, second):
    """Find the Levenshtein distance between two strings."""
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length):
       distance_matrix[i][0] = i
    for j in range(second_length):
       distance_matrix[0][j]=j
    for i in xrange(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length-1][second_length-1]

tree=ET.parse("nodedetails1.xml")
root=tree.getroot()

list1=['208.16.7.9','80','55']
biglist=[]
#list2=[['201.15.7.9','8080','80'],['241.15.63.7','1234','90'],['208.16.7.8','5454','100'],['201.15.7.9','6443','75'],['176.34.54.70','5432','65'],['123.73.65.92','4432','78'],['208.16.8.10','8032','90'],['192.23.71.165','4423','85'],['192.23.72.165','447','85']]
for child in root:
	smalllist=[]
	smalllist.append(child[0].text)
	smalllist.append(child[1].text)
	smalllist.append(child[2].text)
	biglist.append(smalllist)

str1=""
str2=""

for elem in list1:
	str1+=str(elem)
i=0
while (i<10):
	for elem in biglist[i]:
		str2+=str(elem)
	print ("Levenshtein distance between seed node and node",(i+1),":",levenshtein_distance(str1,str2))
	i+=1
	str2=""
			

