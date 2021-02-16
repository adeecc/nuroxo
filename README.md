# API for Chat App for CS F407: AI Assignment

## Instructions for running the server:

1. Install the dependencies

```
pip install -r requirements.txt
```

2. Make and perform database Migrations

```
./manage.py makemigrations
./manage.py migrate
```

1. Run the server on port 8000:

```
./manage.py runserver
```

   - Note: if `./manage.py <command>` gives error, use `python <command>` or `python3 <command>` instead
