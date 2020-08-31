############################################################
#  
#   This code was written in spanish, so maybe you
#   should translate in into your preferred language.
#   
#   GitHub: /sgarciapose/cd_book_db
#
############################################################

from peewee import *
from datetime import date
import numpy as np


mysql_db = MySQLDatabase('db_discos_libros', host="localhost",
                         port=3306, user="root", passwd="password")


class Discos_Dvd(Model):
    numero_disco = PrimaryKeyField()
    artista = CharField()
    album = CharField()
    año = IntegerField()
    sello = CharField()
    genero = CharField()
    tipo = CharField()

    class Meta:
        database = mysql_db
# END class Discos_DVD


class Libros(Model):
    # numero_libro = PrimaryKeyField()
    numero_libro = PrimaryKeyField()
    autor = CharField()
    titulo = CharField()
    editorial = CharField()
    genero = CharField()

    class Meta:
        database = mysql_db
# END class Libros


class Libros_Estudio(Model):
    # numero_libro = PrimaryKeyField()
    numero_libro = PrimaryKeyField()
    autor = CharField()
    titulo = CharField()
    año = IntegerField()
    editorial = CharField()

    class Meta:
        database = mysql_db


def ingresar_cd_dvd():
    """ Ingresa en la base de datos un disco o dvd
    Opciones: 1 - Ingresar un CD, 2 - Ingresar un DVD
     3 - Ver opciones, 4 - Salir """

    def mostrar_opciones():
        print("\n")
        print("1 - Ingresar un CD \n\
            2 - Ingresar un DVD \n\
            3 - Ver opciones \n\
            4 - Salir \n")
    # END mostrar_opciones

    def ingresar_datos_cd_o_dvd(CD_DVD):
        print("\n" + "*"*6 + "Por favor ingrese los datos del CD" +
              "*"*6 + "\n")
        artista = input("Artista: ").strip().title()
        album = input("Album: ").strip().title()
        try:
            año = int(input("Año: "))
        except ValueError:
            año = 0
        genero = input("Género: ").strip().title()
        tipo = CD_DVD
        CD_DVD_nuevo = Discos_Dvd.create(
            artista=artista, album=album, año=año, genero=genero, tipo=tipo)
        CD_DVD_nuevo.save()
    # END ingresar_datos_cd_o_dvd

    salir = False
    while salir is False:
        print("*"*30)
        mostrar_opciones()
        opcion = input("Ingrese el número de opcion: ").strip()

        if opcion == "1":
            ingresar_datos_cd_o_dvd("CD")
            print("\nCD ingresado con éxito -----")
            salir = True
        elif opcion == "2":
            ingresar_datos_cd_o_dvd("DVD")
            print("\nDVD ingresado con éxito -----")
            salir = True
        elif opcion == "3":
            mostrar_opciones()
            salir = False
        elif opcion == "4":
            salir = True
        else:
            print("\nEsa opción no está contemplada\n")
# END Ingresar_cd_dvd


def ingresar_libro():
    """Crea un registro de un nuevo libro en la base"""

    print("\n" + "*"*6 + "Por favor ingrese los datos del Libro" +
          "*"*6 + "\n")
    autor = input("Autor: ").strip().title()
    titulo = input("Título: ").strip().title()
    genero = input("Género: ").strip().title()

    Libro_nuevo = Libros.create(
        autor=autor, titulo=titulo, genero=genero)
    Libro_nuevo.save()

    print("\nLibro ingresado con éxito -----")


def desplegar_lista_discos(parametro=None):
    """Despliega lista de CDs y DVDs con opciones"""

    if (parametro == "CD") | (parametro == "DVD"):
        cds = Discos_Dvd.select().where((Discos_Dvd.tipo == parametro) |
                                        (Discos_Dvd.tipo == "CD/DVD"))
    else:
        cds = Discos_Dvd.select()

    line1 = F"{'Id':{' '}<4}   {'Artista':{' '}<20}   "
    line2 = F"{'Álbum':{' '}<30}   {'Año':{' '}<4}   "
    line3 = F"{'Género':{' '}<15}   {'Tipo':{' '}<6}"
    print(line1 + line2 + line3)
    print("-"*94)
    for cd in cds:
        line1 = F"{cd.numero_disco:{' '}<4}   {cd.artista[:20]:{' '}<20}   "
        line2 = F"{cd.album[:30]:{' '}<30}   {cd.año:{' '}<4}   "
        line3 = F"{cd.genero[:15]:{' '}<15}   {cd.tipo[:6]:{' '}<6}"
        print(line1 + line2 + line3)

    print(F"\n-- Se han desplegado {len(cds)} elementos --")


