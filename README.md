# Real Time Messaging and File Shareing API
This is a Django-based real-time messaging and file-sharing API. The project is dockerized and uses SQLite as the database.

## Prerequisites

- Docker

## Getting Started
## Build and Run the Docker Containers
Build the Docker containers:

```bash
docker-compose build
```
start the Docker containers:

```bash
docker-compose up
```

## Project Structure
.
├── messaging_api
│   ├── chat
│   │   ├── migrations
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── core
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── ...
│   ├── groups
│   │   ├── migrations
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── users
│   │   ├── migrations
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── ...
│   ├── manage.py
├── Dockerfile
└── [README.md]