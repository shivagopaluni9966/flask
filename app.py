from flask import Flask, render_template
import json
import datetime

app = Flask(__name__)

def load_items():
    with open('app.json', encoding='utf-8') as f:
        return json.load(f)

items = load_items()

@app.context_processor
def inject_year():
    return {'current_year': datetime.datetime.now().year}

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

