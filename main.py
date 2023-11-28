from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/target_page')
def target_page():
  return 'Welcome to the target page!'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
