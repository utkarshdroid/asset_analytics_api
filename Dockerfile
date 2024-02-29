FROM python:3.9

RUN apt-get -y update && apt-get install -y freetds-dev

WORKDIR /app

COPY requirements.txt .

# Mount the ssh for use with pip install
RUN --mount=type=ssh pip install --prefer-binary --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
