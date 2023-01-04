# django-ninja-example

### This is a small example of a project using the django ninja framework.

## this example is taken by the following [youtube tutorial](https://www.youtube.com/playlist?list=PL-2EBeDYMIbS7bXwkMOS_ajeTdNRnhApX)

## tutorial [github](https://github.com/bugbytes-io/django-ninja-v1)

## how to run the project:

```sh
git clone https://github.com/mpita/django-ninja-example.git
```
```sh
cd django-ninja-example
```
```sh
python3 -m venv .venv
```
```sh
source .venv/bin/activate
```
```sh
pip install -r requirements.txt
```
```sh
python manage.py migrate
```
```sh
python manage.py ingest_tracks
```
```sh
python nmanage.py runserver
```

[swagger documentation url - http://localhost:8000/api/docs](http://localhost:8000/api/docs)
