# Task

# Lanzar proyecto en dev

### 1. Instalar python

### 2. Instalar dependencias

```bash
pip install -r requirement.txt
```

### 3. Lanzar postgres
En este caso usaremos docker

```bash
docker run --rm --name pg -e POSTGRES_PASSWORD=12345 -p 5432:5432 postgres
```

## 4. Correr migraciones

```bash
python manage.py migrate
```

## 5. Correr aplicación

```bash
python manage.py runserver
```

La aplicación corre en `localhost:8000`