from bottle import route, run, template, default_app

@route('/api')
def hihi():
    return '<b>hit api</b>!'
    #return template('<b>hit api</b>!')

@route('/api/')
def api_slash():
    return '<b>hit api/</b>!'
    #return template('<b>hit api/</b>!')

@route('/')
def slash():
    return '<b>hit /</b>!'
    #return template('<b>hit /</b>!')

@route('*')
def catch_all():
    return '<b>hit /</b>!'
    #return template('<b>hit /</b>!')


application = default_app()

if __name__ == "__main__":
  run(host='0.0.0.0', port=8000)
