FROM python:3.10-bookworm
WORKDIR /app 
COPY . . 

RUN  pip install -r requirements.txt
CMD ["python", "test.py"]