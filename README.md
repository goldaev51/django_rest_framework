# django_rest_framework

## Task

Implemented in the project:
* at least 2 models with links (Post, Comment)
* Post models and comments should benefit (FK link)
* Serializers for Models
* CRUD, which uses a set of views to work, is not used in such a way that:
  1. messages and comments could be anything
  2. adding posts and comments
  3. modified or deleted posts or comments that can only be accessed by their owners (when deleting a post, all comments are deleted regardless of their owners - on_delete=Cascade)

## Launch

* Clone current repo
* Run in terminal './manage.py makemigrations'
* Run in terminal './manage.py migrate'
* Create superuser
* Launch in terminal './manage.py runserver'
* Test logic by url http://127.0.0.1:8000/api/


## Realised

* Created CRUD for models Posts and Comments
* Authorised users can create posts and comments
* Owners can change their posts and comments
* Added token auth http://127.0.0.1:8000/api/dj-rest-auth/login/
