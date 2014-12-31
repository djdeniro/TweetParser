#!/usr/bin/python
# -*- coding: utf8 -*-

import urllib
import urllib2
import random
from lxml import html
import cookielib
import time

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
mailname = "catezokina"
def generate_str():
    q = ''
    s = "1234567890"
    for i in xrange(5):
        q+=s[random.randint(1,8)]
    return q
mailname += generate_str()
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
def get_key(page):
    for i in page.split("\n"):
        if "value" in i and 'token' in i:
            return i.split('"')[5]
values = {}
data = make_data(values)
req = urllib2.Request("http://vk.com/", data, headers)
page = urllib2.urlopen(req)
page = page.read()
data = make_data(values)
req = urllib2.Request("http://m.twitter.com/", data, headers)
page = urllib2.urlopen(req)
page = page.read()
# print page
doc = html.document_fromstring(page)
values["authenticity_token"] = get_key(page)
values["oauth_signup_client[fullname]"] = "hello Wave"
values["oauth_signup_client[phone_number]"] = mailname*3+"@gmail.com"
values["oauth_signup_client[password]"] = "qupassV"
values["wfa"] = 1
values["commit"] = " Sign up for Twitter "
for i in xrange(5):
    time.sleep(1)
    print i,
print
data = make_data(values)
req = urllib2.Request("https://mobile.twitter.com/signup/submit", data, headers)
page = urllib2.urlopen(req)
page = page.read()
values = {}
values["authenticity_token"] = get_key(page)
values["settings[screen_name]"] = mailname
values["commit"] = "Continue"
data = make_data(values)
print page
print mailname