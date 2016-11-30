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


app = Flask(__name__, static_url_path='')

def doWork():
    while True:
        url = q.get()
        #print url,"****"
        data = {}
	#print check_url(url), url
        if(check_url(url)<400):
            
            data = image_properties(url)
            data['status'] = "passed"
            #print data
            #array.append(data)
            #print x+1
        else:
            
            data['status'] = "failed"
            data['url'] = url
            data['img_format'] = None
            data['img_(height, width)'] = None
            data['img_size'] = None
            data['img_url_response'] = "failed"
            data['p-hash'] = None
            #print data
            #array.append(data1)
            #print x+1
        #status, url = getStatus(url)
        array.append(data)
        #doSomethingWithResult(data)
        q.task_done()


def read_cell(csv_f,x,y):
    with open(csv_f, 'r') as f:
        reader = csv.reader(f, dialect=csv.excel_tab)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

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
    
    

def check_url(url):
	try:
		connection = urllib2.urlopen(url)
		return connection.getcode()
		connection.close()
	except:
		return 404

    #except urllib2.HTTPError, e:

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

@app.route('/todo/api/v1.0/image_details', methods=['POST'])
def image_details():

    #print request.files
    csv_file = request.form['csv_file']
    if not csv_file:
        abort(400)
    
    #concurrent = 2
    
    
    urls = csv_operate(csv_file) 
    #print urls
    #q = Queue(concurrent * 2)

    for i in range(concurrent):
        t = Thread(target=doWork)
        t.daemon = True
        t.start()
    try:
        for url in urls:
            q.put(url.strip())
        q.join()
    except KeyboardInterrupt:
        sys.exit(1)
    
    data = array

    json2csv(data)
    

    '''with open('output.csv', 'rb') as f:
        reader = csv.reader(f)
        csvList = list(reader)
    si = StringIO.StringIO()
    cw = csv.writer(si)
    cw.writerows(csvList)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output'''
    return "http://127.0.0.1:5000/output.csv"
    
    
@app.route('/')
def index():
    return "MAKE SURE YOUR URLS ARE IN THE FIRST COLUMN. IF NOT THEN SHIFT IT : SPOILERS ALERT: ARYA IS NOT NOONE UNCLE : BENJEN IS BACK : DROGON RETURNS "

if __name__ == '__main__':
    start = time.time()
    print("start")

    #counter = 1

    concurrent = 10
    q = Queue(concurrent * 2)
    array = []

    app.run(debug=True)

    end = time.time()
    print(end - start)
    
