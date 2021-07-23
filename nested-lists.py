#Reto Nested Lists de HackerRank
#Me dan pares de la forma [name, score]
#Tengo que crear una lista con la info que me dan
#y escribir en orden alfabetico el nombre de todos
#los que tuvieron el segundo puntaje mas chico

if __name__ == '__main__':
    lista = []
    puntajes = set()
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        lista.append([name,score])
        puntajes.add(score)
    lista.sort(key=lambda a:a[0])
    if len(puntajes)>1 :segundo_minimo = sorted(puntajes)[1]
    else: segundo_minimo = list(puntajes)[0]
    for name,score in lista:
        if score==segundo_minimo: print(name)
