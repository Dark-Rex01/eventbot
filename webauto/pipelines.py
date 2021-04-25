# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class WebautoPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        self.curr = self.conn.cursor()
        self.curr1 = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):

        sql = "INSERT IGNORE INTO users (`id`, `name`, `webname`, `website`) VALUES (%s, %s, %s, %s)"
        self.curr.execute(sql, (
            item['title'][0],
            item['dates'][0],
            item['webname'],
            item['website']
        ))
        if self.curr.rowcount >= 1:
            sql1 = "INSERT IGNORE INTO mailcon (`title`, `date`) VALUES (%s, %s)"
            self.curr1.execute(sql1, (
            item['title'][0],
            item['dates'][0]
            ))
        self.conn.commit()
