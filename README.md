# Real Time Messaging and File Sharing API
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

[![Directory docs](img/director.png)](https://github.com/Sagor0078/Real-Time-Messaging-and-File-Shareing-API)

## Software Design Patterns

The provided codebase for the Real-Time Messaging and File Sharing API follows several software design patterns commonly used in Django projects. Here are the key design patterns:

1. **Model-View-Template (MVT) Pattern**
   Django follows the MVT design pattern, which is a variation of the Model-View-Controller (MVC) pattern. The components are:
   - **Model**: Represents the data structure and database schema. Defined in `models.py` files.
   - **View**: Handles the business logic and interacts with the model to fetch or update data. Defined in `views.py` files.
   - **Template**: Defines the presentation layer. Although not explicitly shown in the provided code, templates are typically HTML files used to render the data.

2. **Modular Pattern**
   The project is organized into multiple applications (`users`, `chat`, `groups`), each responsible for a specific functionality. This modular approach promotes separation of concerns and makes the codebase more maintainable.

3. **Singleton Pattern**
   Django settings (`settings.py`) follow the Singleton pattern, ensuring that there is only one instance of the configuration throughout the application.

4. **Factory Pattern**
   Django's ORM uses the Factory pattern to create instances of models. For example, when you call `Model.objects.create()`, Django uses a factory method to instantiate and save the model.

5. **Middleware Pattern**
   Django's middleware system follows the Middleware pattern, allowing you to process requests and responses globally before they reach the view or after they leave the view.

6. **Observer Pattern**
   Django signals (not shown in the provided code) follow the Observer pattern, allowing certain actions to trigger notifications to other parts of the application.