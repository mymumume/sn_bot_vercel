# 🎯 Запуск Telegram бота на Vercel

## ✅ Что уже готово

Создан полный функционал бота с:

### 🎯 Основные возможности:
- ✅ **Главное меню** с кнопками опроса и квиза
- ✅ **Опрос** - 8 вопросов с текстовыми ответами
- ✅ **Квиз "Love Story"** - 5 вопросов с результатами и скидками
- ✅ **Сбор контактов** - имя и телефон пользователя
- ✅ **Уведомления администратора** о новых лидах
- ✅ **Согласие на ПД** и рассылку
- ✅ **Webhook** для работы на Vercel

### 🏗️ Архитектура:
- ✅ **Модульная структура** с разделением логики
- ✅ **State Manager** для управления состояниями
- ✅ **Асинхронная обработка** сообщений
- ✅ **Конфигурация Vercel** готова

## 🚀 Быстрый запуск

### 1. Подготовка
```bash
# Установите Vercel CLI
npm i -g vercel

# Войдите в аккаунт Vercel
vercel login
```

### 2. Настройка переменных
Создайте файл `.env`:
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
```bash
python setup_webhook.py
```

### 5. Тестирование
Отправьте `/start` вашему боту в Telegram!

## 📁 Структура проекта

```
sn_bot_vercel/
├── api/
│   └── webhook.py          # Основной webhook для Vercel
├── handlers/               # Обработчики команд
│   ├── start.py           # Команда /start
│   ├── callbacks.py       # Callback кнопки
│   ├── quiz_handler.py    # Обработчик квиза
│   └── survey.py          # Обработчик опроса
├── logic/                  # Бизнес-логика
│   ├── state.py           # Менеджер состояний
│   └── quiz_logic.py      # Расчет результатов квиза
├── questions/              # Вопросы и ответы
│   ├── survey_questions.py # Вопросы опроса
│   └── quiz_lovestory.py  # Квиз Love Story
├── vercel.json            # Конфигурация Vercel
├── requirements.txt       # Зависимости Python
├── setup_webhook.py      # Настройка webhook
├── test_webhook.py       # Тестирование
├── deploy.bat            # Автоматический деплой
└── README.md             # Подробная документация
```

## 🔧 Настройка в Vercel Dashboard

После деплоя настройте переменные окружения:

1. Перейдите в [Vercel Dashboard](https://vercel.com/dashboard)
2. Выберите ваш проект
3. Settings → Environment Variables
4. Добавьте:
   - `BOT_TOKEN` - токен вашего Telegram бота
   - `ADMIN_ID` - ID администратора
   - `WEBHOOK_URL` - URL вашего webhook

## 🧪 Тестирование

### Проверка webhook:
```bash
python test_webhook.py
```

### Проверка статуса:
```bash
curl "https://api.telegram.org/bot<TOKEN>/getWebhookInfo"
```

## 📊 Мониторинг

- **Логи**: Vercel Dashboard → Functions → webhook
- **Метрики**: Vercel Dashboard → Analytics
- **Статус**: Проверьте webhook через Telegram API

## 🆘 Устранение проблем

### Бот не отвечает:
1. Проверьте переменные окружения в Vercel
2. Убедитесь, что webhook настроен: `python setup_webhook.py`
3. Проверьте логи в Vercel Dashboard

### Ошибки 500:
1. Проверьте синтаксис кода
2. Убедитесь, что все зависимости установлены
3. Проверьте переменные окружения

### Медленные ответы:
1. Это нормально для холодного старта
2. Последующие запросы будут быстрее

## 📚 Документация

- `README.md` - Подробная документация
- `QUICK_START.md` - Быстрый старт
- `MIGRATION_GUIDE.md` - Миграция с polling
- `GIT_SETUP.md` - Настройка Git

## 🎉 Готово!

Ваш бот готов к работе! Он включает весь функционал исходного проекта:

- ✅ Опросы для сбора предпочтений клиентов (текстовые ответы)
- ✅ Квизы с результатами и скидками
- ✅ Сбор контактов и уведомления администратора
- ✅ Согласие на ПД и рассылку
- ✅ Современная архитектура на Vercel

**Следующий шаг**: Настройте переменные окружения и запустите бота! 