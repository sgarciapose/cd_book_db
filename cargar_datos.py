############################################################
#  
#   This code was written in spanish, so maybe you
#   should translate in into your preferred language.
#   
#   GitHub: /sgarciapose/cd_book_db
#
############################################################

# CD and DVD
#--------------
# My db has this columns: ID (ignored as automatically created in this db), Artist, Album,
#                         Year, Label, Genre, Type (CD, DVD, or both).

# Books
#-------------
# My db has this columns: ID (same quote as CD and DVD), Title, Author, Publisher, Genre


import numpy as np

data = np.loadtxt("Catalogo_CSV.csv", delimiter=",",
                  skiprows=1, dtype=str)
largo = len(data[:, 0])
for i in range(largo):
    if data[i, 3] == "":
        data[i, 3] = 0
    else:
        data[i, 3] = int(data[i, 3])
for i in range(largo):

    CD_DVD_nuevo = Discos_Dvd.create(
        artista=data[i, 1], album=data[i, 2], año=data[i, 3], sello=data[i, 4],
        genero=data[i, 5], tipo=data[i, 6])
    CD_DVD_nuevo.save()


data = np.loadtxt("Estudio.csv", delimiter=",",
                  skiprows=1, dtype=str)
largo = len(data[:, 0])
for i in range(largo):

    CD_DVD_nuevo = Libros_Estudio.create(
        titulo=data[i, 1], autor=data[i, 0], editorial=data[i, 3], año=data[i, 2])
    CD_DVD_nuevo.save()


data = np.loadtxt("Libros.csv", delimiter=",",
                  skiprows=1, dtype=str)
largo = len(data[:, 0])
for i in range(largo):

    CD_DVD_nuevo = Libros.create(
        titulo=data[i, 1], autor=data[i, 0], editorial=data[i, 2], genero=data[i, 3])
    CD_DVD_nuevo.save()
