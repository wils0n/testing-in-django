### Commands for Test  

* Para testear solo el proyecto, usamos el flag 'source' y evitará la evaluacion de las funciones built-in de python y otras librerias instaladas en el virtualenv  

```
coverage run --source='.' manage.py test
```

* Para testear solo el proyecto y ver el detalle en la ejecución

```
coverage run --source='.' manage.py test -v 2
```

* Para testear nuestra app llamada whatever

```
coverage run --source='whatever' manage.py test
```
o

```
coverage run manage.py test whatever
```
> El problema del ultimo comando es que evaluara las funciones built-in de python, django y librerias

* Para ver el reporte en la terminal

```
coverage report
```

* Para ver el reporte en una presentación html

```
coverage html
```
> Abrir htmlcov/index.html
