from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = 'ips.log'

def get_real_ip():
    # Thứ tự ưu tiên header phổ biến
    return (request.headers.get('CF-Connecting-IP') or
            request.headers.get('X-Forwarded-For', '').split(',')[0].strip() or
            request.headers.get('X-Real-IP') or
            request.remote_addr)

@app.route('/')
def index():
    ip = get_real_ip()
    # Ghi log (tùy chọn)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.utcnow().isoformat()}  {ip}\n")
    return render_template('index.html', ip=ip)

# Health-check cho Render
@app.route('/health')
def health():
    return 'OK', 200