def desplegar_lista_libros(parametro=None):
    """ Despliega lista de Libros con opciones """
    print("\n1- Texto\n2- Estudio\n3-Salir")

    opcion = input("\nSeleccione una opción: ").strip()
    salir = None
    while salir is not True:
        if opcion == "1":
            salir = True
            libros = Libros.select()
            for libro in libros:
                line1 = F"{libro.numero_libro:{' '}<4}   {libro.autor[:20]:{' '}<20}   "
                line2 = F"{libro.titulo[:40]:{' '}<40}   {libro.editorial[:15]:{' '}<15}   "
                line3 = F"{libro.genero[:15]:{' '}<15}"
                print(line1 + line2 + line3)
            print(F"\n-- Se han desplegado {len(libros)} elementos --")
        elif opcion == "2":
            salir = True
            libros = Libros_Estudio.select()
            for libro in libros:
                line1 = F"{libro.numero_libro:{' '}<4}   {libro.autor[:30]:{' '}<30}   "
                line2 = F"{libro.titulo[:50]:{' '}<50}   {libro.año:{' '}<4}   "
                line3 = F"{libro.editorial[:15]:{' '}<15}"
                print(line1 + line2 + line3)
            print(F"\n-- Se han desplegado {len(libros)} elementos --")
        elif opcion == "3":
            salir = True
# END desplegar_lista_libros()


def actualizar_registro():
    """Genera todo el proceso de actualizar un registro
    en la base de datos, ya sea para CDs, DVDs o Libros"""

    def mostrar_opciones_():
        print("\n1 - CD\
                \n2 - DVD \
                \n3 - CD/DVD\n")
        # END mostrar_opciones

    def elegir_cd_dvd():
        """Elige entre CD DVD o CD/DVD"""

        mostrar_opciones_()
        salir = False
        while salir is False:
            eleccion = input("Elija 1, 2 o 3: ").strip()
            if eleccion == "1":
                salir = True
                return "CD"
            elif eleccion == "2":
                salir = True
                return "DVD"
            elif eleccion == "3":
                salir = True
                return "CD/DVD"
        # END elegir_cd_dvd

    def ingresar_datos_nuevos_cd_dvd():
        """Ingresa los nuevos datos para ser actualizados
        en el registro elegido"""

        mensaje_1 = "Por favor ingrese los datos que quiera actualizar"
        mensaje_2 = "DEJE EL CAMPO VACIO (ENTER) PARA NO ACTUALIZAR ESE DATO"
        print("\n" + "*"*6 + mensaje_1 + "*"*6 + "\n")
        print("===  " + mensaje_2 + "  ===")

        artista_update = input("Artista: ").strip().title()
        album_update = input("Album: ").strip().title()
        salir = False

        while salir is False:
            año_update = input("Año: ").strip()
            if año_update != "":
                try:
                    año = int(año_update)
                    salir = True
                except ValueError:
                    print("\n** Ingrese un año o deje el campo vacío **\n")
            else:
                salir = True

        genero_update = input("Género: ").strip().title()
        tipo_update = elegir_cd_dvd()

        return artista_update, album_update, año_update,
        genero_update, tipo_update
        # END ingresar_datos_nuevos_cd_dvd()

    def filtrar_datos(art, alb, año, gen, tipo, num):
        """Filtra los datos ingresados para actualizar"""

        if art == "":
            art = Discos_Dvd.artista.select().where(
                Discos_Dvd.numero_disco == num)

        if alb == "":
            alb = Discos_Dvd.album.select().where(
                Discos_Dvd.numero_disco == num)

        if año == "":
            año = Discos_Dvd.año.select().where(
                Discos_Dvd.numero_disco == num)
        else:
            año = int(año)

        if gen == "":
            gen = Discos_Dvd.gen.select().where(
                Discos_Dvd.numero_disco == num)

        if tipo == "":
            tipo = Discos_Dvd.tipo.select().where(
                Discos_Dvd.numero_disco == num)

        return art, alb, año, gen, tipo
        # END filtrar_datos

    def elegir_numero():
        """Elige el número de disco que se desea actualizar,
        el número es una clave primaria y por lo tanto única"""

        valido = None
        while valido is not True:
            seleccionado = input(
                "Ingrese el número de disco que quiera actualiar: ").strip()
            try:
                seleccionado = int(seleccionado)
            except ValueError:
                valido = False
            else:
                valido = True
        return seleccionado
        # END elegir_numero
    # --------------------------------------------------------
    # BLOQUE PRINCIPAL
    num_disco = elegir_numero()
    validos = Discos_Dvd.select().where(Discos_Dvd.numero_disco == num_disco)
    if len(validos) == 0:
        print("\n*** NO EXISTE ESE DISCO EN LA BASE DE DATOS ***")
    else:
        art, alb, año, gen, tipo = ingresar_datos_nuevos_cd_dvd()
        art, alb, año, gen, tipo = filtrar_datos(
            art, alb, año, gen, tipo, num_disco)
        cambiar = Discos_Dvd.update(artista=art, album=alb, año=año,
                                    genero=gen, tipo=tipo).where(
                                        Discos_Dvd.numero_disco == num_disco)
        num_elem = cambiar.execute()
        print("\n---- Se ha actualizado {num_elem} elemento")
    # ----------------------------------------------------------
    # END actualizar_registro


