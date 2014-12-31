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
def get_tag():
    f = open("config.true", "r")
    tag = f.readline().split(" ::: ")[1]
    f.close()
    return tag
def get_some(now_page):
    req = urllib2.Request(url,data,headers)
    page = urllib2.urlopen(req)
    doc = html.document_fromstring(page.read())
    for url in doc.cssselect('something'):
        URLS += [url.get('href')]
def make_data(values):
    return urllib.urlencode(values)
values = {}
data = make_data(values)
req = urllib2.Request("https://mobile.twitter.com", data, headers)
page = urllib2.urlopen(req)
page = page.read();
doc = html.document_fromstring(page)
for token in doc.cssselect("div.body input"):
    if (token.get("name") in ["remember_me", "wfa", "commit", "password", "username"]):
        continue
    values[token.get("name")] = token.get("value")

values["wta"] = "1"
values["oauth_signup_client[fullname]"] = "Zhorzhe Hineken"
values["oauth_signup_client[phone_number]"] = "temptimezooho@fake-mail.com"
values["oauth_signup_client[password]"] = "12c4c6"
site = "https://mobile.twitter.com/signup/submit"
data = make_data(values)
req = urllib2.Request(site, data, headers)
page = urllib2.urlopen(req)
page = page.read();
doc = html.document_fromstring(page)
print page