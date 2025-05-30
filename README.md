# backend
## backend repo made with FastAPI connected to a PostgreSQL relational DB

This document provides instructions for setting up, running, and developing this FastAPI project.

## 1. Installation and Setup

### Virtual Environment

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

2.  **Activate the virtual environment:**

    ```bash
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Uvicorn and Reloading

To run the application with automatic reloading on code changes, use:

```bash
uvicorn main:app --reload

```

Environment Variables (.env)
Create a .env file and a alembic.ini in the root directory of your project.

Add your database URL (ALSO IN THE ALEMBIC.INI):


```bash
DATABASE_URL=postgresql://user:password@host:port/database_name

```

## Migrating the Database

create the migration

```bash
alembic revision --autogenerate -m "Migration description"
```

apply it 

```bash
alembic upgrade head
```

