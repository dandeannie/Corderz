from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "message": "Ledgerly API is running!",
        "version": "1.0.0"
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"})

# For Vercel serverless
if __name__ == '__main__':
    app.run(debug=True)
