# Task Manager Backend

This is a Django-based backend for a Task Manager application, providing RESTful APIs for managing users, tasks, and tags. The project includes token-based authentication, task hierarchy management, and CRUD operations.

## Features

- User authentication (Registration and Login)
- CRUD operations for tasks and tags
- Token-based authentication using DRF (Django Rest Framework)
- Parent-child relationships for tasks
- Filtering and pagination for task listing

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. **Python**: Version 3.10 or later
2. **Git**: To clone the repository
3. **Virtual Environment Tool**: Optional but recommended (e.g., `venv`)

---

## Installation Steps

### Step 1: Clone the Repository

```bash
# Clone the repository from GitHub
git clone https://github.com/your-username/task-manager-backend.git
cd task-manager-backend
```

### Step 2: Set Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv todo_venv

# Activate the virtual environment
# On Windows:
todo_venv\Scripts\activate
# On macOS/Linux:
source todo_venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Database

By default, the project uses SQLite as the database. If you wish to use another database (e.g., PostgreSQL), update the `DATABASES` setting in `task_manager/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 5: Run Migrations

Apply database migrations to set up the required tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser (Optional)

Create an admin user to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.

### Step 7: Start the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## API Endpoints

### Base URL

```
http://127.0.0.1:8000/api/
```

### Authentication

1. **Register User**
   - `POST /register/`
   - Payload:
     ```json
     {
       "username": "new_user",
       "password": "password123"
     }
     ```

2. **Login User**
   - `POST /login/`
   - Payload:
     ```json
     {
       "username": "new_user",
       "password": "password123"
     }
     ```
   - Response:
     ```json
     {
       "token": "your_auth_token"
     }
     ```

### Tasks

1. **List Tasks**
   - `GET /tasks/`
   - Headers:
     ```json
     {
       "Authorization": "Token your_auth_token"
     }
     ```

2. **Create Task**
   - `POST /tasks/`
   - Payload:
     ```json
     {
       "title": "New Task",
       "description": "Task description",
       "status": "Pending",
       "due_date": "2024-12-31T23:59:59Z"
     }
     ```

3. **Task Details**
   - `GET /tasks/:id/`

4. **Update Task**
   - `PATCH /tasks/:id/`

5. **Delete Task**
   - `DELETE /tasks/:id/`

6. **View Task Tree**
   - `GET /tasks/:id/tree/`

### Tags

1. **List Tags**
   - `GET /tags/`

2. **Create Tag**
   - `POST /tags/`
   - Payload:
     ```json
     {
       "name": "New Tag"
     }
     ```

---

## Testing the APIs

1. **Using Postman**:
   - Import the provided Postman collection.
   - Replace the `{{base_url}}` and `{{auth_token}}` variables as needed.

2. **Using cURL**:
   Example to list tasks:
   ```bash
   curl -X GET http://127.0.0.1:8000/api/tasks/ \
   -H "Authorization: Token your_auth_token"
   ```

---

## Project Structure

```
project/
├── task_manager/          # Django app
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── static/            # Static files (CSS, JS, etc.)
│   ├── views.py           # Views for handling requests
│   ├── models.py          # Database models
│   ├── serializers.py     # API serializers
│   ├── urls.py            # URL routing
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .gitignore             # Files to ignore in Git
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contribution

Feel free to fork this repository and submit pull requests for improvements or new features!

