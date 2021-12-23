# BlogApplication

```
This is a simple blog application.
In which we can add articles, see the detail view of them.
We can filter the articles by tags by selecting the checkboxes.
On admin panel the we have rich text field for adding content in article,
and admin can also filter them by tags.
```

## Setup
```
1. git clone https://github.com/dipakdkumar92/BlogApplication.git
2. create a virtual environment and activate it.
3. pip install -r requirements.txt
4. check example.env for adding environment variables
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
```

## Check working
 ```
 1. create a superuser
 2. add tags from admin panel
 3. Add articles from Create Article button on index page.
 ```