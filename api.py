import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SERVER_NAME'] = 'example.com'


@app.route('/', methods=['GET'])
def home():
    return "<h1>Web API test - by trongan93</h1><h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run()