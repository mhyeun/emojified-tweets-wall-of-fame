# Emojified Tweets Wall of Fame

A Django application that allows users to emojify tweets via our `twitter-emojify-api`, submit the results, and vote/comment on the funniest submissions.

## Setting up locally

#### Setting up virtual environment

Prior to starting, ensure you are on `Python3` and that you have `pip` installed.

##### For Windows

Run the following commands to create a virtual environment called 'venv':

```sh
$ python -m venv venv
$ venv\Scripts\activate.bat
```

##### For Mac

Run the following commands to create a virtual environment called 'venv':

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

##### For both

_You should see (venv) at the left of the shell prompt if done correctly._

To stop the virtual environment, simply run:

```sh
$ deactivate
```

#### Installing packages

To install the required packages, run:

```sh
$ pip install -r requirements.txt
```

To set up the pre-commit hooks, install the packages as shown above then run:

```sh
$ pre-commit install
```

#### Making migrations

If you made changes to any schemas or added any new tables, make sure to create migration files with:

```sh
$ python manage.py makemigrations
```

#### Running the app

To run migrations, run:

```sh
$ python manage.py migrate
```

To start the Django app, run:

```sh
$ python manage.py runserver
```
