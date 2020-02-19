#!/usr/bin/python
from flask import Flask, request, jsonify, make_response
import requests
import os.path
import json

application = Flask(__name__)

@application.route('/api/provision/v1/healthz')
def healthz():
    return make_response(jsonify({"health": "ok"}), 200)

@application.route('/api/provision/v1/status')
def status():

    if os.path.exists('/tmp/provision_report.json'):
        with open('/tmp/provision_report.json') as json_file:
            data = json.load(json_file)
            return make_response(jsonify(data), 200)

    return make_response(jsonify({"status": "unknown"}), 404)

@application.route('/api/provision/v1/report', methods=['POST'])
def report():
    with open('/tmp/provision_report.json', 'w') as json_file:
        json.dump(request.json, json_file)

    return make_response("", 200)

if __name__ == '__main__':
     application.run(host='127.0.0.1')
