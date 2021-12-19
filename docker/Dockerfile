FROM python:2.7.16

RUN mkdir /app
WORKDIR /app
ADD app /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]