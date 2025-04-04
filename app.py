from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        # Ensure request contains JSON
        data = request.get_json(force=True, silent=True)

        if not data or 'long_url' not in data:
            return jsonify({"error": "No URL provided"}), 400

        long_url = data['long_url']
        short_url = "http://short.ly/abc123"  # Mock short URL
        return jsonify({"short_url": short_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
