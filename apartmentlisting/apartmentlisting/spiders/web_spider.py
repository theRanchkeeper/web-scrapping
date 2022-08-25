import scrapy

class WebSpider(scrapy.Spider):

    name = 'WebSpider'
    #crawling starts from here
    start_urls = [ 'https://www.bayut.com/to-rent/property/dubai/' ]

    def parse(self,response):

        #scraps the links to listed appartments
        #in the listing page
        for listings in response.css('li.ef447dde') :

            yield {
                
                'item_page' : listings.css('a._287661cb::attr(href)').get()

            }  
