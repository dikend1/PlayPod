# Используем официальный образ Python как базовый
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    tk \
    libx11-dev \
    libxext-dev \
    libxrender-dev \
    libxtst-dev \
    libfontconfig1 \
    libfreetype6 \
    libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь код приложения в контейнер
COPY . /app/

# Устанавливаем переменные окружения для Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=nfacplay.settings

# Пример безопасного способа передачи ключа, через .env файл
# ENV SECRET_KEY="${SECRET_KEY}"

# Открываем порт 8000 для доступа
EXPOSE 8000

# Команда для запуска Django сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "nfacplay.wsgi:application"]
