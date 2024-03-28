# Blog-Api

This app creates the Api endpoints for a weblog using Django-Rest-Framework.

## Installation

This app is developed using python 3.11.

After making venv, install the necessary packages using the command below:

```
pip install -r requirements.txt
```

## Usage

Copy `.env.sample` file and rename it to `.env`.

To generate the secret key, run the command below:

```
python -c "import secrets; print(secrets.token_urlsafe())"
```

Copy and paste this new value into the `.env` file under the variable `SECRET_KEY`.

Write the appropriate values for parameteres in `.env` file. For example:

```
DEBUG = True

SECRET_KEY = s4U.........

DATABASE_URL = sqlite:///db.sqlite3
```

