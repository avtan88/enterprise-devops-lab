from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "search-service"}), 200


@app.route("/search", methods=["GET"])
def search():
    return jsonify(
        {
            "results": [
                {"id": 801, "match": "Laptop"},
                {"id": 802, "match": "Mouse"}
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
