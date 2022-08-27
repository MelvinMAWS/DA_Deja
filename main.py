import unittest
import requests
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.response import open_in_browser

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
print("\nModified Header User-agent:")
print("**********")
print(rh.text)
print("**********\n")


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["https://cdn.discordapp.com/attachments/701392074007904316/1009632871163629668/Python.html"]

    def parse(self, response):
        open_in_browser(response)
        with open('./referencewebpage.json', 'wb') as f:
            f.write(response.body)
        css_selector = "img"
        f = open("./imagelinks.json", 'w').close()
        for x in response.css(css_selector):
            newsel = "@src"
            yield {
                "Image Link": x.xpath(newsel).extract_first(),
            }

            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback = self.parse
                )


process = CrawlerProcess(settings={
    "FEEDS": {
        "imagelinks.json": {"format": "json"},
    },
})
process.crawl(NewSpider)
process.start()

print("\nList of Image Links:")
with open("./imagelinks.json", 'r') as f:
    print(f.read())
class TestProgram(unittest.TestCase):
    def testStatusCode(self):

        self.assertEqual(r.status_code, 200) #test if status code is 200

if __name__ == '__main__':
    unittest.main()


