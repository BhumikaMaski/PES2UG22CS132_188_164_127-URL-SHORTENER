from flask import Flask, request, redirect, jsonify
import redis
import shortuuid

app = Flask(__name__)

# Connect to Redis (Running in a separate container)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "No URL provided"}), 400

    short_id = shortuuid.uuid()[:6]  # Generate short URL key
    redis_client.set(short_id, long_url)

    return jsonify({"short_url": f"http://localhost:5000/{short_id}"})

@app.route('/<short_id>')
def redirect_url(short_id):
    long_url = redis_client.get(short_id)
    
    if long_url:
        return redirect(long_url, code=302)
    return jsonify({"error": "URL not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
