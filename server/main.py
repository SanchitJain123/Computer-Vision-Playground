from flask import Flask

# define flask app
app = Flask(__name__)

# index route
@app.route('/', methods=['GET'])
def index():
    return "Server is up and running"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
