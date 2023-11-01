FROM python:3.8

WORKDIR /app

COPY app.py /app/app.py
COPY templates /app/templates
COPY server_power_control /app/server_power_control
COPY requirements.txt /app/requirements.txt

EXPOSE 5000
ENV ENV_FILE_PATH=/app/control.env

RUN pip install --no-cache-dir -r requirements.txt


CMD ["flask", "run", "--host=0.0.0.0"]



