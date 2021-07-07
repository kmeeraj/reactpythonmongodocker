import datetime
import os
import pymongo
import json
from pymongo import MongoClient

#import pprint

from flask_cors import CORS, cross_origin
 
from flask import Flask, Response, request
#from flask_mongoengine import MongoEngine
from logger import MyLogger

app = Flask(__name__)
cors = CORS(app)
# cors = CORS(app, resources={r"/*": {"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
'''app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': 'mcdDB'
}'''

#db = MongoEngine()
#db.init_app(app)

client =  MongoClient("mongodb://admin:test1234@mongodb:27017")
db = client.mcdDB
logger = MyLogger('main', './server2.log', use_stdout=True, log_level='debug')

@app.route("/api", methods=['GET', 'POST'])
def index():
	payload = {};
	logger.debug('successfully fetches tags from all the task')
	for doc in db.status.find():
		#pprint.pprint(doc)
		logger.debug(doc)
		payload = doc['text']
	logger.debug('payload' + payload)
	#return Response({ 'data': payload}, mimetype="application/json", status=200)
	return (json.dumps({ 'data': payload}), 200, {'content-type': 'application/json'})
	#pprint.pprint('hi')
	#return Response({'data': 'payload'}, mimetype="application/json", status=200)
	#return "Praise the Lord. The Lord shall bless thee out of Zion"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))