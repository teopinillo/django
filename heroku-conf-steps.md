# Heroku Config #

 1. Update Pipfile.loc

    Run `pipenv lock` to generate teh appropriate `Pipfile.lock`

 2. Add a new `Procfile` file in the project root directory. This file tells *Heroku* how to run the remote server where our code will live
    
    `touch Procfile`

 3. Install Gunicorn. 

    In `Procfile` add the line:
    `web: gunicorn mb_project.wsgi --log-file -`

    Next install Gunicorn which we'll use in production while still using Django's internal server for local development use.
    `pipenv install gunicorn`

 4. Update settings.py

      `ALLOWED_HOSTS = ['*']`



 source:Django for Beginners. William S. Vincet


