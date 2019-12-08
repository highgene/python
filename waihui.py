#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import html

from Spider import Spider


class Waihui(Spider):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_url(self, page=None):
        return "http://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do"

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html1 = req.text

        tree = html.fromstring(html1)
        for i in range(1, 10):
            xpath = tree.xpath('//*/tr[@class="first"][' + str(i) + ']/td')
            a1 = str.strip(xpath[0].text)
            a2 = str.strip(xpath[1].text)
            a3 = str.strip(xpath[2].text)
            print(a1, a2, a3)

    def parse(self, row):
        return row

    def insert(self, data):
        print(data)

    def run(self):
        url = self.get_url()
        rows = self.get_data(url)