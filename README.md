# Utcapp

An awesome REST boilerplate that uses Flask-RESTX (formerly Flask-RESTPlus).
It has the usual API features to get you started and off the ground,
it's also designed to be easily scalable and extendable.

I wrote this boilerplate because I found that a lot of Flask REST boilerplates are either
doing too much, is lacking, or it simply doesn't fit my needs.


# Features

* Full featured framework for fast, easy, and documented API with [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
* JSON Web Token Authentication with [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
* Swagger Documentation (Part of Flask-RESTX).
* Unit Testing.
* Database ORM with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* Database Migrations using [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate)
* Object serialization/deserialization with [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* Data validations with Marshmallow [Marshmallow](https://marshmallow.readthedocs.io/en/stable/quickstart.html#validation)

## Flask CLI help command output:
```sh
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  Provides commands from Flask, extensions, and the application. Loads the
  application defined in the FLASK_APP environment variable, or from a
  wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
  will enable debug mode.

    $ export FLASK_APP=utcapp.py
    $ export FLASK_ENV=development
    $ flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  db      Perform database migrations.
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.
  test    Run unit tests
```

# Pre-requisites

This boilerplate uses `SQLite` as its database, make sure you have it installed.
`Pipenv` is recommended to help manage the dependencies and virtualenv.

You can also use other DBs like `PostGreSQL`, make sure you have it setup and update your `DATABASE_URL` in your configs.
Read more at [Flask-SQLAlchemy's](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) documentations.

It uses [Black](https://github.com/psf/black) for code styling/formatting.

# Usage

## Notes

This version is intended as the starting point for student projects and has some extra bits.

- An "app" blueprint which provides a flask template based end point at index. Which at the moment just lists the other parts of the system (you probably wouldn't use this live)
- A "pwa" blueprint that just statically serves the content of a pwa folder out side of the project. It is currently rigged to use a clone of https://github.com/UTCSheffield/demo-progressive-web-app at the same level as this repo. In use this would be statically served from somewhere else. But this saves the hassle of running 2 servers.
- An "admin" section that quickly adds an admin interface for the models using `admin.add_view(ModelView(User, db.session))` etc.

By default the `/auth` route is used by the `auth` blueprint. This currently only really works the the api documentation try it yourself functionality.

The rest of the resources are found in `/api` (This is the docs route by default, this can be changed easily).

**Note**: Pipenv seems to have been becoming unmaintained or unsupported, so `virtualenv` is recommended to manage your packages and Python environment, hence why `requirements.txt` has been generated.

## Installing with Pipenv ???????
```sh
# Clone the repo
$ git clone https://github.com/X1Zeth2X/flask-restx-boilerplate.git

# Install packages with pipenv
$ pipenv install
```

## Running
Please specify your app's environment variables in a `.env` file, otherwise Flask CLI wouldn't find your app.

```sh
# .env file example
export FLASK_APP=utcapp

# configs: production, testing, development, and default (uses DevelopmentConfig)
export FLASK_CONFIG=development

# Another way of assigning environment variables is:
FLASK_APP=utcapp
FLASK_CONFIG=development

# Read more at https://github.com/theskumar/python-dotenv
```

```sh
# Enter the virtualenv
$ pipenv shell

# (Optional for development, recommended)
$ flask db init # Initializes a new SQLite database.
$ flask db migrate # Creates the changes for the database.
$ flask db upgrade # Apply the changes to the database.

# Run the app
$ flask run
```

Or windows

```bat
$ py -m flask db init --app utcapp # Initializes a new SQLite database.
$ py -m flask db migrate --app utcapp # Creates the changes for the database.
$ py -m flask db upgrade --app utcapp # Apply the changes to the database.

# Run the app
$ flask run --app utcapp
```


## Unit testing
Utcapp has already some unit tests written, we encourage adding more unit tests as you scale.

```sh
# Unit testing
$ flask test

# Run specific unit test(s)
$ flask test tests.test_auth_api tests.test_user_model ...
```
