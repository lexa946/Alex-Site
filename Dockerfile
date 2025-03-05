FROM python:3.12-slim

COPY mainapp ./mainapp
COPY requirements.txt requirements.txt
COPY *.py ./

RUN pip install -r requirements.txt

CMD ["uvicorn", "mainapp.app:app", "--host", "0.0.0.0", "--port", "80"]