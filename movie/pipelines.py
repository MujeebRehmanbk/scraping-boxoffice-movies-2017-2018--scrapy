# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class MoviePipeline(object):


    def __init__(self):
        self.csvwriter = csv.writer(open("boxoffice2017_2019.csv", "w", newline=''))
        self.csvwriter.writerow(["title", "domestic_revenue"])

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])
        row.append(item["domestic_revenue"])
        # row.append(item["world_revenue"])
        # row.append(item["distributor"])
        # row.append(item["opening_revenue"])
        # row.append(item["opening_theaters"])
        # row.append(item["budget"])
        # row.append(item["MPAA"])
        # row.append(item["genres"])
        # row.append(item["release_days"])
        self.csvwriter.writerow(row)
        return item



    def process_item(self, item, spider):
        return item


# import json

# class JsonWriterPipeline:

#     def open_spider(self, spider):
#         self.file = open('items.jl', 'w')

#     def close_spider(self, spider):
#         self.file.close()

#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item