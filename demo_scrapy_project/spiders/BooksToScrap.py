import scrapy
from scrapy.loader import ItemLoader
from demo_scrapy_project.items import ItemsPYofBooks


class BooksToScrap(scrapy.Spider):
    # identity
    name = "books"
    start_url = "http://books.toscrape.com/catalogue/page-1.html"


    def start_requests(self):
        url = 'http://books.toscrape.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    def __init__(self):
        self.cnt = 1

    # start_url = "http://books.toscrape.com/index.html"

    def parse(self, response):
        # for book in response.selector.xpath('//article[@class="product_pod"]'):
        for book in response.selector.xpath('//li[@class ="col-xs-6 col-sm-4 col-md-3 col-lg-3"]'):
            # loader = ItemLoader(item=ItemsPYofBooks(), selector=book, response=response)
            #
            # loader.add_xpath('title ', ".//h3/a/text()[1]"),
            # loader.add_xpath('price ', ".//p[@class='price_color']/text()"),
            # loader.add_xpath('stock ', ".//p[@class='instock availability']/text()[2]")
            # yield loader.load_item()
            stock_filter=book.xpath(".//p[@class='instock availability']/text()[2]").extract_first()
            yield {
                'title ': book.xpath(".//h3/a/text()[1]").extract_first(),
                'price ': book.xpath(".//p[@class='price_color']/text()").extract_first(),
                # 'stock ': book.xpath(".//p[@class='instock availability']/text()[2]").extract_first()
                'stock': str.strip(stock_filter)
              }




            if self.cnt >=1:
                next_url = 'http://books.toscrape.com/catalogue/page-' + str(self.cnt) + '.html'
                self.cnt += 1
                print(self.cnt)
                yield scrapy.Request(url=next_url, callback=self.parse)




