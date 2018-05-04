# Blog con Python 3 + Django

Algunos comandos de utilidad
-

```
virtualenv blog-django o virtualenv .
```

 (dentro de la carpeta del proyecto)
```
.\Scripts\activate
pip install django
```
```
python .\Scripts\django-admin.py startproject blogdjango    
```
(con esto salen las opciones ejemplo: migraciones startproject y demás)
```
python .\Scripts\django-admin.py
```
```
cd blogdjango
```

```
python manage.py runserver
``` 
Si se pones 8001 al final nos da otro puerto

```
python manage.py migrate (Migraciones)
```
Crear super usuario (Antes de eso hacer las migraciones)
```
python manage.py createsuperuser Ejem admin - arrow1995
```

Creando app  python
```
python manage.py startapp posts
```
Migraciones a modelos
```
python manage.py makemigrations
python manage.py migrate
```
Archivos estaticos
```
python manage.py collectstatic
```