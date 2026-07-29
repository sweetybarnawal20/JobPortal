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

---

## Problems I faced

- (Write any errors here)

---

## Questions for tomorrow

- What is manage.py?
- What is settings.py?
- What are Django apps?