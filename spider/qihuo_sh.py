#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import http
import json
import urllib
import random
import time
import requests
from lxml import etree, html
from spider.dbutils import DB
from datetime import datetime


class qihuo_sh():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_url(self, page=None):
        return "http://www.shfe.com.cn/data/delaymarket_rb.dat"

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        try:
            product_dic = json.loads(html)
            return product_dic
        except Exception:
            return ""
    def get_date(self):
        urls = 'http://www.shfe.com.cn/products/rb'
        req = requests.get(url=urls, headers=self.headers)
        req.encoding = 'utf-8'
        data = req.text

        try:
            tree = html.fromstring(data)
            items = str(tree.xpath('//*[@id="tab_conbox"]/li[2]/h3/span[2]/text()'))
            items = items.replace("'更新时间：", '')
            items = items.replace("'", '')[1:11]
            items = items.replace("-", '')
            return items
        except Exception:
            return ""

    def parse(self, row):
        print(row)

    def insert(self, data):
        db = DB()
        dt = datetime.now()
        dtstr = dt.strftime('%Y%m%d')
        datestr = self.get_date()
        if dtstr != datestr :
            pass
        sql = "delete from SGBA_ODS_WB_QH where qh_day = '"+ datestr+"' and qh_code ='"+data['contractname']+"'"
        db.execute(sql)
        db.commit()
        qh_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
        sql = "INSERT INTO SGBA_ODS_WB_QH(QH_ID,QH_DAY,QH_CODE,QH_NAME,QH_KP,QH_ZG,QH_ZD,QH_ZX,QH_ZDS,QH_ZJS) VALUES" \
              "("+qh_id +"," +dt.strftime('%Y%m%d')+",'"+ data['contractname']+"','螺纹钢"+data['contractname']+"',"+data['openprice'].replace("--","0")+","+data['highprice'].replace("--","0")+","+data['lowerprice'].replace("--","0")+","+data['lastprice']+","+data['upperdown']+","+data['presettlementprice']+")"
        db.execute(sql)
        db.commit()
        db.close()

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        url = self.get_url()
        rows = self.get_data(url)
        j = len(rows['delaymarket'])
        for i in range(0,j-1):
            self.insert(rows['delaymarket'][i])