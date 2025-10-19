# ToDoList Application

A simple, elegant Django-based Todo List application that helps you manage your daily tasks efficiently.

## Features

- User authentication (register, login, logout)
- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete
- Add images to tasks
- Set due dates for tasks
- User profile settings

## Technologies Used

- Django 5.2
- SQLite database
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository
```
git clone <repository-url>
cd ToDoList
```

2. Create a virtual environment and activate it
```
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up your environment
```
# Copy the settings template
cp ToDoList/settings_template.py ToDoList/settings.py

# Edit settings.py and update:
# - SECRET_KEY with a secure key
# - DEBUG = True for development
# - Any other environment-specific settings
```

5. Run migrations
```
python manage.py migrate
```

6. Start the development server
```
python manage.py runserver
```

7. Access the application at http://127.0.0.1:8000/

## Usage

1. Register a new account or login with existing credentials
2. Add new tasks with optional images and due dates
3. Mark tasks as complete when finished
4. Edit or delete tasks as needed
5. Update your profile settings

## GitHub Setup

1. Initialize a Git repository
```
git init
```

2. Add your files (the .gitignore will prevent sensitive data from being included)
```
git add .
```

3. Commit your changes
```
git commit -m "Initial commit"
```

4. Create a new repository on GitHub

5. Link your local repository to GitHub
```
git remote add origin https://github.com/yourusername/ToDoList.git
```

6. Push your code to GitHub
```
git push -u origin main
```

## Project Structure

- `accounts/` - User authentication and profile management
- `todo/` - Core todo list functionality
- `static/` - CSS, JavaScript, and other static files
- `template/` - HTML templates
- `media/` - User-uploaded files

## License

This project is open-source and available under the MIT License.