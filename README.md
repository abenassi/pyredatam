pyredatam
===============================
[![Coverage Status](https://coveralls.io/repos/abenassi/pyredatam/badge.svg?branch=master&service=github)](https://coveralls.io/github/abenassi/pyredatam?branch=master)
[![Build Status](https://travis-ci.org/abenassi/pyredatam.svg?branch=master)](https://travis-ci.org/abenassi/pyredatam)
[![PyPI](https://badge.fury.io/py/pyredatam.svg)](http://badge.fury.io/py/pyredatam)
[![Buy me a coffee](https://img.shields.io/badge/donate-buy%20me%20a%20coffee-blue.svg)](http://ko-fi.com?i=934NLRIV80O8)


Genera consultas REDATAM en python.

## Instalación

```python
virtualenv pyredatam  # Create new environment
source pyredatam/bin/activate  # Activate the environment
pip install -r requirements.txt  # Install dependencies
```

## Uso

```python
import pyredatam

# para generar una consulta de lista por áreas
query = pyredatam.arealist_query("FRAC", "PERSONA.CONDACT", 
                                 {"PROV": ["02", "03"]})
print query
"""
RUNDEF Job
        SELECTION INLINE,
         PROV 02, 03
    <BLANKLINE>
    TABLE TABLE1
        AS AREALIST
        OF FRAC, PERSONA.CONDACT
"""

# para hacer la consulta a la base REDATAM del Censo 2010 de Argentina
df = pyredatam.cpv2010arg.make_arealist_query(query)
# devuelve un pandas.DataFrame con el resultado

# para hacer otras consultas REDATAM que no sean de tipo lista por áreas
html = pyredatam.cpv2010arg.make_query(query)
# devuelve un html con el resultado, que debe ser parseado

# para construir el diccionario de entidades, variables y categorías
dicc, entidades_geo, entidades_data = pyredatam.cpv2010arg.scrape_dictionary()
```

## Generar consultas REDATAM

Esta es una lista de los tipos de consultas que el sistema REDATAM permite, la idea es ir implementando todas ellas en este paquete. Si necesitás usar alguna que aún no ha sido implementada, bienvenidas todas las contribuciones!

* Estadísticas (**Falta implementar**)
* Frecuencias (**Falta implementar**)
* Cruce de Variables (**Falta implementar**)
* Promedio (**Falta implementar**)
* Mediana (**Falta implementar**)
* Conteo (**Falta implementar**)
* Lista por Áreas (**SOPORTADO!**)
    - *Una o más variables* (variables cuyos datos se quiere obtener)
    - *Nivel de Salida* (nivel de agregación geográfico al cual se piden los datos)
    - *Incluir Nombres del Área de Salida* (incluir nombres además de los códigos de las áreas de salida - **Falta implementar**)
    - *Título* (título que tendrá la tabla con los resultados solicitados)
    - *Selección de Área* (restringir los resultados a un área geográfica en particular)
    - *Filtro Universal* (expresión de filtro en lenguaje REDATAM)
    - *Peso* (uso de ponderadores - **Falta implementar**)

## Scrapear resultados de consultas REDATAM

El paquete incluirá un módulo por base de datos REDATAM que permita hacer las consultas generadas a la base correspondiente al que se acceda como `pyredatam.modulo_redatam_db`. Por ahora sólo se provee un módulo con métodos para consultar y parsear el resultado de la base de datos REDATAM del Censo 2010 de Argentina. Todos los módulos que se agreguen deberían proveer, al menos, los siguientes métodos públicos:

* `make_query(query)` - Devuelve un html (u otra cosa, si no es posible) con el resultado de la query realizada a la base de datos.
* `make_arealist_query(query)` - Métodos específicos para cada tipo de consulta, que usen make_query() y luego parseen el resultado html (o del formato que sea) a un DataFrame de pandas.
* `scrape_dictionary()` - Un método que devuelva un diccionario jerárquico ordenado (collections.OrderedDict) de entidades, sus variables y las categorías de las variables; una lista de las entidades que se utilizan para agregar geográficamente la información, y una lista de las entidades que contienen variables con data (no usadas para agregar la base de datos geográficamente, sino con la data que es realmente el objetivo de la encuesta o censo).



