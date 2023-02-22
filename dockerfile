FROM python:3.8-slim-buster

WORKDIR /

CMD ["cd", "/src"]

COPY src/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py"]

EXPOSE 5050