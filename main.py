import urllib2
from bs4 import BeautifulSoup as heinz
import sqlite3
import os
DB_ROOT = os.path.expanduser('~')

class index:
    def __init__(self,domain):
        try:
            con = sqlite3.connect(r'%s\\indexdb\\%s.sqlite'%(DB_ROOT,domain.replace('/','-')))

        except StandardError as e:
            print 'CONNECT_DB: %s' % e
            pass

        cur = con.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS rootindex (uid int PRIMARY KEY, url varchar(255))'

        try:
            cur.execute(sql)
            
        except Exception as e:
            print 'SETUP_DB: %s' % e
            pass

        sql = 'SELECT COUNT(*) FROM rootindex'

        try:
            cur.execute(sql)
        except Exception as e:
            print 'Q_DB: %s' % e
            pass

        item = cur.fetchone()
        if int(item[0]) < 0:
            soup = heinz(self.get_page(domain))
            print soup
            
            

    def get_page(self,url):
        theurl = url
        txdata = None
        txheaders = {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        req = urllib2.Request(theurl,txdata,txheaders)
        handle = urllib2.urlopen(req)
        return handle.read()



