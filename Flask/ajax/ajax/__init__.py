from flask import Flask, render_template, Response, jsonify, request
import time
app = Flask(__name__)
import ajax.views

if __name__ == "__main__":

    app.run(debug=True, threaded=True)
