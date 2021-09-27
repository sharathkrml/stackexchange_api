# StackExchange API with caching

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/sharathkrml/stackexchange_api
$ cd stackexchange_api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py createcachetable
(venv)$ python manage.py runserver
```
