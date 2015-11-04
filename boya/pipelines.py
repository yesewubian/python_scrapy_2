# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class BoyaPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='', db='boya_specialty', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        
    #----------------------------------------------------------------------
    def process_item_bak(self,item,spider):
        pass
        
    def process_item(self, item, spider):
        try:
            pro_id = self.get_region_id(item['pro'], 1, 0)
            city_id = self.get_region_id(item['city'], 2, pro_id)
            county_id = self.get_region_id(item['county'], 3, city_id)
            self.cursor.execute("""INSERT INTO by_specialty(name,pro_id,city_id,county_id,pic,introduce,ext) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (item['name'], pro_id, city_id, county_id, item['pic'], item['introduce'], item['ext']))
            self.conn.commit()
            
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            return item
        
    def get_region_id(self,region_name,level_id,father_id=0):
        if region_name == '':
            return 0
        try:
            self.cursor.execute("""SELECT * FROM by_region WHERE region_name = %s""",(region_name))
            lines = self.cursor.fetchall()
            if lines:
                return lines[0][0];
            else:
                self.cursor.execute("""INSERT INTO by_region(region_name,level_id,father_id) VALUES (%s, %s, %s)""",
                    (region_name, level_id, father_id))
                return self.cursor.lastrowid
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            return item
            
            