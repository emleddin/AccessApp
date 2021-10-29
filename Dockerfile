FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Install geospatial libraries
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin

# Install python dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

COPY . /code/

# run gunicorn
CMD gunicorn AccessMap.wsgi:application --bind 0.0.0.0:$PORT
