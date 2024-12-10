# Устанавливаем базовый образ с Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY ./app/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Копируем все файлы из локальной директории в контейнер
COPY ./app .

# Указываем порт, который будет использовать приложение внутри контейнера
EXPOSE 3100

# Устанавливаем команду запуска для Gunicorn
CMD ["gunicorn", "main:app", "-c", "gunicorn.conf.py"]