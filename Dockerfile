FROM python:3-alpine AS production

WORKDIR /srv

ENV PYTHONUNBUFFERED=1

CMD [ "/usr/local/bin/uvicorn", "--host", "0.0.0.0", "cantina.core.asgi:application" ]

COPY ./requirements.txt /srv/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./cantina /srv/cantina
