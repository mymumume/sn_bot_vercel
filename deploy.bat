@echo off
echo 🚀 Деплой бота на Vercel...

echo 📦 Проверка зависимостей...
if not exist "requirements.txt" (
    echo ❌ Файл requirements.txt не найден!
    pause
    exit /b 1
)

echo 🔧 Проверка конфигурации...
if not exist "vercel.json" (
    echo ❌ Файл vercel.json не найден!
    pause
    exit /b 1
)

echo 📤 Деплой на Vercel...
vercel --prod

if %errorlevel% equ 0 (
    echo ✅ Деплой успешно завершен!
    echo.
    echo 📋 Следующие шаги:
    echo 1. Настройте переменные окружения в Vercel Dashboard
    echo 2. Запустите: python setup_webhook.py
    echo 3. Протестируйте бота командой /start
) else (
    echo ❌ Ошибка при деплое!
)

pause 