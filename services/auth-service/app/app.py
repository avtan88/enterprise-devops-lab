from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "auth-service"}), 200


@app.route("/auth", methods=["GET"])
def auth():
    return jsonify(
        {
            "auth": "enabled",
            "provider": "internal"
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
