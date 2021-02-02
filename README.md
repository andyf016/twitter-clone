# Django Twitter Clone
This is a simple messaging application, similar Twitter. Users can sign in, create posts, "like" posts, and follow other users. This application is written with Python using the Django framework.

## To run
After cloning the repo, open a terminal in the project's directory and run the following commands to install and activate the virtual environment. 
```bash
poetry install
poetry shell
```
Create a super user:
```bash
python manage.py createsuperuser
```
Push changes to the sql server:
```bash
python manage.py makemigrations
python manage.py migrate
```
Finally run the server
```bash
python manage.py runserver
```

Log in the the superuser account or create a new user.