# this code has been taken from the scrapy framework and their get started guide, this is a basic web crawler that will retreive data from urls.
# https://docs.scrapy.org/en/latest/intro/tutorial.html

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    
    # websites to the scraped
    def start_requests(self):
        urls = [
            'https://yourstoryclub.com/short-stories-friendship/friends-short-story-illusion-of-zero/',
            'https://yourstoryclub.com/short-stories-from-college/short-story-on-friendship-the-boy/',
            'https://yourstoryclub.com/short-stories-from-college/short-story-for-friends-me-and-smita/',
            'https://yourstoryclub.com/short-stories-from-college/friends-short-story-7-in-a-bus/',
            'https://yourstoryclub.com/short-stories-friendship/friends-short-story-illusion-of-zero/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

            
            # saves file 
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
