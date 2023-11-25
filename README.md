# robo-mission-control

Robo Mission Control is a Django-based backend designed to track missions and return result coordinates as a stream of data, utilizing Celery as a task queue to handle asynchronous processing..

## Setup

1. After cloning the repository, ensure the python environment is in sync using
   
   `>>pipenv sync`

   The project expects redis to be available on the sytem. We are also using django's default SQLite3 as database.
3. Once env is ready, change directory to app robomission and run make database ready.
   
    `>>make migrations`

    Incase the above doesn't works for you, go to roboapp `>>cd roboapp/` run `>>python manage.py makemigrations` and then `>>python manage.py migrate`.

4.  Now in the cmd run the project using

    `>>make run`

5. After this we will start our celery task queue:

   
   `>>make celeryworker`

6. The project uses a `.env` file for configuration, in its absence we use the default values. Here are the available options:

      `PORT=browser_port`
      
      `REDIS_HOST=localhost`
      
      `REDIST_PORT=port_number`
      
      `DB_ENGINE=sqlite3_engine`
      
      `DB_NAME=sqlite3_db_name`

7. Backend is ready, we can setup our frontend now: https://github.com/prachi-ec/robo-mission-control-dashboard

