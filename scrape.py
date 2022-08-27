import scrapy

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["https://cdn.discordapp.com/attachments/701392074007904316/1009632871163629668/Python.html"]

    def parse(self, response):
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
