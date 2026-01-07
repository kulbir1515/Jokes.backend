from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

jokes = [
    "Fashion changes fast but my wardrobe stays the same",
    "I dressed up to stay home and scroll social media",
    "Trendy clothes are just old clothes with confidence",
    "Fashion advice wear what feels comfortable"
]

@app.route("/joke")
def joke():
    return jsonify({"joke": random.choice(jokes)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
