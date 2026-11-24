from flask import Flask, jsonify
import os, time, random

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def home():
    return jsonify({
        "app": "auto-recover",
        "status": "running",
        "uptime_sec": round(time.time() - start_time, 2),
        "pod": os.getenv("HOSTNAME", "local")
    })

@app.route('/health')
def health():
    # 20% chance fail ani cheppi crash simulate chestam
    if random.random() < 0.2:
        return jsonify({"status": "FAIL"}), 500
    return jsonify({"status": "OK", "uptime": round(time.time() - start_time, 2)})

@app.route('/crash')
def crash():
    # Container ni crash cheyadaniki
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
