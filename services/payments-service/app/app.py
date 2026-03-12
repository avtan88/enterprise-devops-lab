from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "payments-service"}), 200


@app.route("/payments", methods=["GET"])
def payments():
    return jsonify(
        {
            "payments": [
                {"id": 501, "status": "approved"},
                {"id": 502, "status": "pending"}
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
