Tango With Django
===================

[How To Tango With Django 1.7](http://www.tangowithdjango.com/book17/)


	$ django-admin startproject twd
	$ python manage.py migrate
	$ python manage.py runserver 8001
	$ python manage.py startapp rango

add 'rango' into `settings.py:INSTALLED_APP`.

map the URL. Two parts:

- The project: `twd/urls.py`, `path('rango/', include('rango.urls'))`
- The app: `rango/urls.py`, e.g. `path('', views.index, name="index")`

    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        path('', views.index, name='index'),
    ]

- use `django.urls.reverse` map between name and URL.

Templates and Static Media
---------------------------

- django 1.7: `<workspace>/twd/templates/rango/`
- django 2.1: `<workspace>/twd/rango/templates/rango/` when `APP_DIRS=True` in `TEMPLATES` (settings.py)
- make sure `django.contrib.staticfiles` in `INSTALLED_APPS`, `STATIC_URL='/static/`, per-app static is `<workspace>/twd/rango/static/`
- add to `settings.py`

	STATICFILES_FINDERS = [
		'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	]
- set `STATIC_ROOT="/var/www/example.com/static/`, and `python manage.py collectstatic` to copy files to `STATIC_ROOT` (served by other webserver) needs more details on what the full URL will be

- `{% load static %}` and `{% load staticfiles %}` (the later knows external storage ? like Amazon S3 ?) they allow us to call static template tag as `{% static "rango/junk.html" %}`


Models
----------

- `category = models.ForeignKey(Category, on_delete=models.CASCADE)`
- no need `id` field, will be created by Django
- Create models then `python manage.py makemigrations`
- `python manage.py migrate`
- Whenever you add to existing models, you will have to repeat this process running python manage.py makemigrations <app_name>, and then python manage.py migrate
- `python manage.py shell`

		# Import the Category model from the Rango application
		>>> from rango.models import Category

		# Show all the current categories
		>>> print Category.objects.all()
		[] # Returns an empty list (no categories have been defined!)

		# Create a new category object, and save it to the database.
		>>> c = Category(name="Test")
		>>> c.save()

		# Now list all the category objects stored once more.
		>>> print Category.objects.all()
		[<Category: test>] # We now have a category called 'test' saved in the database!

		# Quit the Django shell.
		>>> quit()

- `c = Category.objects.get_or_create(name=name)[0]`
- add `class CateoryAdmin(admin.ModelAdmin)` into app/admin.py, and set `fields`, `list_display`.
- add `class CategoryInline(admin.StackedInline)`, `class CategoryInline(admin.TabularInline)` for `PageAdmin.inlines = [ CategoryInline ]`

