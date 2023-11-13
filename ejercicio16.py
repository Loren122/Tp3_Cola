# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:

from cola_prioridad import ColaPrioridad

cola = ColaPrioridad()

# a. cargue tres documentos de empleados (cada documento se representa solamente con 
# un nombre).
def download():
    cola.arrive("Pedro", 1)
    cola.arrive("Lorenzo", 1)
    cola.arrive("Juan", 1)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
def getDocument(cola):
    print()
    print('Nombre del primer documento de la cola')
    print(cola.atention()[1])


# c. cargue dos documentos del staff de TI.
def downloadStaffTI(cola):
    cola.arrive("Julieta", 2)
    cola.arrive("Ramiro", 2)


# d. cargue un documento del gerente.
def downloadGerent(cola):
    cola.arrive("Alberto", 3)

# e. imprima los dos primeros documentos de la cola.
def deleteTwoFirst(cola):
    print()
    print('Los 2 primeros documentos de la cola')
    print(cola.atention())
    print(cola.atention())

# f. cargue dos documentos de empleados y uno de gerente.
def twoAndTreedownload(cola):
    cola.arrive("Alfonso", 1)
    cola.arrive("Federico", 1)
    cola.arrive("Julian", 3)

# g. imprima todos los documentos de la cola de impresión.
def allDelete(cola):
    print()
    print('Todos los documentos')
    for i in range(0, cola.size()):
        print(cola.atention())
    

download()
getDocument(cola)
downloadStaffTI(cola)
downloadGerent(cola)
deleteTwoFirst(cola)
twoAndTreedownload(cola)
allDelete(cola)
