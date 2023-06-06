from cola import Cola

# Se tienen una cola con personajes de Marvel Cinematic Universe(MCU), de los cuales se conoce el nombre
# del personaje, el nombre del superhéroe y su género(Masculino M y Femenino F)
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M},
# {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

class PersonajeMCU:
    
    def __init__(self, nombre, superheroe, genero):
        
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero
        

def cargar_personajes(cola):
    personajes = [
        PersonajeMCU("Natasha Romanoff", "Black Widow", "F"),
        PersonajeMCU("Tony Stark", "Iron Man", "M"),
        PersonajeMCU("Scott Lang", "Ant-Man", "M"),
        PersonajeMCU("Steve Rogers", "Capitan America", "M"),
        PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"),
        PersonajeMCU("Peter Parker", "Spider-Man", "M"),
        PersonajeMCU("Gamora", "Gamora", "F")
    ]
    
    for personaje in personajes:
        cola.arrive(personaje)


# a. determinar el nombre del personaje de la superhéroe Capitana Marvel
def nombre_cap_marvel(cola):
    
    nom_cap_marvel = []
    
    while cola.size() > 0:
        personaje = cola.atention()
        
        if personaje.superheroe == "Capitana Marvel":
            nom_cap_marvel.append(personaje.nombre)
            
    return nom_cap_marvel


# b. mostrar los nombre de los superhéroes femeninos
def superheroes_fem(cola):
    
    nom_heroes_fem = []
    
    while cola.size() > 0:
        personaje = cola.atention()
        
        if personaje.genero == "F":
            nom_heroes_fem.append(personaje.superheroe)
            
    return nom_heroes_fem

            
# c. mostrar los nombres de los personajes masculinos
def superheroes_masc(cola):
    nom_heroes_masc = []

    while cola.size() > 0:
        personaje = cola.atention()

        if personaje.genero == "M":
            nom_heroes_masc.append(personaje.superheroe)

    return nom_heroes_masc


# d. determinar el nombre del superhéroe del personaje Scott Lang
def nombre_scott_lang(cola):
    
    nom_scott_lang = []
    
    while cola.size() > 0:
        personaje = cola.atention()
        
        if personaje.nombre == "Scott Lang":
            nom_scott_lang.append(personaje.superheroe)
            
    return nom_scott_lang


# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S
def nombres_con_s(cola):
    
    while cola.size() > 0:
        personaje = cola.atention()
        
        if personaje.nombre.startswith("S") or personaje.superheroe.startswith("S"):
            print(f"['{personaje.nombre}', '{personaje.superheroe}', '{personaje.genero}']")
            
    
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes
def carol_is(cola):
    
    esta= False
    
    while cola.size() > 0:
        personaje = cola.atention()
        
        if personaje.nombre == "Carol Danvers":
            esta = True
            break
    if esta:
        print(f"{personaje.nombre} está en la cola y su nombre de superheroe es: {personaje.superheroe}")
        return True
    else:
        print("No está en la cola")
        return False
        

cola = Cola()

cargar_personajes(cola)
print("Nombre de la Capitana Marvel:")
print(nombre_cap_marvel(cola)), print('---------------------------------------------')

cargar_personajes(cola)
print("Superheroes femeninos:")
print(superheroes_fem(cola)), print('---------------------------------------------')

cargar_personajes(cola)
print("Superheroes masculinos:")
print(superheroes_masc(cola)), print( '---------------------------------------------')

cargar_personajes(cola)
print("Nombre de superheroe del personaje Scott Lang:")
print(nombre_scott_lang(cola)), print('---------------------------------------------')

cargar_personajes(cola)
print("Personajes o superheroes que empiezan con la letra 'S':")
nombres_con_s(cola), print('---------------------------------------------')

cargar_personajes(cola)
print(carol_is(cola)), print('---------------------------------------------')
