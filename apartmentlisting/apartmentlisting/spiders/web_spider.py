import logging
import scrapy

class WebSpider(scrapy.Spider):

    name = 'WebSpider'
    #crawling starts from here
    start_urls = [ 'https://www.bayut.com/to-rent/property/dubai/' ]

    def parse(self,response):

        #scraps the links to listed appartments
        #in the listing page
        for listings in response.css('li.ef447dde') :

            #gets all the relative links of listed appartments
            #callbacks craw_listing function with response as param
            yield  scrapy.Request(response.urljoin(listings.css('a._287661cb::attr(href)').get()),callback= self.crawl_listing)

    #scraps data from listed appartment
    # yields as a dictonary
    def crawl_listing(self,response):
        
        try:

            yield{
                    "property_id" : response.css('span._812aa185::text')[2].get(),
                    "purpose" : response.css('span._812aa185::text')[1].get(),
                        "type" : response.css('span._812aa185::text')[0].get(),
                    "added_on" : response.css('span._812aa185::text')[5].get(),
                    "furnishing" : response.css('span._812aa185::text')[3].get(),
                    "price" : {
                            "currency" : response.css('div.c4fc20ba > span::text')[0].get(),
                            "amount" : response.css('div.c4fc20ba > span::text')[1].get(),
                        },
                    "location" : response.css('span._105b8a67::text').get(),
                    "bed_bath_size" : {
                            "bedrooms" : response.css('span.fc2d1086::text')[0].get().split(' ')[0],
                            "bathrooms" : response.css('span.fc2d1086::text')[1].get().split(' ')[0],
                            "size" : response.css('span.fc2d1086 > span::text').get(),
                        },
                    "permit_number" : response.css('span.ff863316::text')[6].get(),
                    "agent_name" : response.css('span._55e4cba0::text').get(),
                    "image_url" :
                    response.css('picture._219b7e0a > source::attr(srcset)').get(),
                    "breadcrumbs" : ">".join(list(map(str,response.css('div._74ac503e > a > span::text').getall()))),
                    "amenities" : response.css('div._40544a2f >span._005a682a::text').getall(),
                    "description" : ''.join(response.css('span._2a806e1e::text').getall())
,
                }
        except :
            print("error")
        