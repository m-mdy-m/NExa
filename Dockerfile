FROM python:3.11-slim
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y build-essential
RUN pip install --upgrade pip
RUN pip install .  
ENTRYPOINT ["nexa"]
CMD ["nexa"]
