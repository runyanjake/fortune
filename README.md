# fortune
A super simple Django site recreating the unix fortune command using an LLM as an infinite fortune creator. (https://en.wikipedia.org/wiki/Fortune_(Unix))

Uses https://pypi.org/project/chatgptpy/ to communicate with a locally hosted LLM server or LLM server on the local network that uses the OpenAI api format. (Requires Python 3.9.x or newer.)

## First Time Setup

`sudo apt-get install python3.11`
`sudo apt install python3.11-venv`
`python3.11 -m venv env`
`source env/bin/activate`
`pip install django`
`pip install chatgptpy`
`django-admin startproject fortune`
`cd fortune && python manage.py migrate`

Add to fortune/settings.py:
`APPEND_SLASH=True`
`DEBUG=False` if prod, `DEBUG=True` if dev.
```
ALLOWED_HOSTS=[
    '127.0.0.1',
    'fortune.whitney.rip'
]
```

Visible at `http://127.0.0.1:8000`

## Development 

`python manage.py migrate && python manage.py runserver`

## Deployment via Docker

`docker-compose build && docker-compose up -d && docker logs -f fortune`

