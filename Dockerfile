FROM python:3.14

WORKDIR /app

COPY requriements.txt .

RUN pip install --no-cache-dir -r requriements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["python", "app.py"]