FROM ubuntu:latest

RUN apt-get update && \ 
apt-get install -y python-pip python-dev build-essential

COPY requirements.txt /usr/src/app/
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python create_db.py

EXPOSE 5000
CMD ["python", "run.py"]