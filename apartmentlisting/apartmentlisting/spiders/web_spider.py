import logging
from os import link
import scrapy

class WebSpider(scrapy.Spider):

    name = 'WebSpider'
    #crawling starts from here
    start_urls = [ 'https://www.bayut.com/to-rent/property/dubai/' ]

    def parse(self,response):

        #scraps the links to listed appartments
        #in the listing page
        for listings in response.css('li.ef447dde') :

            yield  scrapy.Request(response.urljoin(listings.css('a._287661cb::attr(href)').get()),callback= self.crawl_listing)

    #this function will get all relative links of listed appartment
    #  
    def crawl_listing(self,response):
        
        self.logger.info("Got into products links :",response.url)
        