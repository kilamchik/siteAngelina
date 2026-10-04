from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Дозволяє сайту стукати на локальний сервер

# Дані твого Telegram-бота
TOKEN = "7951655114:AAHvqXXRAv-jWbxOpljPTh-uAQy2Pi2ZdfM"
CHAT_ID = "706354958"  # Сюди прийде повідомлення

@app.route('/send-alert', methods=['POST'])
def send_alert():
    data = request.json
    location = data.get('location', 'Невідоме місце')
    
    # Текст повідомлення тобі в телеграм
    text = f"🚨 Ура, Владе! Вона погодилася на побачення! 🥰\n📍 Обрана локація: {location}"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)