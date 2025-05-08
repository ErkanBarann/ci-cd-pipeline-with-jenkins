from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello from CI/CD pipeline with Jenkins!"})

if __name__ == "__main__":
    # Development only: do NOT run with debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)
