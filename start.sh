#!/bin/bash

# Создаем виртуальное окружение
python3 -m venv venv

# Активируем виртуальное окружение
source venv/bin/activate

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем приложение
uvicorn app:app --host 0.0.0.0 --port 10000