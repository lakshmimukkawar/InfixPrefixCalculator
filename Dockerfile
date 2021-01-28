FROM python:3.7.9



RUN pip install pipenv

COPY /src /app/src
COPY /tests /app/tests
COPY setup.py Pipfile Pipfile.lock /app/
WORKDIR /app

RUN pipenv install --system --deploy
WORKDIR /app/src

ENTRYPOINT python main.py