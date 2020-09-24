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
  Este módulo implementa el tipo abstracto de datos
  (TAD) Map sin orden. Se puede implementar sobre una estructura
  de datos Hash Table, con resolución de colisiones: Linear Probing
  o separate chaining
"""

def newCatalog():
    catalog = {'details': None,
               'casting': None, 
               'compañias': None,
               'directores':None,
                }
    catalog['details'] = lt.newList('SINGLE_LINKED', CompareIdsMovies)
    catalog['casting'] = lt.newList('SINGLE_LINKED', CompareIdsMoviesC)
    catalog['compañias'] = mp.newMap(1000,maptype='CHAINING',loadfactor=0.7,comparefunction=compareCompanyByName)
    catalog['directores'] = mp.newMap(1000,maptype='CHAINING',loadfactor=0.7,comparefunction=compareDirectorByName)
    return catalog


def addMovie(catalog, movie):
    lt.addLast(catalog['details'], movie)
    mp.put(catalog['details'], movie["id"], movie)

def addCasting(catalog, movie):
    lt.addLast(catalog['casting'], movie)
    mp.put(catalog['casting'], movie["id"], movie)

def newCompany(name):
    company = {'name': "", "movies": None,  "vote_average": 0}
    company['name'] = name
    company['movies'] = lt.newList('SINGLE_LINKED', compareCompanyByName)
    return company

def newDirector(name):
    diretor = {'name': "", "movies": None,  "vote_average": 0}
    director['name'] = name
    director['movies'] = lt.newList('SINGLE_LINKED', compareDirectorByName)
    return director

def addMoviesCompany(catalog, companyname, Movie):
    companys = catalog['compañias']
    existcompany = mp.contains(companys, companyname)
    if existcompany:
        entry = mp.get(companys, companyname)
        company = me.getValue(entry)
    else:
        company = newCompany(companyname)
        mp.put(companys, companyname, company)
    lt.addLast(company['movies'], Movie)
    company['vote_average'] = company['vote_average']/2

def addMoviesDirector(catalog, directorname, Movie):
    directores = catalog['directores']
    existdirector = mp.contains(directores, directorname)
    if existdirector:
        entry = mp.get(directores, directorname)
        director = me.getValue(entry)
    else:
        director = newDirector(directorname)
        mp.put(directores, directorname, director)
    lt.addLast(director['movies'], Movie)
    director['vote_average'] = director['vote_average']/2

def getMoviesByCompany(catalog, ncomp):
    company = mp.get(catalog['compañias'], ncomp)
    if company:
        return me.getValue(company)
    return None

def getMoviesByDirector(catalog, ndirec):
    director = mp.get(catalog['directores'], ndirec)
    if director:
        return me.getValue(director)
    return None

def CompareIdsMovies(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def CompareIdsMoviesC(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareCompanyByName(keyname, company):
    authentry = me.getKey(company)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareDirectorByName(keyname, director):
    authentry = me.getKey(director)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
