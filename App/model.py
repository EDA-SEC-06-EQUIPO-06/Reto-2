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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Peliculas
# -----------------------------------------------------



# Funciones para agregar informacion al catalogo

def newCatalog(datastructure='ARRAY_LIST', cmpfunction=None):
    """Crea una lista vacia.

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Una nueva lista
    Raises:
        Exception
    """
    try:
        lst = lt.newList(datastructure, cmpfunction)
        return lst
    except Exception as exp:
        error.reraise (exp, 'TADList->newList: ')



def addMovie(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza el apuntador a la útima posición. 
    Se incrementa el tamaño de la lista en 1
    
    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    try:
        lt.addLast (lst, element)
    except Exception as exp:
        error.reraise (exp, 'TADList->addLast: ')




# ==============================
# Funciones de consulta
# ==============================

def isEmptyCatalog (lst):
    """ Indica si la lista está vacía

    Args: 
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lt.isEmpty(lst)
    except Exception as exp:
        error.reraise (exp, 'TADList->isEmpty: ')


def sizeCatalog(lst):
    """ Informa el número de elementos de la lista.

    Args
        lst: La lista a examinar
    
    Raises: 
        Exception
    """
    try: 
        return lst.size(lst)
    except Exception as exp:
        error.reraise (exp, 'TADList->size: ')


