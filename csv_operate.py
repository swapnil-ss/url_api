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



def csv_operate(csv_file):
    csv_f = open(csv_file)
    csv_read = csv.reader(csv_f, dialect=csv.excel_tab)
    
    urls = []
    
    for row in csv_f:
        url = row.split(",")[0]
        urls.append(url)

    length = len(urls)
    print length
    #print urls

    #for x in range(0, length):
	#url = read_cell(csv_file,0,x)
        #if(check_url(url)<400):
            #data = image_properties(url)
            #array.append(data)
            #print x+1
        #else:
            #data1 = {}
            #data1['invalid url index'] = x+1
            #array.append(data1)
            #print x+1
    csv_f.close()
    return urls 	
    
    
