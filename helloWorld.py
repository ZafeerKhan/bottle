from bottle import route, run

@route('/')
def index(name):
    return "Hello World"

run(host='0.0.0.0', port=80)
