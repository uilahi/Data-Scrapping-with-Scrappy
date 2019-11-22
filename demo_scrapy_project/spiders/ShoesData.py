import scrapy


class QuotesSpider(scrapy.Spider):
    name = "shoes"

    def start_requests(self):
        url = 'https://www.alibaba.com/catalog/men%E2%80%99s-shoes_cid100001615?spm=a272h.12388681.jx1sipk2.2.5fca830boc3XHa'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            yield{
                'Quote : ':quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                'Author: ': quote.xpath(".//div[@class='quoteText']/span[@class='authorOrTitle']/text()").extract_first(),
                'Tags : ':quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract()

            }
















        # 'http://quotes.toscrape.com/page/2/',
        # 'http://quotes.toscrape.com/page/3/',
        # 'http://quotes.toscrape.com/page/4/'

        # def parse(self, response):
        #     page = response.url.split("/")[-2]
        #     filename = 'quotes-%s.html' % page
        #     with open(filename, 'wb') as f:
        #         f.write(response.body)
        #     self.log('Saved file' + page)