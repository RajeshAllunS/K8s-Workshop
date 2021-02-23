from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

@app.route("/")
def main():
    redis.incr('hits')
    count = int(redis.get('hits'))
    return render_template('main.html', hits=count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
