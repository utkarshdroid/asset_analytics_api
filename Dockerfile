FROM python:3.9

RUN apt-get -y update && apt-get install -y freetds-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --prefer-binary --no-cache-dir --upgrade -r requirements.txt

RUN pip install pytest

COPY . .

RUN pytest 

ENV PYTHONPATH "${PYTHONPATH}:/app/"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
