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
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________





# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar catálogo de películas")
    print("2- Información de las películas (título, fecha de estreno, promedio de votación, número de votos e idioma)")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("7- encontrar peliculas buenas")
    print("0- Salir")

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if len(inputs)>0:
       if int(inputs[0]) == 1:
          archivo = "theMoviesdb/SmallMoviesDetailsCleaned.csv"
          catalogo_peliculas = controller.initCatalog()
          print("Inicializando Catálogo ....")
          lista_p = controller.loadPeliculas(catalogo_peliculas, archivo)
          numero_cargadas = lt.size(lista_p)
          print("Se cargaron ",numero_cargadas," peliculas")
       elif int(inputs[0])==2: #opcion 2
          print("Peliculas cargadas: ", lista_p)
          peliculas = 0 
       elif int(inputs[0])==0: #opcion 0 salir
          sys.exit(0)        

