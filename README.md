# DjangoRest-Project
Proyecto [Formación Cristhian](https://www.udemy.com/user/cristhian-santa-cruz-carrion/) con Django Rest Framework Marcos Ruiz Muñoz 

Enlaces a los otros proyectos de Django:
- [Web Django](https://github.com/Markete17/WebPlayGroundPython/)

**Índice**   
1. [Configuración del proyecto](#id1)
2. [Introducción a Serializers y ListAPIView](#id2)

## Configuración del proyecto<a name="id1"></a>

- 1. <b>Configurar el entorno virtual</b>

Para ello, se hace uso de <b>pipenv shell</b> para crear el entorno virtual.
Una vez dentro de la consola, acceder a la requierements dentro del proyecto y ejecutar:

```console
pip install -r local.txt
```
Con las siguientes dependencias:
```txt
asgiref==3.2.7
Django==3.0.5
django-model-utils==4.0.0
psycopg2-binary==2.9.5
pytz==2019.3
sqlparse==0.3.1
Unipath==1.1
djangorestframework==3.14.0
```

- 2. <b>Instalar y configurar Postgres</b>

Antes que nada, instalas postgres en el ordenador: [Descargar Postgres](https://www.postgresql.org/download/)
Y establecer una contraseña administrador
Después, para usar Postgres en consola, es necesario configurar la variable de entorno. Para ello, ir a variables de entorno del sistema y en Path añadir una nueva entrada al bin del postgres: C:\Program Files\PostgreSQL\15\bin

Para entrar a la consola Postgres, escribir el comando:

```console
psql -U postgres
```

C:\Users\mruiz>psql -U postgres
Contraseña para usuario postgres:
psql (15.1)

Después, hay que crear una base de datos:

```console
postgres=# CREATE DATABASE agendadb;
```
Y conectarase a ella:
```console
postgres=# \c agendadb;
```
Hay que crear un usuario para que se pueda conectar con la app con Django:
```console
postgres=#create user neunapp with password 'neunapp2023';
```

Por último, es necesario dar permisos al esquema public al usuario postgres

```console
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
```

- 3. <b>Configuración Base de Datos Postgres en Django</b>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- 4. <b>Configuración Django Rest Framework</b>

```console
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Introducción a Serializers y ListAPIView<a name="id2"></a>

Es necesario tener una <b>clase serializadora</b>, es decir, la encargada de convertir el QuerySet en un objeto JSON para la respuesta REST.
Por lo tanto, antes hay que crear en la app, el archivo <b>serializers.py</b>

```python
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email'
        )
```

Y después en la Vista, utilizar ListAPIView para listar los objetos del modelo:

```python
class PersonListAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
```