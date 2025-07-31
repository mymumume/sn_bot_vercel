# 🚀 Быстрый старт

## 1. Подготовка

1. **Установите Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Войдите в аккаунт Vercel:**
   ```bash
   vercel login
   ```

## 2. Настройка переменных

Создайте файл `.env` в корне проекта:
```env
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_admin_user_id
WEBHOOK_URL=https://your-app-name.vercel.app/api/webhook
```

## 3. Деплой

```bash
vercel --prod
```

## 4. Настройка webhook

После деплоя:
```bash
python setup_webhook.py
```

## 5. Проверка

Отправьте `/start` вашему боту в Telegram!

## 🔧 Переменные окружения в Vercel

После деплоя настройте в Vercel Dashboard:
- `BOT_TOKEN` - токен бота
- `ADMIN_ID` - ID администратора  
- `WEBHOOK_URL` - URL вашего webhook

## 🆘 Проблемы?

1. Проверьте логи в Vercel Dashboard
2. Убедитесь, что переменные настроены
3. Проверьте статус webhook: `https://api.telegram.org/bot<TOKEN>/getWebhookInfo` 