#!/usr/bin/python
# -*- coding: utf8 -*-

import urllib
import urllib2
import random
from lxml import html
import cookielib
import time

headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0)'}
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)

def get_some(now_page):
    req = urllib2.Request(url,data,headers)
    page = urllib2.urlopen(req)
    doc = html.document_fromstring(page.read())
    for url in doc.cssselect('something'):
        URLS += [url.get('href')]

