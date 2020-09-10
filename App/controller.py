"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadPeliculas(lst, file):
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row:
                ## Eliminar la información que no fue solicitada para el laboratorio
                elemento.pop("id")
                elemento.pop("budget")
                elemento.pop("genres")
                elemento.pop("imdb_id")
                elemento.pop("original_language")
                elemento.pop("overview")
                elemento.pop("popularity")
                elemento.pop("production_companies")
                elemento.pop("production_countries")
                elemento.pop("revenue")
                elemento.pop("runtime")
                elemento.pop("status")
                elemento.pop("tagline")
                elemento.pop("original_title")
                elemento.pop("production_companies_number")
                elemento.pop("spoken_languages_number")
                elemento.pop("production_countries_number")
                model.addMovie(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst 
