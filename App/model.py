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
                }
    catalog['details'] = lt.newList('SINGLE_LINKED', CompareIdsMovies)
    catalog['compañias'] = mp.newMap(329045,maptype='CHAINING',loadfactor=0.4,comparefunction=compareCompanyByName)
    return catalog


def addMovie(catalog, movie):
    lt.addLast(catalog['details'], movie)
    mp.put(catalog['details'], movie["id"], movie)

def newCompany(name):
    company = {'name': "", "movies": None,  "vote_average": 0}
    company['name'] = name
    company['movies'] = lt.newList('SINGLE_LINKED', compareCompanyByName)
    return company

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
    company['PromVote_average'] = company['PromVote_average']/lt.size(company['movies'])

def getMoviesByCompany(catalog, ncomp):
    company = mp.get(catalog['compañias'], ncomp)
    if company:
        return me.getValue(company)
    return None

def CompareIdsMovies(id1, id2):
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
