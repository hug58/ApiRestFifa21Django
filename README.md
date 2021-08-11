# API FIFA 21 
guardar data de la api fifa 21 en una database postgres y django rest 

### Reto algoritmo de ordenamiento
```python

la funcion canBeSplitted espera un array[int]
Ten en cuenta que los elementos de la lista esten separados por un espacio

python algorithm.py --list 1 2 3 3 3 //devuelve 1
python algorithm.py --list 1 2   // devuelve -1
python algorithm.py // devuelve 0



```

## Configurar .env
Configure su .env para la db

```env

  SECRET_KEY=supersecret!

  POSTGRES_DB=fifadb
  POSTGRES_USER=hug58
  POSTGRES_PASSWORD=123456

  DEBUG=1
```



## Instalacion
Compila primero todo los servicios

```bash
  docker-compose up -d --build
```

luego ejecuta y crea las migraciones de django:

```bash
  docker-compose exec web python manage.py makemigrations 

  docker-compose exec web python manage.py migrate 
```

#### ejecutar peticiones a la api de fifa21 y guardarlo


```bash
    docker-compose exec web python tools/main.py
```

Hay varios jugadores repetidos en la api de fifa(ej:Cristiano), para evitar guardarlos use este en vez del anterior

```bash
    docker-compose exec web python tools/main.py --repeat 0
```


## Correr gunicorn

```bash
  docker-compose up
```

## Para desmotar la imagen usa el comando

```bash
  docker-compose down -v
```



## Obtener informacion de un jugador
```bash
    curl http://localhost:8000/api/v1/players?search=Cr&order=desc&page=2
```

## Obtener informacion de un equipo

```bash
    curl -X POST -H "Content-Type: application/json" -d '{"Name": "reaL maDRI "page": 2}' http://localhost:8000/api/v1/team
```
