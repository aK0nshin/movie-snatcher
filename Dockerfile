FROM python:3.11.0-slim
WORKDIR movie-snatcher
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl build-essential
RUN set -ex && pip3 install pip --upgrade
RUN pip install poetry
COPY . ./
COPY /db/*.sql /docker-entrypoint-initdb.d/
RUN poetry config virtualenvs.create false
RUN poetry install --only main
EXPOSE 5000
CMD ["poetry", "run", "python", "-m", "flask", "run"]
