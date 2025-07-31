import os
import requests
import json
from dotenv import load_dotenv

def test_webhook():
    """Тестирует webhook бота."""
    load_dotenv()
    
    webhook_url = os.getenv("WEBHOOK_URL")
    if not webhook_url:
        print("Ошибка: WEBHOOK_URL не задан в .env файле")
        return
    
    # Тестовое сообщение
    test_update = {
        "update_id": 123456789,
        "message": {
            "message_id": 1,
            "from": {
                "id": 123456789,
                "is_bot": False,
                "first_name": "Test",
                "username": "testuser"
            },
            "chat": {
                "id": 123456789,
                "first_name": "Test",
                "username": "testuser",
                "type": "private"
            },
            "date": 1234567890,
            "text": "/start"
        }
    }
    
    try:
        response = requests.post(webhook_url, json=test_update)
        print(f"Статус ответа: {response.status_code}")
        print(f"Тело ответа: {response.text}")
        
        if response.status_code == 200:
            print("✅ Webhook работает корректно")
        else:
            print("❌ Webhook вернул ошибку")
            
    except Exception as e:
        print(f"❌ Ошибка при тестировании webhook: {e}")

if __name__ == "__main__":
    test_webhook() 