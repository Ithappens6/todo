Here’s the revised version of your `README.md`:

```markdown
# Task Manager Backend

This is a Django-based backend for a Task Manager application, providing RESTful APIs for managing users, tasks, and tags. The project includes token-based authentication, task hierarchy management, and CRUD operations.

---

## Features

- User authentication (Registration and Login)
- CRUD operations for tasks and tags
- Token-based authentication using Django REST Framework (DRF)
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
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

### Step 1: Apply Migrations

Run the following commands to set up the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Create a Superuser (Optional)

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.

---

## Start the Development Server

Start the Django development server with:

```bash
python manage.py runserver
```

The server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Usage

### Access the Admin Panel

Log in to the admin panel at:
```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials you created earlier.

### Interact with APIs

- Use tools like Postman or cURL to test the APIs.
- The base URL for the APIs is:
  ```
  http://127.0.0.1:8000/api/
  ```

---

## Project Structure

```
project/
├── task_manager/          # Main Django app
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
```

### Key Changes:
1. **Simplified and clarified instructions** for setup and usage.
2. **Reformatted** for better readability.
3. Removed explicit API documentation since you requested that the focus should remain on installation and project setup.
4. Adjusted the virtual environment activation for clarity.

Let me know if further changes are needed! 😊
