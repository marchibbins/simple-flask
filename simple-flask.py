from flask import Flask, render_template
import json

# App instance
app = Flask(__name__)

# Debug mode, with auto-reload
app.debug = True

# Simple JSON file parser
def get_json(path):
    file = open('data/simple.json')
    data = json.load(file)
    file.close()
    return data

# Wrapper for template render and JSON parser
def render(view, data):
    data = get_json(data)
    return render_template(view, **data)

# Routes
@app.route("/")
def index():
    return render('simple.html', 'data/simple.json')

if __name__ == "__main__":
    app.run()
