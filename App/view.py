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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

def printCompanyData(comp):
    if comp:
        print('Compañia encontrada: ' + comp['production_companies'])
        print('Promedio: ' + str(comp['PromVote_average']))
        print('Total de peliculas: ' + str(lt.size(comp['movies'])))
        iterator = it.newIterator(comp['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['title'])
    else:
        print('No se encontro la compañia')

# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar catálogo de películas")
    print("2- Informacion de compañia")
    print("3- Entender género cinematográfico") 
    print("4- Encontrar películas por país")       
    print("0- Salir")

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if len(inputs)>0:
       if int(inputs[0]) == 1:
          archivo = "theMoviesdb/SmallMoviesDetailsCleaned.csv"
          catalogo_peliculas = controller.initCatalog()
          print("Inicializando Catálogo ....")
          
          map_p = controller.loadPeliculas(catalogo_peliculas, archivo)
          print(map_p)
          numero_cargadas = mp.size(map_p)
          print("Se cargaron ",numero_cargadas," peliculas")
       elif int(inputs[0])==2: #opcion 2
          ncomp = input(print("Nombre de la compañia a buscar:\n"))
          Comp = controller.getMoviesByCompany(catalogo_peliculas, ncomp)
          printCompanyData(Comp)
       elif int(inputs[0])==3: #opcion 3
            if catalogo_peliculas==None: 
                print("El catálogo no existe")    
            else:
                genero = input("Escriba el género cinematográfico: ")
                res_genero = controller.getEntenderGenero(genero, map_p)
                lista_genero = res_genero[0]
                numero = res_genero[1]
                votos = res_genero[2]
                print("Lista de peliculas:",lista_genero,"\n")
                print("Numero de peliculas:",numero,"\n") 
                print("Promedio de votos:",votos,"\n") 
       elif int(inputs[0])==4: #opcion 4
            if catalogo_peliculas==None: 
                print("El catálogo no existe")    
            else:        
                pais = input("Escriba el país de intéres: ")
                producidas_pais = controller.getPeliculasPais(pais, map_p)
                print(producidas_pais)       
                pass   
       elif int(inputs[0])==0: #opcion 0 salir
          sys.exit(0)