# Проект использующий UV
Веб-приложение, созданное с использованием [UV](https://github.com/astral-sh/)
## Требования

- [Docker](https://docs.docker.com/get-docker/) (v20.10+)
- [Docker Compose](https://docs.docker.com/compose/install/) (v2.0+)

## Быстрый старт

### 1. Клонируйте репозиторий
```
bash
git clone https://github.com/igor228337/cobec.git
```

### 2. Соберите и запустите контейнеры
```docker compose up --build```

Для запуска в фоновом режиме:
```docker compose up --build -d```

### 3. Доступ в приложение 
Доступ к приложению
Основной сервис: http://localhost:8000

Документация API: http://localhost:8000/docs

Админ-панель: http://localhost:8000/admin
