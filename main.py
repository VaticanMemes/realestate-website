from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/get_started')
def get_started():
    return render_template('get_started.html')

if __name__ == '__main__':
    app.run(debug=True)