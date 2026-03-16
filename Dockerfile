FROM python:3.11-slim

WORKDIR /sensordata

COPY requirements.txt .

# Python
ENV PYTHONDONTWRITEBYTECODE=1   
# allows for live logging, only way for debugging containers, otherwsie all logs are buffered or don't even appear if container crashes
ENV PYTHONUNBUFFERED=1  
ENV PYTHONFAULTHANDLER=1        

# Pip
ENV PIP_NO_CACHE_DIR=1          
ENV PIP_DISABLE_PIP_VERSION_CHECK=1  

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]