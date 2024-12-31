import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

url = "https://www.catholic.org/bible/book.php?id=1"
page = urlopen(url)
html = page.read().decode("utf-8")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# title_index = html.find("<title>")
# start_index = title_index + len("<title>") #gets rid if the title tag's text, i.e., literally "<title>"
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)

content_index = html.find('<p><a name="1"></a><sup>1</sup>')
content_start_index = content_index + len('<p><a name="1"></a><sup>1</sup>') #gets rid if the title tag's text, i.e., literally "<title>"
content_end_index = html.find('</p><div id="pager-Chapter">')
content = html[content_start_index:content_end_index]
print(content)

with open('products.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
writer.writerow(content.values())



# Find all anchor tags
#anchors = soup.find_all('a')
#for anchor in anchors:
#    # Check if the anchor has a name attribute
#    if 'name' in anchor.attrs:
#        name = anchor.attrs['name']
#        print(name)