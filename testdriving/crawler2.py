from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv 

base_url = "http://olympus.realpython.org"

html_page = urlopen(base_url + "/profiles")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")

for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)



with open('products.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)

for link in links:
    writer.writerow([link_url])
# writer.writerow(link_url.values()) #doesn't like values for strings

    