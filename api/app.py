import time 
from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
from model import ALModel 
import json

model = ALModel("./imdb.csv")
app = Flask(__name__) 
CORS(app) 

@app.before_first_request
def prepare_model():
	model.pretraning()
	print("Pre-training Done")


@app.route('/model/pre')
def start_training():
	p = model.get_performance()
	response = {"newscore": p[len(p) - 1]}
	return jsonify(response)


@app.route('/model/query', methods=["GET"])
def query_once():
	query = model.query()
	return {
		"content" : query["content"],
		"idx" : str(query["idx"]),
		"oracle" : str(query["oracle"])
	}

@app.route('/model/label', methods=["POST"])
def labeling():
	label = request.get_json()
	new_performance = model.label(label["label"], label["idx"])
	print(model.performance)
	return {
		"performance" : new_performance
	}

@app.route('/model/performance', methods=["GET"])
def get_performance():
	return {
		"performance_list" : model.get_performance()
	}
