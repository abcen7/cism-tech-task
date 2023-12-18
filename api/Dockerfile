FROM python:3.10

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]