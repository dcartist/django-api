# Remix Lyrics API




Remix Lyrics API is the django api for remix lyrics app. It was made with Python, Django and Postgres 




## EndPoints

| Endpoints           | Location              |
| ------------------- | --------------------- |
| /                   | List all categories   |
| /categories/        | List all categories   |
| /songs/             | List all songs        |
| /songs/:songId/     | List song by id       |
| /artists/           | List all artist       |
| /artists/:artistId/ | List artist by id     |
| /remixlevels/       | List all remix levels |







## Prerequisites

Before you begin, ensure you have the following installed:

- Python (>= 3.x)
- pip (Python package installer)
- pipenv
- Postgres

## Installation

Clone the project to your local machine using:

```bash
git clone https://github.com/dcartist/django-api.git
cd django-api
```

use pipenv to install the django app with the following command in the terminal

```bash
pipenv install
```

You must create a postgres database, then using the variables create a .env using the following:

```bash
SECRET_KEY="SECRET_KEY_HERE"
DEBUG=True
DB_URL=postegresURL_here
DB_NAME=dbNAME_here
DB_USER=dbUSERNAME_here
DB_PASSWORD=dbPassWord_here
```


run the pipenv enviroment using: 

```bash
pipenv install
```

inside the pipenv shell check run the migrations using

```bash
python3 manage.py. migrate
```

Then run the app using

```bash
python3 manage.py. runserver
```





