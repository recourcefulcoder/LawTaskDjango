![tests](https://github.com/recourcefulcoder/LawTaskDjango/actions/workflows/test.yaml/badge.svg)

# LawTaskDjango

This project implements backend API for law reference website; 
it parses data (documents) from [this website]() and stores them in the database, giving
out on request

Table of contents:
-
- [API documentation](#api-docs)
- [Launching project instructions](#running-application-instructions)
  - [With Docker Compose](#docker-compose) (preferred)
  - [Manually](#manual-startup)
- [Code documentation](#code-documentation)
  - [Code style conventions](#code-style-conventions)  
  - [Environment variables](#environment-variables)

## API docs

## Running application instructions

### Docker Compose
1. Create .env file in the root directory of the project ( /lawproject ) and define 
[environment variables](#environment-variables) needed for running an app
2. Run docker containers with 

```bash
docker compose up --build -d
```

> [!NOTE]
> application is run on port 8000. If you want to change this behaviour, adjust port 
> mapping in Docker Compose 

To stop an application, simply run
```bash
docker compose down
```

### Manual startup
Not defined yet

## Code documentation
### Code style conventions
Code must meet basic PEP8 style requirements + some additional ones. <br> 
Code is considered to be properly formatted when it passes check of [flake8](https://pypi.org/project/flake8/) 
linting tool with given plugins:

- [flake8-import-order](https://pypi.org/project/flake8-import-order/)
- [flake8-print](https://pypi.org/project/flake8-print/)

### Environment variables

| Variable | Value |
| -------- | ----- |
| DJANGO_DEBUG | defines whether django application should be run in default mode; <br> set to _True_ for debug mode <br> considered to be _False_ by default |
| DJANGO_SECRET_KEY | secret key, used for internal django's security operations (hashing, etc.) |
| DJANGO_APPLICATION_PORT | defines which port service's docker container expose; <br> defaults to 8000 |
|||
| POSTGRES_USER | declares user of postgres DB (only in dev mode; in Docker Compose name 'postgres' is set explicitly) |
| POSTGRES_PASSWORD | declares password for postgres user |
| POSTGRES_DB | declares name of the DB used |
| DB_HOST | declares host which database is running on; <br> considered to be _localhost_ by default |
| DB_PORT | port database is running on; considered to be [5432](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-PORT) by default|
