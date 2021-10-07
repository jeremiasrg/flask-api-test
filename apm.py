# initialize using environment variables
import os
import random
from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
app = Flask(__name__)

server_url = 'http://localhost:8200'
if os.environ.get('SERVER_URL') != None:
    server_url = os.environ.get('SERVER_URL')

app_name = 'flask-apm-client'
if os.environ.get('APP_NAME') != None:
    app_name = os.environ.get('APP_NAME')

service_name = 'Flask-APM-Test'
if os.environ.get('SERVICE_NAME') != None:
    service_name = os.environ.get('SERVICE_NAME')


app.config['ELASTIC_APM'] = {
    'APP_NAME': app_name,
    'DEBUG': True,
    'SERVER_URL': server_url,
    'TRACES_SEND_FREQ': 5,
    'SERVICE_NAME': service_name,
    'FLUSH_INTERVAL': 1,
    'MAX_QUEUE_SIZE': 1,
}
apm = ElasticAPM(app, logging=True)


@app.route('/test/getAll', methods=['GET'])
def getTests():
    1/random.randrange(0, 3)
    return 'Get all tests!'


@app.route('/test/create', methods=['POST'])
def createTest():
    1/random.randrange(0, 3)
    return 'Create new test'


@app.route('/test/update', methods=['UPDATE'])
def updateTest():
    1/random.randrange(0, 3)
    return 'Update test'


@app.route('/test/delete', methods=['DELETE'])
def deleteTest():
    1/random.randrange(0, 3)
    return 'Delete task'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
