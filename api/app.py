import time 
from flask import Flask
from flask_cors import CORS
from flask import request
# from flask_script import Manager, Server
from model import ALModel 

model = ALModel("./imdb.csv")


	
app = Flask(__name__) 


CORS(app) 


@app.before_first_request
def prepare_model():
	print(model.learner)
	model.pretraning()
	print(model.performance)


@app.route('/pre')
def test_page():
	return {
		'query': "XX"
	}

### git test

@app.route('/query', methods=["GET"])
def query_once():
	query = model.query()
	return {
		"content" : query["content"],
		"idx" : str(query["idx"]),
		"oracle" : str(query["oracle"])
	}

@app.route('/label', methods=["POST"])
def labeling():
	label = request.get_json()
	new_performance = model.label(label["label"], label["idx"])
	print(model.performance)
	return {
		"performance" : new_performance
	}

# if __name__ == "__main__":
#     manager.run()

	
# sample_data = [{'id': 0, 'text' : 'IMDB Review 0'}, {'id': 1, 'text' : 'IMDB Review 1'}, {'id': 2, 'text' : 'IMDB Review 2'}]

# manager = Manager(app)
# manager.add_command('runserver', CustomServer())
# class CustomServer(Server):
#     def __call__(self, app, *args, **kwargs):
#         prepare_model()
					#  return Server.__call__(self, app, *args, **kwargs)
#  