def hacer_consulta():
    """ Realiza una consulta en la base de datos """

    print("Ingrese palabras, números o frases separadas por comas ','")
    print("que desee buscar en la base de datos: ")
    entradas = 0
    busquedas = input().strip().split(',')
    largo = len(busquedas)
    if not((largo == 1) & (busquedas[0] == "")):
        print("\n" + "*"*50)
        print(F"\n{'RESULTADO DE LA BÚSQUEDA':^50}")
        print("\n" + "*"*50)

        for i in range(largo):
            busqueda = busquedas[i].strip()
            if busqueda != "":
                try:
                    numero = int(busqueda)
                except ValueError:
                    numero = -1

                # BUSCO EN LOS DISCOS
                cds = Discos_Dvd.select().where(
                    Discos_Dvd.artista.contains(busqueda) |
                    Discos_Dvd.album.contains(busqueda) |
                    Discos_Dvd.sello.contains(busqueda) |
                    Discos_Dvd.año.contains(numero) |
                    Discos_Dvd.genero.contains(busqueda)
                )
                entradas += len(cds)
                if len(cds) != 0:
                    print()
                    line1 = F"{'Id':{' '}<4}   {'Artista':{' '}<20}   "
                    line2 = F"{'Álbum':{' '}<30}   {'Año':{' '}<4}   "
                    line3 = F"{'Género':{' '}<15}   {'Tipo':{' '}<6}"
                    print(line1 + line2 + line3)
                    print("-"*94)
                    for cd in cds:
                        line1 = F"{cd.numero_disco:{' '}<4}   {cd.artista[:20]:{' '}<20}   "
                        line2 = F"{cd.album[:30]:{' '}<30}   {cd.año:{' '}<4}   "
                        line3 = F"{cd.genero[:15]:{' '}<15}   {cd.tipo[:6]:{' '}<6}"
                        print(line1 + line2 + line3)

                # BUSCO EN LIBROS DE TEXTO
                libros = Libros.select().where(
                    Libros.autor.contains(busqueda) |
                    Libros.titulo.contains(busqueda) |
                    Libros.editorial.contains(busqueda) |
                    Libros.genero.contains(busqueda)
                )
                entradas += len(libros)
                if len(libros) != 0:
                    print()
                    line1 = F"{'Id':{' '}<4}   {'Autor':{' '}<20}   "
                    line2 = F"{'Título':{' '}<40}   {'Editorial':{' '}<15}   "
                    line3 = F"{'Género':{' '}<15}"
                    print(line1 + line2 + line3)
                    print("-"*106)
                    for libro in libros:
                        line1 = F"{libro.numero_libro:{' '}<4}   {libro.autor[:20]:{' '}<20}   "
                        line2 = F"{libro.titulo[:40]:{' '}<40}   {libro.editorial[:15]:{' '}<15}   "
                        line3 = F"{libro.genero[:15]:{' '}<15}"
                        print(line1 + line2 + line3)

                # BUSCO EN LIBROS DE ESTUDIO
                libros = Libros_Estudio.select().where(
                    Libros_Estudio.autor.contains(busqueda) |
                    Libros_Estudio.titulo.contains(busqueda) |
                    Libros_Estudio.editorial.contains(busqueda) |
                    Libros_Estudio.año.contains(numero)
                )
                entradas += len(libros)
                if len(libros) != 0:
                    print()
                    line1 = F"{'Id':{' '}<4}   {'Autor':{' '}<30}   "
                    line2 = F"{'Título':{' '}<50}   {'Año':{' '}<4}   "
                    line3 = F"{'Editorial':{' '}<15}"
                    print(line1 + line2 + line3)
                    print("-"*115)
                    for libro in libros:
                        line1 = F"{libro.numero_libro:{' '}<4}   {libro.autor[:30]:{' '}<30}   "
                        line2 = F"{libro.titulo[:50]:{' '}<50}   {libro.año:{' '}<4}   "
                        line3 = F"{libro.editorial[:15]:{' '}<15}"
                        print(line1 + line2 + line3)
        print(F"\n--- Se han encontrado {entradas} entradas ---")


