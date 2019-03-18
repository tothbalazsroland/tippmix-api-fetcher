from flask import Flask
import urllib2
import json
from flask import jsonify

app = Flask(__name__)
tippmix_api_url = "http://api.tippmix.hu/tippmix/search"

@app.route('/')
def hello_world():

    response = urllib2.urlopen(tippmix_api_url).read()
    content = json.loads(response)
    return jsonify(content)


if __name__ == '__main__':
    app.run()
