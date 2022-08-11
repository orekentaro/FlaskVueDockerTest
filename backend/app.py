from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)


@app.route("/")
def test():
    return {"message": "hello"}


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
