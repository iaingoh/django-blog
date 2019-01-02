# Django Blog

Documentation for a blog built in Django. It was built with Corey Schafer's instructions from his YouTube Django series for the intention of learning and experimenting. You can visit his series at https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p .

---

Project source can be downloaded from https://github.com/iaingoh/django-blog.git

---

## Author & Contributor List

Corey Schafer  
Iain Goh

---

## File List

```
.:
db.sqlite3
manage.py
README.md
./templates_corey_schafer
./testfeatures
./user_registration
./users
```
```
/testfeatures
__init__.py
settings.py
urls.py
wsgi.py
```
```
/templates_corey_schafer:
./migrations
./static
./templates
__init__.py
admin.py
apps.py
models.py
tests.py
urls.py
views.py
```
```
/user_registration
./migrations
./templates
__init.py
admin.py
apps.py
forms.py
models.py
tests.py
urls.py
views.py
```
```
/users
./migrations
./templates
__init.py
admin.py
apps.py
forms.py
models.py
signals.py
tests.py
views.py
```

## How to run file
Django, crispy forms, and pillow should already be installed to run this project. If not, you may do so via either pipenv or pip via the following commands:
```
pipenv install django
pipenv install django-crispy-forms
pipenv install Pillow
```

Find the project parent directory, and locate manage.py .
Run python manage.py runserver

With the localhost address, paste it into the browser's address bar and from there you will be redirected to the project's home page.

---

## Project's URL routes run on the development server

```
http://localhost/admin/
http://localhost/
http://localhost/register/
http://localhost/profile/
http://localhost/login/
http://localhost/logout/
```