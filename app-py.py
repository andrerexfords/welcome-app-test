from flask import Flask

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name=None):
    if name:
        return f"Selamat datang {name}"
    else:
        return "Anonymous"

@app.route('/welcome/')
def welcome_anonymous():
    return "Anonymous"

@app.route('/welcome/healthcheck')
def healthcheck():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
