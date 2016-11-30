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

def check_url(url):
	try:
		connection = urllib2.urlopen(url)
		return connection.getcode()
		connection.close()
	except:
		return 404

    #except urllib2.HTTPError, e:


