# Project Management

##  DataBase:

1. Install Postgres database and a database inside the server.
2. Create .env-local file and add:

```
"DJANGO_SECRET_KEY="django-insecure-mbw2ns6tzht7pdf9be0_z_m&(o+yyinhy%40ou2$rgk6in@*)%"

POSTGRESS_NAME="socialmedia"
POSTGRESS_USER="postgres"
POSTGRESS_PASSWORD="vijaya"
POSTGRESS_HOST="localhost"
POSTGRESS_PORT=5432

EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
```

## Setup

- Create virtual environment using

- Activate the envirnoment

- Install local and base requeriements using

```
pip install -r requirements/base.txt
```

```
pip install -r requirements/local.txt
```

- Run migrations

```
python manage.py makemigrations
```

```
python manage.py migrate --run-syncdb
```

- Start the server
```
python manage.py runserver
```

## Note: To access admin portal:
      - localhost:8000/admin

## Pages:
	1. Login Page
	2. Signup Page
	3. Dashboard Page
		- This page shows the analytics data like charts, tables, bar graphs
	4. List of Scheduled Post Page
		- A table showing all scheduled posts
		- A buttom saying "Schedule Post"
	5. Schedule Post Page
		- This is a form
		- This page will allow user to add post content, time to be posted, allow the platform list
	
## Models:
	1. User
	2. PlatformAuth
		- user
		- platform
		- credentials
	3. SchedulePost
		- post_title
		- user
		- platform
		- created_at
		- post_content
		- image
	4. Platform
            - choices

## Apps:
	1. user
	2. analytics
	3. schedule

## References 
- https://appseed.us/
- https://github.com/cookiecutter/cookiecutter
