# Django CMS Guide


## Installation.

1. First create a virtualenv and then install all the dependencies into the environment.

```shell script
# Environment File Created
virtualenv -p python3 env
# Install all the Python Dependencies
pip install -r requirements.txt
```

2. After Installation the dependencies, now create a django-cms project

```shell script
cd <project_name>
mkdir <project_name>
# creating django-cms using djangocms installer
djangocms -p . <project_name>
```

3. There are two views in django
- Structure 
- Content

_Content show you a preview of what the page will look like in the page_
_Structure show all the places where you can edit edit_


4. Create a new apps for django doner shop
```shell script
python manage.py startapp doner_shop
```

5. Apphooks in DjangoCMS
```shell script
python manage.py start app blogs
```




### Some Key points for Template Design in Django CMS

- You’ll also see `{% load cms_tags %}` in that file - `cms_tags` is the required template tag library.

Now in Django CMS there are two types of placeholder.

1. Static Placeholder 
 - To add a placeholder you need to add following codes
 ```html
 <footer>
       {% static_placeholder 'footer' %}
 </footer>
```
 If you add this placeholder in the base.html file, it will appear in every pages in django templates
 

### Issue Section

1. One update is _staticfiles_ is changes to `static` to locate css file in template files.
