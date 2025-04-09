![tests](https://github.com/recourcefulcoder/LawTaskDjango/actions/workflows/test.yaml/badge.svg)

# LawTaskDjango

This project implements backend API for law reference website; 
it parses data (documents) from [this website]() and stores them in the database, giving
out on request

Table of contents:
-
- [API documentation](#api-docs)
- [Launching project instructions](#running-application-instructions)
  - [In production](#docker-compose) (with Docker Compose)
  - [In developer regime](#running-in-dev-mode)
- [Code documentation](#code-documentation)
  - [Code style conventions](#code-style-conventions)  
  - [Environment variables](#environment-variables)
  - [Database models description](#django-models)

## API docs

This application's API provides given methods:

1. get_documents_metadata (**NOT_IMPLEMENTED**)
- URL: /docs-meta
- method allowed: GET
- options: "category" (_optional_) - specifies category's name to get
- description: gives metadata (i.e. name, eoNumber, etc.) about documents specified with options

2. get_document_metadata
- URL: /doc-meta/<document-id>/
- method allowed: GET
- options: -
- description: Gives specific document's metadata based on it's id value

3. get_documents
- URL: /docs
- method allowed: GET
- options: "category" - specifies category's name to get
- description: gives out documents (as pdf files), which were specified with options

4. get_document
- URL: /doc/<document-id>
- method allowed: GET
- options: -
- description: gives document (as pdf files), based on it's ID provided

5. get_category
- URL: /categories
- method allowed: GET
- options: parent (_optional_) - specifies name of category whose children are requested to vb seen; <br>
if omitted, gives out most high categories. If many "parent" options are provided, only last one is taken into account.
- description: Gives list of categories sharing same specified parent (or on the top of the hierarchy, if not provided) 
and their data - all database files, to be specific. JSON structure is following:

```json lines
[
  {
    id: <category-id>,
    name: <category-name>,
    type_id: <category-type-id>,
    block: <category-name>,
  }
]
```

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
> mapping in docker-compose.yaml

To stop an application, simply run
```bash
docker compose down
```

### Running in dev mode
1. setup PostgreSQL database
2. create .env file in ```/lawproject``` directory and fill it properly (see [here](#environment-variables))
3. create virtual environment and run it
```bash
python3 -m venv venv
source venv/bin/activate 
```
4. install project dependencies

```bash
pip install --upgrade pip
pip install requirements.txt
```
5. migrate database and fill it with document categories <br>
For that from ```/lawproject``` directory run
```bash
python manage.py migrate
python manage.py loaddata fixtures/categories.json
```

6. start a development server by running

```bash
python manage.py runserver
```

## Code documentation

> [!IMPORTANT]
> Hardcoded document types are loaded via fixture fixtures/hardcode.json

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
|||
| POSTGRES_USER | declares user of postgres DB (only in dev mode; in Docker Compose name 'postgres' is set explicitly) |
| POSTGRES_PASSWORD | declares password for postgres user |
| POSTGRES_DB | declares name of the DB used |
| DB_HOST | declares host which database is running on; <br> considered to be _localhost_ by default |
| DB_PORT | port database is running on; considered to be [5432](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-PORT) by default|

### Django models

Since project is written on django, tables are defined with django orm - being specific, with 
these two models: Category and Document 

#### Category model
Categories are hierarchically organised; this model is inherited from [MPTTModel](https://django-mptt.readthedocs.io/en/latest/models.html) 
of django-mptt library; on top of this model's attributes and methods, whose description you may find on the link higher,
following attributes are added:

- id
- name - name of the document category to be shown on frontend
- type_id - UUID of document type in government web service ([this one](http://publication.pravo.gov.ru/)) being parsed;
if set to NULL; this category doesn't correspond to any DocumentType on government API, yet is considered
parent category in this service.
- block - codename of the category to be used on [government API](http://publication.pravo.gov.ru/help) and this service's API;
<br><br>
If set to NULL, represents that this Category isn't bound to any specific in government API, yet is a part of 
internal service's hierarchical organisation of categories <br><br> 
- auto_updates - boolean field, defines whether this document type should be automatically parsed and 
updated within Celery task 
- parent - stores "block" value of parent's category 

#### Document model
Attributes:
- id
- name - document formal name, to be shown on frontend
- eoNumber - electronic publication number of the document ("номер электронного опубликования")
- category - Django's [ForeignKey](https://docs.djangoproject.com/en/5.2/ref/models/fields/#django.db.models.ForeignKey) 
field; relation to Category model; document's category
- file - Django's [FileField](https://docs.djangoproject.com/en/5.2/ref/models/fields/#filefield); 
actual file of the document