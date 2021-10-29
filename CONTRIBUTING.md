# Contributing to AccessMap

Welcome to our Hackathon project! This is a Django App.

## Using Docker

- Download [Docker](https://www.docker.com/get-started)
- Test the installation with
```
docker run hello-world
```
- Run `docker-compose up` from the root directory of this repository
(where `docker-compose.yml` is).
This will launch the app locally at http://localhost:8000.

### Potential Errors

1. `Version in "./docker-compose.yml" is unsupported. You might be seeing this error because you're using the wrong Compose file version.`
The installation of `docker-compose` you have is too old!
Try to download the [latest release](https://github.com/docker/compose/releases)
from GitHub.
Alternatively, follow their
[documented install procedure](https://docs.docker.com/compose/install/).

2. `Got permission denied while trying to connect to the Docker daemon socket at unix`
This occurred because you were trying to run as a non-root user.
Either run as root, or create a `docker` group.
```bash
$ sudo groupadd docker
$ sudo usermod -aG docker ${USER}
# Logout and log back in OR run `su -s ${USER}`
# Test with:
$ docker run hello-world
```

3. `Package X is not installed`
Something was likely added after you built your Docker container.
```
docker-compose down
docker-compose up --build
```

4. Generic database issues -- 404 with app information
```
## With the project "running" in another Terminal
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

5. `django.db.migrations.exceptions.InconsistentMigrationHistory: Migration ABC is applied before its dependency ABC on database 'default'`

If error persists:
```
docker-compose up --force-recreate --no-deps --build db
docker-compose up
## In another terminal, simultaneously
docker-compose exec web python manage.py migrate
```


### Creating an Admin Account

```
docker-compose exec web python manage.py createsuperuser
```

### Installing New Packages

To add more requirements to the Docker image, do
```
docker-compose exec web pipenv install <PACKAGENAME>
```
while the image is running.

After, rebuild the container:
```
docker-compose up --build web
```

## Setting Up (Manually)

If you're using Docker, ignore this!

Install Python3 ([Anaconda](https://www.anaconda.com/products/individual)
is recommended!).

Install the required packages:
```
python3 -m pip install -r requirements.txt
```

### Testing Locally

```
python3 manage.py runserver
```

## Using Heroku

```
git push heroku main
```

```
heroku container:login
heroku container:push web
heroku container:release web
```

## Additional Documentation

- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django GitHub Actions Tutorial](https://www.hacksoft.io/blog/github-actions-in-action-setting-up-django-and-postgres)

## Additional Information on Web Accessibility

- [Color Oracle - Color Blindness Simulator](https://colororacle.org/)
- [Coolors Color Contrast Checker](https://coolors.co/contrast-checker)
- [Who Can Use -- color guidelines](https://whocanuse.com/)
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- [WAVE Browser Extension (works on local test site)](https://wave.webaim.org/extension/)
- [Web AIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
