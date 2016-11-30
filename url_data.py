from flask import Flask, jsonify
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

app = Flask(__name__)

def doWork():
    while True:
        url = q.get()
        #print url
        if(check_url(url)<400):
            data = image_properties(url)
            data['status'] = "passed"
            #array.append(data)
            #print x+1
        else:
            data = {}
            data['status'] = "failed"
            #array.append(data1)
            #print x+1
        #status, url = getStatus(url)
        array.append(data)
        #doSomethingWithResult(data)
        q.task_done()

