from flask import Flask,render_template
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)

@app.route('/')
def index():
    with counter.get_lock():
        counter.value += 1
        count = counter.value
    return render_template('main.html', hits=count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

