# Ahoy, matey! Welcome aboard the Login API ship! ⚓
# This be our placeholder login endpoint, ready to set sail.

from flask import Flask, request, jsonify

# Hoist the main sail — initialize our Flask app!
app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    """Arrr! This be the login endpoint. Present yer credentials or walk the plank!"""
    data = request.get_json()

    # Ye must provide a username and password, or ye'll be cast overboard!
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    # Shiver me timbers! This be a placeholder — no real auth here, savvy?
    if username and password:
        return jsonify({
            "message": "Login successful",
            "username": username,
            "token": "placeholder-token-1234"
        }), 200

    # Avast! Something went wrong on deck!
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/health", methods=["GET"])
def health():
    """A quick check to see if the ship be still afloat!"""
    return jsonify({"status": "ok"}), 200


# Here be where we weigh anchor and start the server!
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
