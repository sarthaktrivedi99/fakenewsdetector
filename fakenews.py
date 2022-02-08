from flask import Flask,request
import json
from ml import model
from scrap import scrap
import logging
app = Flask(__name__)
@app.route("/",methods=['Get'])
def main_page():
    return open("index.html","r").read()
@app.route("/ml",methods=['Get','Post'])
def ml():
    logging.basicConfig(filename='everything.log')
    app.logger.info("payload - "+ request.get_data().decode('utf8'))
    input_data = json.loads(request.get_data().decode('utf8'))
    out_data = scrap.getreadabledata(input_data['data'])
    app.logger.info("input_text/url - "+ input_data['data'])
    out_data = model.tokenize(out_data)
    out_data=model.vectorize(out_data)
    return model.nn_model(out_data.reshape(1,300))
if __name__ == "__main__":
    app.run(debug=True,port=8050,host='0.0.0.0')