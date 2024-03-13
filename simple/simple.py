import random

def simple_list():

    lista_diccionarios = []
    
    for i in range(10):
        diccionario = {
            "id": i + 1,
            "age": random.randint(1, 100)  
        }
        # Agregar el diccionario a la lista
        lista_diccionarios.append(diccionario)
    
    return lista_diccionarios

def sort_list(dicts):
    
    lista_ordenada = sorted(dicts, key=lambda x: x["age"])
    return lista_ordenada
