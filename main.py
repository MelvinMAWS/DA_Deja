import requests
import scrape
from scrapy.crawler import CrawlerProcess


url = "http://www.wikipedia.org" # html url
url2 = "http://httpbin.org/headers" # header url

r = requests.get(url)  # get request on given site
if r.status_code == 200:
    print("Return Status: OK")
else:
    print("Return Status: FAILED")

h = requests.head(url)  # display website header
print("\nHeader:")
print("**********")
for i in h.headers:
    print("\t", i, ":", h.headers[i])
print("**********\n")

headers = {"User-Agent": "Mobile"}

rh = requests.get(url2, headers=headers)
print("\nModified Header user-agent:")
print("**********")
print(rh.text)
print("**********\n")

process = CrawlerProcess(settings={
    "FEEDS": {
        "imagelinks.json": {"format": "json"},
    },
})
process.crawl(scrape.NewSpider)
process.start()

print("\nList of Image Links:")
with open("./imagelinks.json", 'r') as f:
    print(f.read())



