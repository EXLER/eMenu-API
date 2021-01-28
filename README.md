# eMenu-API
eMenu, an API serving as a restaurant's menu, built with Django &amp; Django REST framework

## Installation

* Copy the `.env.example` file as `.env` and set the `SECRET_KEY` variable
* Run using *docker-compose*
```bash
$ docker-compose up -d
```
* You can load the initial data using the following command:
```bash
$ docker-compose run web python manage.py loaddata data.json
```

## Usage

* Auto-generated Swagger API documentation: `http://localhost:8000/swagger/`
* API root: `http://localhost:8000/api/`

## Testing

To run the tests through Docker use the following command:
```bash
$ docker-compose run web python manage.py test
```

### Coverage
You can check the code coverage using the following commands:
```bash
$ docker-compose run web coverage run manage.py test
$ docker-compose run web coverage report
```