from bottle import route, run, template, default_app, Bottle

app = application = Bottle()

@app.route('/api')
def hihi():
    log("hit api")
    return '<b>hit api</b>!'

@app.route('/api/')
def api_slash():
    log("hit api/")
    return '<b>hit api/</b>!'

@app.route('/')
def slash():
    log("hit /")
    return '<b>hit /</b>!'

@app.route('/api/hi')
def catch_more():
    log("hit api/hi")
    return '<b>hit /api/hi</b>!'

@app.route('/api/byah')
def catch_more():
    log("hit api/byah")
    return '<b>hit /api/byah</b>!'

@app.route('/api/<url:re:.+>')
def catch_more(url):
    log("hit catch more")
    return '<b>hit /api/%s</b>!' % url

@app.route('/<url:re:.+>')
def catch_all(url):
    log("hit catch all")
    return '<b>hit /%s</b>!' % url

def log(message):
  with open("byah_api.log", "a") as myfile:
      myfile.write(message)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5080)
