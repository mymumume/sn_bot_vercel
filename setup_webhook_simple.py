import requests

# Ваш токен бота
BOT_TOKEN = "7798045497:AAEx_wh2Jr5eOFqP0605en8ypaGf7p6_BOs"
WEBHOOK_URL = "https://snbotvercel.vercel.app/api/webhook"

# Настройка webhook
def setup_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
    data = {"url": WEBHOOK_URL}
    
    response = requests.post(url, json=data)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.text}")
    
    # Проверка статуса
    info_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo"
    info_response = requests.get(info_url)
    print(f"\nСтатус webhook: {info_response.json()}")

if __name__ == "__main__":
    setup_webhook() 