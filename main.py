import zmq, json

from datetime import datetime
from flask import Flask, request
app = Flask(__name__)

app.config.DEBUG = True

'''
{"@source":"unknown","@type":null,"@tags":[],"@fields":{},"@message":"Hello world","@timestamp":"2012-06-26T15:58:20.135353Z"}
'''

def _to_logstash_format(log):
    '''
    Converts an appengine log dict to logstash format
    '''
    return {'@source': 'appengine://' + log['app_id'],
            '@type': 'appengine',
            '@tags': [],
            '@fields': {k: v for k, v in log.iteritems()
                        if v and k not in ['message', 'app_id']},
            '@message': log['message'],
            '@timestamp': datetime.fromtimestamp(log['start_time']).isoformat()}


@app.route("/logs", methods=['PUT'])
def root():
    context = zmq.Context.instance()
    socket = context.socket(zmq.PUSH)
    socket.connect('tcp://127.0.0.1:2120')
    for log in request.json['logs']:
        socket.send(json.dumps(_to_logstash_format(log)) + '\n')
    return ''

if __name__ == "__main__":
    app.run()
