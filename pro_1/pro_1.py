# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '?s=4957699'
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>(.*?)<span class="stats-vote.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[2])
        if not haveImg:
            print item[0], item[1], item[3]
except urllib2.URLError, e:
    if hasattr(e, "code"):
       print e.code
    if hasattr(e, "reason"):
       print e.reason