def create_and_connect():
    mysql_db.connect()
    mysql_db.create_tables([Discos_Dvd, Libros, Libros_Estudio], safe=True)
# END create_and_connect()


def __main__():
    """ Programa principal de la base de datos """

    print("*"*74 + "\n")
    print("*"*19 + "   Catálogo de CDs, DVDs y Libros   " + "*"*19 + "\n")
    print("*"*74 + "\n")

    def mensaje_despedida():
        print("*"*74 + "\n")
        print("*"*28 + "   Hasta luego   " + "*"*29 + "\n")
        print("*"*74)

    def mostrar_opciones_main():
        """Despliega las opciones del menú del Main"""

        print("\n1 - Ingresar un CD o DVD\
            \n2 - Ingresar un Libro\
            \n3 - Desplegar lista de CDs y DVDs\
            \n4 - Desplegar lista de CDs\
            \n5 - Desplegar lista de DVDs\
            \n6 - Desplegar lista de Libros\
            \n7 - Hacer una consulta\
            \n8 - Salir")

    def seguir_haciendo_cosas():
        fin = False
        while fin is False:
            otra_accion = input(
                "\n¿Quiere realizar otra acción? (Y/N): ").strip().upper()
            if otra_accion == "Y":
                fin = True
                return False
            elif otra_accion == "N":
                fin = True
                return True

    salir_main = False
    print("¿Qué desea hacer?")
    mostrar_opciones_main()
    while salir_main is False:
        print()
        print("Para ver las opciones ingrese la letra 'o'")
        opcion_main = input("Ingrese la opción que quiera realizar: ").strip()
        print()

        if opcion_main == "o" or opcion_main == "O":
            mostrar_opciones_main()
        elif opcion_main == "1":  # ingresar cd o dvd
            ingresar_cd_dvd()
            salir_main = seguir_haciendo_cosas()
        elif opcion_main == "2":  # ingresar libro
            ingresar_libro()
            salir_main = seguir_haciendo_cosas()
        elif opcion_main == "3":  # desplegar lista cds y dvds
            desplegar_lista_discos()
            salir_main = seguir_haciendo_cosas()
        elif opcion_main == "4":  # desplegar lista de cds
            desplegar_lista_discos("CD")
            salir_main = seguir_haciendo_cosas()
        elif opcion_main == "5":  # desplegar lista de dvds
            desplegar_lista_discos("DVD")
            salir_main = seguir_haciendo_cosas()
        elif opcion_main == "6":  # desplegar lista libros
            desplegar_lista_libros()
            salir_main = seguir_haciendo_cosas()
        elif opcion_main == "7":  # hacer una consulta
            hacer_consulta()
            salir_main = seguir_haciendo_cosas()
        elif opcion_main == "8":  # salir
            salir_main = True

    print()
    mensaje_despedida()
# END __main__


create_and_connect()


if __name__ == "__main__":
    __main__()
