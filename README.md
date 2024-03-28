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
py -c "import secrets; print(secrets.token_urlsafe())"
```

Copy and paste this new value into the `.env` file under the variable `SECRET_KEY`.

Write the appropriate values for parameteres in `.env` file. For example:

```
DEBUG = True

SECRET_KEY = s4U.........

DATABASE_URL = sqlite:///db.sqlite3
```

Run the server:

```
py manage.py runserver
```

## Endpoints and Permissions

You can see all endpoints using swagger-ui in this url: `http://localhost:8000/api/schema/swagger-ui/`.

There are 4 types of endpoints: users, categories, posts, comments.

You have not access to any of these endpoints without authentication.

After authentication as a regular user, you only have access to posts and comments endpoints.

Only the admin user has access to all endpoints.

## Authentication Endpoints

`http://localhost:8000/api/dj-rest-auth/registration/`  =>  Register the new user.

`http://localhost:8000/api/dj-rest-auth/login/`  =>  Login the user and generate a token.

`http://localhost:8000/api/dj-rest-auth/logout/`  =>  Logout the user.

## Posts Endpoints

`http://localhost:8000/api/posts/`  => All posts which `is_active=True` with related authors and comments and categories using pagination.

`http://localhost:8000/api/posts/1`  => The post which `is_active=True` and `id=1` with related author and comments and category.

`http://localhost:8000/api/posts/?author=ali`  => The posts which `is_active=True` and `author_username=ali` with related comments and categories using pagination.

`http://localhost:8000/api/posts/?category=sport`  => The posts which `is_active=True` and `category=sport` with related authors and comments using pagination.

`http://localhost:8000/api/posts/?search=hello`  => The posts which `is_active=True` and the word `hello` exists in their title or body with related authors and comments and categories using pagination.

## Permissions for Posts Endpoints

In the `http://localhost:8000/api/posts/` endpoint, all logged-in users can create a new post; and the author of the new post would be the username of the current logged-in user. The new post would not be displayed until the admin user activates it in the admin panel.

In the `http://localhost:8000/api/posts/1` endpoint, only the logged-in author of this post can update or delete it. Other users can only read this post. Only the category, title, and body of the post can be updated by the logged-in author.

## Comments Endpoints

`http://localhost:8000/api/comments/`  => All comments which `is_active=True` with related authors and posts using pagination.

`http://localhost:8000/api/comments/1`  => The comment which `is_active=True` and `id=1` with related author and post.

`http://localhost:8000/api/comments/?author=ali`  => The comments which `is_active=True` and `author_username=ali` with related post using pagination.

`http://localhost:8000/api/comments/?post=1`  => The comments which `is_active=True` and `post_id=1` with related authors and post using pagination.

`http://localhost:8000/api/comments/?search=hello`  => The comments which `is_active=True` and the word `hello` exists in their title with related authors and posts using pagination.

## Permissions for Comments Endpoints

In the `http://localhost:8000/api/comments/` endpoint, all logged-in users can create a new comment; and the author of the new comment would be the username of the current logged-in user. The new comment would not be displayed until the admin user activates it in the admin panel.

In the `http://localhost:8000/api/comments/1` endpoint, only the logged-in author of this comment can update or delete it. Other users can only read this comment. Only the title and body of the comment can be updated by the logged-in author.

## Categories Endpoints

`http://localhost:8000/api/categories/`  => All categories which `is_active=True` with related posts using pagination.

`http://localhost:8000/api/categories/1`  => The category which `is_active=True` and `id=1` with related posts.

`http://localhost:8000/api/categories/?search=hello`  => The categories which `is_active=True` and the word `hello` exists in their title with related posts using pagination.

## Permissions for Categories Endpoints

Only the admin user has access to categories endpoints.

In the `http://localhost:8000/api/categories/` endpoint, Only the admin user can create a new category. The new category would not be displayed until the admin user activates it in the admin panel.

In the `http://localhost:8000/api/categories/1` endpoint, only the logged-in admin user can update or delete this category. Only the title and body of the category can be updated by the logged-in admin user.

## Users Endpoints

`http://localhost:8000/api/users/`  => All users using pagination.

`http://localhost:8000/api/users/1`  => The user which `id=1`.

## Permissions for Users Endpoints

Only the admin user has access to users endpoints.

