import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://en.wikipedia.org/wiki/Paris']

    def parse(self, response):
        clean_urls = []
        raw_urls = response.css('.image img::attr(src)').getall()
        for urls in raw_urls:
            clean_urls.append(response.urljoin(urls))

            yield {
                'image_urls': clean_urls
            }
