from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "shipping-service"}), 200


@app.route("/shipping", methods=["GET"])
def shipping():
    return jsonify(
        {
            "shipping": [
                {"id": 701, "carrier": "UPS"},
                {"id": 702, "carrier": "FedEx"}
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
