# music-plus

MUSIC PLUS API, созданное с помощью FastAPI и SQLite3 с музыкальной базой данных 🎵

## Эндпоинты

#### Артист
![1](https://user-images.githubusercontent.com/88138099/186618519-31a53ce3-85ac-49de-8db2-fb5842d99744.png)

#### Альбом
![2](https://user-images.githubusercontent.com/88138099/186618701-0b9ec5d5-6619-4e7c-a2a8-025bb94a0ed0.png)

#### Песня
![3](https://user-images.githubusercontent.com/88138099/186618740-686d1c8f-de4b-47f1-8199-eb1c894825fa.png)

## Быстрый старт (Quick Start)

Установите зависимости:

```bash
git clone https://github.com/dsymbol/music-api
pip install -r requirements.txt
```

Создайте базу данных и запустите API:

```bash
python src/database.py
python -m uvicorn --port 5000 server:app
```

Просмотреть документацию API можно по адресу: http://localhost:5000

## Пример запроса (Example)

#### Запрос (Request):

```
GET http://localhost:5000/api/artist?name=drake
```

#### Ответ (Response):

```json
[
  {
    "artist_id": 3,
    "name": "Drake",
    "first_name": "Aubrey",
    "last_name": "Graham",
    "phone": "615-541-4518",
    "website": "drakerelated.com",
    "is_group": false
  }
]
```

## PyTest

Тесты не зависят друг от друга, после запуска каждого файла с тестами необходимо сбрасывать базу данных.
