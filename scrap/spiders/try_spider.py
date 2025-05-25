import scrapy


class QuotesSpider(scrapy.Spider):
    name = "title"
    start_urls = [
        "https://www.onlinekhabar.com",
        "https://www.daraz.com.np" 
    ]

    def parse(self, response):
        title = response.css('title::text').get()
        yield {
            'url': response.url,
            'title': title
        }