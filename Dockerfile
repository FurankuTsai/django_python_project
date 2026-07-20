FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 安裝 mysqlclient 編譯需要的套件
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*


# 複製 requirements.txt
COPY requirements.txt .

# 升級 pip 並安裝套件
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案程式碼
COPY src/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]