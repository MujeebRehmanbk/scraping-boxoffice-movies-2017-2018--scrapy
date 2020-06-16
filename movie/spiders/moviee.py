# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem

class MovieeSpider(scrapy.Spider):
    name = 'moviee'
    year = 2017
    Custom_settings = {
        "FEED_FORMAT" : "csv",		
        "FEED_URI" : "feed.csv"
    }
    allowed_domains = ['boxofficemojo.com']
    start_urls = [
                  'https://www.boxofficemojo.com/year/2017/'
         ]
        
    # for year in [2018,2019]:
    #     start_urls.append("https://www.boxofficemojo.com/year/"+str(year)+"/")

    def parse(self, response):
        for tr in response.css('div#table table tr')[1:]:
            hreff = tr.css("td.mojo-cell-wide a").xpath("@href")
            url = response.urljoin(hreff[0].extract())
            #passingurl to another funcand yielding url
            yield scrapy.Request(url , callback=self.parse_page_contents)
            

    def parse_page_contents(self , response):
        items = MovieItem()
        domestic_revenue = response.css("span.a-size-medium.a-text-bold span.money").css("::text").get()
        title = response.css("div.a-fixed-left-grid-col.a-col-right > h1::text").getall()
        
        items['domestic_revenue'] = domestic_revenue
        items['title'] = title
        yield items

        # next_year = "https://www.boxofficemojo.com/year/" +str (MovieeSpider.year)+ "/" 
        
        # if MovieeSpider.year <= 2018:
        #     MovieeSpider.year +=1
        
        #     yield response.follow(next_year , callback = self.parse)