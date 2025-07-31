import os
import requests
from dotenv import load_dotenv

def setup_webhook():
    """Настраивает webhook для бота."""
    load_dotenv()
    
    bot_token = os.getenv("BOT_TOKEN")
    webhook_url = os.getenv("WEBHOOK_URL")
    
    if not bot_token or not webhook_url:
        print("Ошибка: BOT_TOKEN или WEBHOOK_URL не задан в .env файле")
        return
    
    # Удаляем старый webhook
    delete_url = f"https://api.telegram.org/bot{bot_token}/deleteWebhook"
    response = requests.post(delete_url)
    print(f"Удаление старого webhook: {response.status_code}")
    
    # Устанавливаем новый webhook
    set_url = f"https://api.telegram.org/bot{bot_token}/setWebhook"
    data = {"url": webhook_url}
    response = requests.post(set_url, json=data)
    
    if response.status_code == 200:
        print(f"✅ Webhook успешно настроен: {webhook_url}")
    else:
        print(f"❌ Ошибка настройки webhook: {response.text}")
    
    # Проверяем статус
    info_url = f"https://api.telegram.org/bot{bot_token}/getWebhookInfo"
    info_response = requests.get(info_url)
    if info_response.status_code == 200:
        info = info_response.json()
        print(f"Статус webhook: {info}")

if __name__ == "__main__":
    setup_webhook() 