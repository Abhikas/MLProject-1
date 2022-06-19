from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "Starting Machine Learning Project"

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True)