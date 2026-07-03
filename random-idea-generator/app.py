from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

with open("random-idea-generator/ideas.json") as f:
    ideas = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/idea/<category>")
def idea(category):
    if category not in ideas:
        return jsonify({"idea": "Category not found."})

    return jsonify({
        "idea": random.choice(ideas[category])
    })

if __name__ == "__main__":
    app.run(debug=True)