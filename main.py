from urllib.request import Request, urlopen

from bs4 import BeautifulSoup 

# test out beauitulsoup

url = "https://archiveofourown.org/works/53938930"
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urlopen(req, timeout=15).read().decode("utf8")
html[:60]

soup = BeautifulSoup(html, 'html.parser')
work_title = soup.select("h2.title.heading")

print(work_title)
print(work_title.string)