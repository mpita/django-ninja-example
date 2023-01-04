# django-ninja-example

### This is a small example of a project using the django ninja framework.

## this example is taken by the following [youtube tutorial](https://www.youtube.com/playlist?list=PL-2EBeDYMIbS7bXwkMOS_ajeTdNRnhApX)

## tutorial [github](https://github.com/bugbytes-io/django-ninja-v1)

## how to run the project:

```sh
git clone https://github.com/mpita/django-ninja-example.git
cd django-ninja-example
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py ingest_tracks
python nmanage.py runserver
```

[swagger documentation url - http://localhost:8000/api/docs](http://localhost:8000/api/docs)
