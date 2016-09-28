from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_monkey():
    ''' Regresa un mensaje tonto con cada mensaje '''

    resp = twilio.twiml.Response()
    resp.message('Hola, Chango Mobil')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
