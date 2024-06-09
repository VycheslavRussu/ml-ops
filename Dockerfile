# Используем официальный образ Python в качестве базового образа
FROM python:3.9-slim

# Обновляем pip до последней версии
RUN pip install --upgrade pip

# Копируем файлы приложения в контейнер
WORKDIR /app
COPY . /app

# Устанавливаем переменные окружения для секретов
ARG GPT_API_KEY
ARG FOLDER_ID
ARG API_OCR
ENV GPT_API_KEY=${GPT_API_KEY}
ENV FOLDER_ID=${FOLDER_ID}
ENV API_OCR=${API_OCR}

# Устанавливаем зависимости приложения
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для Streamlit
EXPOSE 8501

# Определяем команду запуска вашего Streamlit-приложения
CMD ["streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
