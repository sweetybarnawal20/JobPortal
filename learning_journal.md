# Django Job Portal Learning Journal

---

# Day 1 - Project Setup
Date: 29 July 2026

## What I accomplished

- Created project folder
- Created virtual environment
- Activated virtual environment
- Installed Django
- Created Django project
- Ran development server
- Opened Django welcome page
- Initialized Git
- Created .gitignore
- Made my first Git commit

---

## Commands I learned

```bash
python -m venv venv (used to create virtual environment)

.\venv\Scripts\activate (Used to activete virtual environment)

pip install django (used to install Django)

django-admin startproject jobportal .(used to create project folder)

python manage.py runserver (Used to check whether Django project is started or not and also to open our project on browser)

git init (used for git initialization)

git status (used to see git status)

git add . git add = Tell Git which files should be included in the next commit./. = Add everything in the current folder except what's ignored by .gitignore

git commit -m "Initial Django project setup" (The -m lets you add a short message describing this snapshot.)
```
git log is used to see the author and all the info of the project.
## New concepts I learned

- What a virtual environment is
- Why we use Django projects
- What manage.py is
- What Git is
- What .gitignore is
- What a commit is

New concepts learned
-manage.py is the command center of a Django project.
-settings.py stores the global configuration for the project.
-BASE_DIR is the project's root path used to build file locations.
-INSTALLED_APPS tells Django which applications are part of the project.
-DEBUG=True is useful during development but should be turned off in production.
-SQLite is Django's default database and is suitable for development.

Django follows a request-response cycle.
urls.py maps URLs to views.
views.py contains the application logic.
render() returns an HTML template to the browser.
Templates are stored in the templates folder and configured through settings.py.

New concepts learned
A model is a blueprint for a database table.
Django models are written in Python.
makemigrations creates migration files (database change plans).
migrate applies those changes to the database.
A custom User model should be created before building authentication.
AUTH_USER_MODEL tells Django to use our custom User model.

---

## Problems I faced

- (Write any errors here)

---

## Questions for tomorrow

- What is manage.py?
- What is settings.py?
- What are Django apps?

# Day 2 - Project Setup
Date: 2026-07-30

✔ Built user registration functionality
✔ Customized Django registration form
✔ Learned Django Forms
✔ Learned UserCreationForm
✔ Learned AuthenticationForm
✔ Built login page
✔ Implemented login functionality
✔ Learned POST requests
✔ Understood why CSRF token is required
✔ Improved Bootstrap UI
✔ Fixed import and form errors
✔ Committed progress using Git

# Day 3 - Candidate Profile & Django Signals
Date: 2026-08-01

✔ Designed database architecture for the Job Portal
✔ Learned why User, CandidateProfile, and EmployerProfile should be separate models
✔ Understood database normalization and avoiding unnecessary NULL values
✔ Created the CandidateProfile model
✔ Learned OneToOneField relationship
✔ Learned on_delete=models.CASCADE
✔ Learned the purpose of blank=True and null=True
✔ Installed and configured Pillow for ImageField support
✔ Created and applied Django migrations
✔ Learned how makemigrations and migrate work internally
✔ Learned the purpose of Django Signals
✔ Created signals.py
✔ Learned post_save signal
✔ Learned @receiver decorator
✔ Implemented automatic CandidateProfile creation after user registration
✔ Learned the purpose of the created parameter in signals
✔ Registered models in Django Admin
✔ Verified automatic profile creation through the Admin Panel
✔ Committed progress using Git

# Day 4 - Employer Profile & Django Signals
Date:8/2/2026

✔ Created EmployerProfile model
✔ Learned why employers need a separate profile model
✔ Updated Django Signals to automatically create EmployerProfile
✔ Registered EmployerProfile in Django Admin
✔ Verified automatic EmployerProfile creation
✔ Learned how Django Admin helps verify database records
✔ Committed progress using Git