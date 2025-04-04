FROM python:3.12-alpine AS builder

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install gunicorn


FROM python:3.12-alpine

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app

COPY . .

ENV DJANGO_DEBUG=False

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]
