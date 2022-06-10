# API Restful con Flask

Este proyecto es una tarea para una postulacion. Se compone de python con flask exponiendo una api rest, con opciones de obtener xml o json (dependiendo del header "Accept":"application:json" o "Accept":"application:xml")

## Instalacion y Ejecucion

Se deben instalar las librerias requerimiento primero

```bash
python -m pip install -r requirements.txt
```

Despues se ejecuta

```bash
python app.py
```

## Pruebas Unitarias

Se ejecutan las pruebas unitarias con el siguiente comando

```bash
python -m unittest  
```

## Dockerizar

Al tener Dockerfile simplemente se hace la imagen del proyecto

```bash
docker build -t apitest:latest . 
```

Despues se monta la imagen a un container

```bash
docker run -p 5000:5000 apitest
```
