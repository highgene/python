#!/usr/bin/python
# -*- coding: UTF-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from kpi import kpi
from moneysupply import moneysupply
from hl import hl
from shibor import shibor
from qihuo_dl import qihuo_dl
from qihuo_sh import qihuo_sh
from stock_a import stock_a
from stock_hk import stock_hk
import os

'''
    大连、郑州商品交易所：75+60+90+150=375    
    上午09:00 -- 10:15 10:30 -- 11:30
    下午 13:30 -- 15:00
    夜盘 21:00-23:30

    上海期货交易所：75+60+40+40+330=545分钟
    上午 09:00 -- 10:15 10:30 -- 11:30
    下午 13:30 -- 14:10 14:20 -- 15:00
    夜盘 21:00-次日2:30

    A股：9:30 — 11:30；13:00 — 15:00
    H股：10:00 — 12:30；14:30 — 16:00
    '''
if __name__ == '__main__':


    scheduler = BlockingScheduler()

    scheduler.add_job(kpi().run, 'cron', hour='12', minute='0', second='0')
    scheduler.add_job(moneysupply().run, 'cron', hour='12', minute='0', second='0')
    scheduler.add_job(hl().run, 'cron', hour='6,8,10,12,14,16,18', minute='0', second='0')
    scheduler.add_job(shibor().run, 'cron', hour='6,8,10,12,14,16,18', minute='0', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='9-11', minute='*/5', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='11', minute='(0-30)/5', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='13', minute='(30-60)/5', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='14', minute='*/5', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='21-23', minute='*/5', second='0')
    
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='9-11', minute='*/5', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='11', minute='(0-30)/5', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='13', minute='(30-60)/5', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='14', minute='*/5', second='0')
    scheduler.add_job(qihuo_dl().run, 'cron', day_of_week='mon-fri',hour='21-23', minute='*/5', second='0')

    scheduler.add_job(stock_a().run, 'cron', day_of_week='mon-fri',hour='9', minute='(30-60)/5', second='0')
    scheduler.add_job(stock_a().run, 'cron', day_of_week='mon-fri',hour='10', minute='*/5', second='0')
    scheduler.add_job(stock_a().run, 'cron', day_of_week='mon-fri',hour='11', minute='(0-30)/5', second='0')
    scheduler.add_job(stock_a().run, 'cron', day_of_week='mon-fri',hour='13-15', minute='*/5', second='0')

    scheduler.add_job(stock_hk().run, 'cron', day_of_week='mon-fri',hour='10-11', minute='*/5', second='0')
    scheduler.add_job(stock_hk().run, 'cron', day_of_week='mon-fri',hour='12', minute='(0-30)/5', second='0')
    scheduler.add_job(stock_hk().run, 'cron', day_of_week='mon-fri',hour='14', minute='(30-60)/5', second='0')
    scheduler.add_job(stock_hk().run, 'cron', day_of_week='mon-fri',hour='15', minute='*/5', second='0')
    
    print('Press Ctrl+{0} to exit'.format('C' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass
    '''

    spiders = [
        #kpi()
        moneysupply()
        #hl(),
        #shibor(),
        #qihuo_sh()
        #qihuo_dl(),
        #stock()
    ]
    for spider in spiders:
        spider.__getattribute__("run")()
'''