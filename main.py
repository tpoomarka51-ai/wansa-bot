import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Wansa Bot is Running! 🔥"

@app.route('/wansa')
def wansa():
    return "Hello from Wansa Bot!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
