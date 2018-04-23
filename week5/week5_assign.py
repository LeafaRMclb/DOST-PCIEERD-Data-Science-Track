import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter url: ")
print("Retrieving: ", url)
data = urllib.request.urlopen(url).read()
print("Retrieved: ", len(data), "characters")
tree = ET.fromstring(data)
counts = tree.findall(".//count")
print("Count: ", len(counts))
counts_list = []
for count in counts:
    counts_list.append(count.text)

print(sum([int(i) for i in counts_list]))














































