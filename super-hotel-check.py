# -*- coding: utf8 -*-
# coding: utf8
import pycurl
import time
import codecs
import sys
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

from StringIO import StringIO

dir="./superhotel-backup/"
timeStamp = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
fileName = dir + timeStamp + ".html"
buffer = StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'https://hotel.reservation.jp/superhotel/jpn/reservation/a1.asp')
c.setopt(pycurl.SSL_VERIFYPEER, 1)
c.setopt(pycurl.SSL_VERIFYHOST, 2)
#c.setopt(pycurl.CAINFO, "/path/to/updated-certificate-chain.crt")

post_data = {'ir_change': '',
             'ne_area': '90',
             'ir_reserv_dd': '4',
             'ir_reserv_yyyymm': '2017/03/01',
             'scnt': '1',
             'mcnt': '3',
             'rcnt': '1',
             'smoke': '1'
             }
# Form data must be provided already urlencoded.
postfields = urlencode(post_data)
print postfields

# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
c.setopt(c.POSTFIELDS, postfields)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
f = open(fileName, 'w')
f.write(body)
f.closed
