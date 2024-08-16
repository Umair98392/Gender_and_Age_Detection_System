FROM python:3.10

WORKDIR /fast-test

COPY ./requirements.txt /fast-test/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fast-test/requirements.txt

# 
COPY ./main.py /fast-test/

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]