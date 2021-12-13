FROM python:3.8
WORKDIR /usr/src/app
COPY requirements.txt .
COPY service.py .
RUN pip install -r requirements.txt
RUN echo "America/Bogota" > /etc/timezone

EXPOSE 5050

CMD ["python", "service.py"]