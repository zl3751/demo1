import time 
from flask import Flask
from scipy.sparse.construct import random
from flask_cors import CORS
from flask import request, jsonify
import json
import pickle
from datetime import datetime
import random


def load_model(filename):
    with open(f"./{filename}", "rb") as infile:
        _model = pickle.load(infile)
        return _model


model = load_model("RF3.pickle")
app = Flask(__name__) 
CORS(app)  

epoch = 1

@app.route('/model/query', methods=["GET"])
def query_once():
	query = model.query()
	return {
		"content" : query["content"],
		"index" : str(query["index"]),
		"oracle" : str(query["oracle"])
	}

@app.route('/model/label', methods=["POST"])
def labeling():
	label = request.get_json()
	print(label)
	model.label(label["idx"], label["label"])
	performance = model.performance
	data = model.learner.predict_proba(model.x_pool_vec).tolist()
	score = model.score()
	uncertainties = {"epoch": len(model.performance) - 1, 
									"values" : 
										[{"id": i, "value": v[0]} for i, v in enumerate(data)]}
	randomIdx = random.sample(range(0, len(uncertainties["values"])), 50)
	uncertainties["values"] = [v for i, v in enumerate(uncertainties["values"]) 
														if i in randomIdx]
	return json.dumps({
		"performance" : performance,
		"uncertainty" : uncertainties
	})

@app.route('/model/performance', methods=["GET"])
def get_performance():
	return {
		"performance_list" : model.get_performance()
	}


