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


def json2csv(data):
    f = csv.writer(open("/home/swapnil/static/output.csv", "wb+"))

    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["url","img_format", "img_(height, width)", "img_size", "img_url_response","p-hash"])

    #print data

    for x in data:
        
        f.writerow([x["url"],
                    x["img_format"], 
                    x["img_(height, width)"], 
                    x["img_size"], 
                    x["img_url_response"],
                    x["p-hash"]]) 

