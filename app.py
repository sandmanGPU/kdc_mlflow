from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.prediction import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# os.environ['LANG'] = 'en_US.UTF-8'
# os.environ['LC_ALL'] = 'en_US.UTF-8'

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
# By adding @cross_origin() as a decorator, 
# you are indicating that this route should allow cross-origin requests, 
# meaning it can be accessed by web clients from different domains.
# "different domain" refers to a different combination of protocol, hostname, or port number in a URL
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET', 'POST']) 
@cross_origin()
#  The route accepts both GET and POST requests, as specified by the methods argument. 
# GET requests are typically used for retrieving data, 
# while POST requests are used for submitting data to the server.
def trainRoute():
    os.system("python main.py")
    # os.system("python dvc.repro")
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image=request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == '__main__':
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #for AWS