from flask import Flask, jsonify, send_file
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from PIL import Image
import csv
import httplib
from httplib import HTTP
from urlparse import urlparse
import urllib2
import cStringIO
import urllib
import json
import time
from urlparse import urlparse
from threading import Thread
import httplib, sys, getopt
from Queue import Queue
import StringIO
import imagehash

def image_properties(url):
    file = urllib.urlopen(url)
    data = {}
    try:
        img = Image.open(file)
        data['url'] = url
        data['img_format'] = img.format
        data['img_(height, width)'] = img.size
        data['img_size'] = file.headers.get("content-length")
        data['img_url_response'] = check_url(url)
        #data['p-hash'] = str(imagehash.phash(img))+str(imagehash.phash(img.rotate(90)))+str(imagehash.phash(img.rotate(180)))+str(imagehash.phash(img.rotate(270)))
        #counter = counter + 1
        data['p-hash'] = imagehash.phash(img)
        instant = time.time()
        print (instant - start)
    except:
        data['url'] = url
        data['img_format'] = None
        data['img_(height, width)'] = None
        data['img_size'] = None
        data['img_url_response'] = "failed"
        data['p-hash'] = None
    
    return data

