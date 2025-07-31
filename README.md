# Telegram Bot для Vercel

Этот бот переписан для работы на Vercel с использованием webhook вместо polling.

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
# Установите Vercel CLI
npm i -g vercel

# Войдите в аккаунт Vercel
vercel login
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корне проекта:
```env
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_admin_user_id
WEBHOOK_URL=https://your-app-name.vercel.app/api/webhook
```

### 3. Деплой

```bash
# Автоматический деплой
deploy.bat

# Или вручную
vercel --prod
```

### 4. Настройка webhook

После деплоя настройте webhook:
```bash
python setup_webhook.py
```

## 📁 Структура проекта

```
├── api/
│   └── webhook.py          # Основной API файл для Vercel
├── handlers/               # Обработчики команд и сообщений
├── logic/                  # Логика состояния и бизнес-логика
├── questions/              # Вопросы для опросов и квизов
├── vercel.json            # Конфигурация Vercel
├── requirements.txt       # Зависимости Python
├── setup_webhook.py      # Скрипт настройки webhook
├── test_webhook.py       # Тестирование webhook
└── deploy.bat            # Автоматический деплой
```

## ⚙️ Настройка переменных окружения в Vercel

После деплоя настройте переменные окружения в Vercel Dashboard:

1. Перейдите в [Vercel Dashboard](https://vercel.com/dashboard)
2. Выберите ваш проект
3. Перейдите в Settings → Environment Variables
4. Добавьте переменные:
   - `BOT_TOKEN` - токен вашего Telegram бота
   - `ADMIN_ID` - ID администратора
   - `WEBHOOK_URL` - URL вашего webhook (например: `https://your-app.vercel.app/api/webhook`)

## 🔧 Настройка webhook

### Автоматически
```bash
python setup_webhook.py
```

### Вручную
```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://your-app.vercel.app/api/webhook"}'
```

## 🧪 Тестирование

### Локальное тестирование
```bash
python test_webhook.py
```

### Проверка статуса webhook
```bash
curl "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo"
```

## 📊 Мониторинг

- **Логи**: Vercel Dashboard → Functions → webhook
- **Статус**: `https://api.telegram.org/bot<TOKEN>/getWebhookInfo`
- **Метрики**: Vercel Dashboard → Analytics

## 🔍 Устранение неполадок

### Проблема: Webhook не работает
**Решение:**
1. Проверьте переменные окружения в Vercel
2. Убедитесь, что webhook URL правильный
3. Проверьте логи в Vercel Dashboard

### Проблема: Ошибки 500
**Решение:**
1. Проверьте логи в Vercel Dashboard
2. Убедитесь, что все зависимости установлены
3. Проверьте синтаксис кода

### Проблема: Бот не отвечает
**Решение:**
1. Проверьте статус webhook: `https://api.telegram.org/bot<TOKEN>/getWebhookInfo`
2. Убедитесь, что webhook правильно настроен
3. Проверьте переменные окружения

## ⚡ Особенности Vercel

- **Холодный старт**: первое обращение может занять несколько секунд
- **Таймаут**: функции имеют ограничение по времени выполнения (10 секунд)
- **Переменные окружения**: настройте их в Vercel Dashboard
- **Логи**: доступны в реальном времени в Dashboard
- **Масштабирование**: автоматическое масштабирование

## 🎯 Функционал бота

### Основные возможности:
1. **Главное меню** с кнопками для опроса, квиза и ссылок
2. **Опрос** - 8 вопросов с текстовыми ответами для сбора предпочтений клиентов
3. **Квиз "Love Story"** - 5 вопросов для определения стиля съемки с результатами и скидками
4. **Сбор контактов** - имя и телефон пользователя
5. **Уведомления администратора** о новых лидах
6. **Согласие на ПД** и рассылку
7. **Отложенные результаты** через 25 часов

### Архитектура:
- **Webhook** для работы на Vercel
- **State Manager** для управления состояниями пользователей
- **Модульная структура** с разделением логики и обработчиков
- **Асинхронная обработка** сообщений

## 📝 Команды для разработки

```bash
# Тестирование webhook
python test_webhook.py

# Настройка webhook
python setup_webhook.py

# Деплой на Vercel
vercel --prod
```

## 🆘 Поддержка

Если возникли проблемы:
1. Проверьте логи в Vercel Dashboard
2. Убедитесь, что все переменные окружения настроены
3. Проверьте статус webhook через Telegram Bot API 