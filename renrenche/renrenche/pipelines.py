# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings


# class RenrenchePipeline(object):
#     def process_item(self, item, spider):
#         return item

class RenrencheMysqlPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'renrenche',
            'charset': 'utf8'
        }
        # ** 代表将字典中的key 和value当作关键字传过去
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None



    def process_item(self, item, spider):
        # self.cursor.execute(self.sql1,(item['name']))
        self.cursor.execute(self.sql,(item['title'],item['city'],item['small'],item['summary'],item['travel'],item['price']))
        self.conn.commit()

    @property
    def sql1(self):
        if not self._sql:
            self._sql = """
                insert into brands(name) values(%s)

                """
            return self._sql
        return self._sql

    @property
    def sql(self):

        if not self._sql:
            self._sql = """
                 insert into catrs(title,city,small,summary,travel,price) values(%s,%s,%s,%s,%s,%s)

                 """
            return self._sql
        return self._sql