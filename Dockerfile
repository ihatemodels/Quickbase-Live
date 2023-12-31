FROM python:3.11.5-slim
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./src /app/
EXPOSE 8080
ENTRYPOINT ["python", "main.py"]