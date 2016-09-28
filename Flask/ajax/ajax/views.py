from ajax import app, render_template, Response, jsonify, request
import time 
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/serverEvents')
def serverEvents():
    mensaje = '000000'
    return render_template('serverEvents.html', mensaje=mensaje)

@app.route('/_switch')
def switch():
    print ('alguien esta en _switch')
    def leer_tarjeta():
        while True:
            with open('mensajes.txt', 'r') as cardFile:
                tarjeta = cardFile.read().strip()
                yield 'data: {0}\n\n'.format(tarjeta)
                time.sleep(1)
    return Response(leer_tarjeta(), mimetype='text/event-stream')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)
