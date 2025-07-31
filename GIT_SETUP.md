# 🔧 Настройка Git

## Инициализация репозитория

```bash
# Инициализация Git
git init

# Добавление всех файлов
git add .

# Первый коммит
git commit -m "Initial commit: Telegram bot for Vercel"

# Добавление удаленного репозитория (замените на ваш URL)
git remote add origin https://github.com/yourusername/sn-bot-vercel.git

# Отправка в репозиторий
git push -u origin main
```

## Структура .gitignore

Файл `.gitignore` уже настроен для исключения:
- Python кэш файлов
- Виртуальных окружений
- Переменных окружения (.env)
- IDE файлов
- Логов и временных файлов

## Рекомендуемые ветки

```bash
# Основная ветка
main

# Ветка для разработки
develop

# Ветки для фич
feature/new-quiz
feature/survey-improvements
```

## Коммиты

Используйте префиксы для коммитов:
- `feat:` - новые функции
- `fix:` - исправления багов
- `docs:` - документация
- `refactor:` - рефакторинг
- `test:` - тесты

Примеры:
```bash
git commit -m "feat: add new quiz type"
git commit -m "fix: resolve webhook timeout issue"
git commit -m "docs: update README with deployment guide"
```

## Автоматический деплой

Для автоматического деплоя при пуше в main ветку:

1. Подключите репозиторий к Vercel
2. Настройте автоматический деплой в Vercel Dashboard
3. Каждый push в main будет автоматически деплоить изменения

## Переменные окружения

Не забудьте настроить переменные окружения в Vercel:
- `BOT_TOKEN`
- `ADMIN_ID` 
- `WEBHOOK_URL` 