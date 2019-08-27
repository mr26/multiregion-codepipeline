FROM python:2.7-slim

RUN pip install gunicorn flask

EXPOSE 8000

COPY api.py /

ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":8000", "api:app"]
